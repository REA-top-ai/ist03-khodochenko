import os
from pathlib import Path

import requests as r

base_url = "https://newsapi.org/v2"


def _load_env_file() -> None:
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.is_file():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        os.environ.setdefault(key, value)


def get_api_keys() -> tuple[str, str]:
    _load_env_file()
    news_key = os.environ.get("NEWS_API_KEY", "").strip()
    mistral_key = os.environ.get("MISTRAL_API_KEY", "").strip()
    if not news_key:
        raise ValueError(
            "Не задан NEWS_API_KEY. Добавьте ключ в файл .env (см. .env.example)."
        )
    if not mistral_key:
        raise ValueError(
            "Не задан MISTRAL_API_KEY. Добавьте ключ в файл .env (см. .env.example)."
        )
    return news_key, mistral_key


def get_everything(api_key: str, params: dict | None = None) -> dict:
    final_params = {
        key: value
        for key, value in (params or {}).items()
        if value is not None
    }
    return _make_request("everything", api_key, final_params)


def _make_request(endpoint: str, api_key: str, params: dict | None = None) -> dict:
    url = f"{base_url}/{endpoint}"
    query = {"apiKey": api_key}
    if params:
        query.update(params)

    try:
        response = r.get(url, params=query, timeout=10)
        response.raise_for_status()
        data = response.json()
    except r.exceptions.RequestException as e:
        raise RuntimeError(f"Ошибка обращения к NewsAPI ({endpoint}): {e}") from e
    except ValueError as e:
        raise RuntimeError(f"Ошибка парсинга JSON NewsAPI ({endpoint}): {e}") from e

    if data.get("status") != "ok":
        raise RuntimeError(
            f"NewsAPI вернул ошибку: {data.get('code')} — {data.get('message')}"
        )
    return data


def summarize_with_mistral(api_key: str, articles: list[dict]) -> str:
    if not articles:
        raise ValueError("Нет статей для суммаризации.")

    url = "https://api.mistral.ai/v1/chat/completions"
    articles_text = ""
    for i, article in enumerate(articles[:10], 1):
        articles_text += (
            f"{i}. {article.get('title')} — {article.get('description')}\n"
        )

    prompt = f"""
Ты аналитик новостей. Сделай аннотацию (250-300 слов) на русском языке
по этим статьям за последний день. Добавь оценку ситуации и общий вывод.

{articles_text}
"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "mistral-small",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = r.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
    except r.exceptions.RequestException as e:
        raise RuntimeError(f"Ошибка обращения к Mistral API: {e}") from e
    except ValueError as e:
        raise RuntimeError(f"Ошибка парсинга JSON Mistral API: {e}") from e

    try:
        return result["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise RuntimeError(f"Неожиданный ответ Mistral API: {result}") from e
