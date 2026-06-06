from pathlib import Path

from news_analytics import get_api_keys, get_everything, summarize_with_mistral

TOPIC = "футбольные команды"
OUTPUT_FILE = Path(__file__).resolve().parent / "text.txt"


def main() -> None:
    news_key, mistral_key = get_api_keys()

    result = get_everything(news_key, {"q": TOPIC})
    articles = result.get("articles", [])

    text = summarize_with_mistral(mistral_key, articles)

    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(OUTPUT_FILE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
