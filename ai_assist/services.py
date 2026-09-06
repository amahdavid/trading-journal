import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_trade_summary(trade_data: dict, model: str = "llama3") -> str:
    prompt = (
        "Summarize this options trade in plain English and flag any rule "
        f"violations: {trade_data}"
    )
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
        timeout=60,
    )
    response.raise_for_status()
    return response.json().get("response", "")
