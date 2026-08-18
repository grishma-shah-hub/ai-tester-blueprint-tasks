import json
from pathlib import Path

SETTINGS_PATH = Path(__file__).parent / "settings.json"

DEFAULT_SETTINGS = {
    "jira_email": "your.email@example.com",
    "jira_token": "your_jira_api_token_here",
    "jira_url": "https://your-domain.atlassian.net",
    "ollama_url": "http://localhost:11434",
    "groq_token": "your_groq_api_key_here",
}


def load_settings() -> dict:
    if SETTINGS_PATH.exists():
        with open(SETTINGS_PATH, "r") as f:
            data = json.load(f)
        return {**DEFAULT_SETTINGS, **data}
    return dict(DEFAULT_SETTINGS)


def save_settings(settings: dict) -> None:
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)
