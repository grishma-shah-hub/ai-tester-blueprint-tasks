import requests


class JiraFetchError(Exception):
    pass


def _flatten_adf(node) -> str:
    """Flatten Jira's Atlassian Document Format description into plain text."""
    if node is None:
        return ""
    if isinstance(node, str):
        return node

    text_parts = []
    if isinstance(node, dict):
        if node.get("type") == "text":
            text_parts.append(node.get("text", ""))
        for child in node.get("content", []) or []:
            text_parts.append(_flatten_adf(child))
        if node.get("type") in ("paragraph", "heading"):
            text_parts.append("\n")
    return "".join(text_parts)


def fetch_ticket(ticket_id: str, settings: dict) -> dict:
    jira_url = settings["jira_url"].rstrip("/")
    url = f"{jira_url}/rest/api/3/issue/{ticket_id}"

    try:
        response = requests.get(
            url,
            auth=(settings["jira_email"], settings["jira_token"]),
            headers={"Accept": "application/json"},
            timeout=15,
        )
    except requests.exceptions.RequestException as e:
        raise JiraFetchError(f"Could not reach Jira at {jira_url}: {e}")

    if response.status_code == 401:
        raise JiraFetchError("Jira authentication failed. Check email/token in Settings.")
    if response.status_code == 404:
        raise JiraFetchError(f"Ticket '{ticket_id}' not found.")
    if not response.ok:
        raise JiraFetchError(f"Jira returned {response.status_code}: {response.text[:200]}")

    data = response.json()
    fields = data.get("fields", {})
    summary = fields.get("summary", "")
    description = _flatten_adf(fields.get("description")).strip()

    return {
        "id": ticket_id,
        "summary": summary,
        "description": description,
    }
