import requests
from datetime import datetime, timedelta

NEWS_API_KEY = "9f126b1c3db9410ab90a72b808fcb7bc"
MISTRAL_API_KEY = "nlextYOnoFYFwAX41D3RyiudZR7R60Xp"

def get_news(topic):
    url = "https://newsapi.org/v2/everything"
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    params = {
        "q": topic,
        "from": yesterday,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY,
        "pageSize": 3
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = []
    for article in data.get("articles", []):
        articles.append({
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "content": (article.get("content") or "")[:200]
        })
    return articles

def build_prompt(articles, topic):
    prompt = f"Ты аналитик. Проанализируй новости за последний день по теме '{topic}'.\n\n"

    for i, art in enumerate(articles, 1):
        prompt += f"{i}. {art['title']}\n"
        prompt += f"{art['description']}\n"
        prompt += f"{art['content']}\n\n"

    prompt += (
        "Сделай аналитическую аннотацию на русском языке (250-300 слов). "
        "Опиши основные события, тренды и общий вывод."
    )

    return prompt


def generate_summary(prompt):
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistral-small",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()


        if "choices" not in result:
            print("Ошибка API:")
            print(result)
            return "Ошибка: проверь API ключ или тариф"

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("Ошибка запроса:", e)
        return "Ошибка при запросе к AI"


def generate_news_summary(topic):
    articles = get_news(topic)
    if not articles:
        return "Нет новостей по теме"
    prompt = build_prompt(articles, topic)
    summary = generate_summary(prompt)
    return summary


def save_to_file(text):
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    topic = "soccer"
    result = generate_news_summary(topic)
    save_to_file(result)
    print("Готово")