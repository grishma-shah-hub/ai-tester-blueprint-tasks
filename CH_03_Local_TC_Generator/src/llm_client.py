from typing import Optional

import requests

OLLAMA_MODEL = "gemma3:1b"
GROQ_MODEL = "llama-3.1-8b-instant"
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


class GenerationError(Exception):
    pass


def _try_ollama(prompt: str, ollama_url: str) -> Optional[str]:
    try:
        response = requests.post(
            f"{ollama_url.rstrip('/')}/api/generate",
            json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException:
        return None


def _try_groq(prompt: str, groq_token: str) -> Optional[str]:
    if not groq_token:
        return None
    try:
        response = requests.post(
            GROQ_URL,
            headers={"Authorization": f"Bearer {groq_token}"},
            json={
                "model": GROQ_MODEL,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except (requests.exceptions.RequestException, KeyError, IndexError):
        return None


def generate_test_cases(prompt: str, settings: dict) -> str:
    result = _try_ollama(prompt, settings.get("ollama_url", ""))
    if result:
        return result

    result = _try_groq(prompt, settings.get("groq_token", ""))
    if result:
        return result

    raise GenerationError(
        "Could not generate test cases. Ollama is unreachable and GROQ fallback "
        "also failed — check the Ollama URL and GROQ token in Settings."
    )
