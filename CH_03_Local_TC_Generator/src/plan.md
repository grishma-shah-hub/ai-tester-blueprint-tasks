# CH_03 Local Test Case Generator — Two-Page Streamlit App

## Context

`CH_03_Local_TC_Generator/` currently contains only design docs (`src/FineTune_Prompt.md`, `src/Prompt.md`), a UI mockup (`src/ApplicationScreenshot.png`), and an output template (`Templates/testcase_creator.md`) — no code exists yet. The chapter's goal is to turn that spec into a working local tool: a chat-style page where a QA engineer types something like "create tc for VWO-49," the app fetches that ticket from Jira, and generates test cases with a local Ollama model (fallback: GROQ), formatted per the existing template. A second settings page persists the Jira/GROQ/Ollama config the user enters, so nothing is hardcoded.

No credentials are known or requested from the user in this session — the settings file will ship with clearly-fake placeholder values (e.g. `your.email@example.com`) that the user fills in themselves after the app is built.

## Approach

**Stack:** Streamlit multipage app, local JSON file for settings (gitignored), `requests` for Jira REST API + GROQ HTTP API, `ollama` python package (or raw HTTP to `localhost:11434`) for local generation.

### File layout (new)

```
CH_03_Local_TC_Generator/
├── src/
│   ├── app.py                  # Page 1: chat interface (Streamlit entrypoint)
│   ├── pages/
│   │   └── 1_Settings.py       # Page 2: settings form (Streamlit auto-discovers pages/*.py)
│   ├── settings_store.py       # load_settings()/save_settings() <-> settings.json
│   ├── jira_client.py          # fetch_ticket(ticket_id) -> title/description/acceptance criteria
│   ├── llm_client.py           # generate_test_cases(prompt) -> tries Ollama, falls back to GROQ
│   ├── prompt_builder.py       # fills Templates/testcase_creator.md with ticket content
│   ├── settings.json           # gitignored; created on first save; dummy placeholders pre-seeded
│   └── settings.example.json   # committed reference with the same dummy placeholders
├── Templates/
│   └── testcase_creator.md     # existing — reused as-is
└── requirements.txt            # streamlit, requests, ollama (or plain requests), python-dotenv (optional)
```

### Page 1 — `app.py` (chat page, matches mockup)

- `st.chat_input` (or text_input + Send button, matching the hand-drawn mockup) for the request, e.g. "create tc for VWO-49".
- On submit: extract ticket ID from the message via regex `[A-Z]+-\d+`. If none found, show an inline error asking the user to include a ticket ID.
- Call `jira_client.fetch_ticket(ticket_id)` using settings loaded via `settings_store.load_settings()`.
- Build the generation prompt via `prompt_builder`, which reads `Templates/testcase_creator.md` and substitutes `[FEATURE]`/`[PASTE REQUIREMENTS HERE]` with the ticket's summary/description, and fills `[NUMBER]` with a reasonable default (e.g. "5-10").
- Call `llm_client.generate_test_cases(prompt)`; render the returned markdown table in the chat pane (`st.session_state` keeps chat history for the session).
- Surface clear errors if Jira fetch fails (bad ticket/auth) or if both Ollama and GROQ fail.

### Page 2 — `pages/1_Settings.py`

- Form fields matching the mockup: Jira Email, Jira Token (password-masked), Jira URL, Ollama URL, GROQ Token (password-masked).
- Pre-populate from `settings_store.load_settings()` (falls back to placeholder defaults if `settings.json` doesn't exist yet).
- "Save Settings" button writes via `settings_store.save_settings(...)` to `settings.json`.

### `settings_store.py`

- `DEFAULT_SETTINGS` dict with dummy placeholders:
  - `jira_email`: `your.email@example.com`
  - `jira_token`: `your_jira_api_token_here`
  - `jira_url`: `https://your-domain.atlassian.net`
  - `ollama_url`: `http://localhost:11434`
  - `groq_token`: `your_groq_api_key_here`
- `load_settings()`: reads `settings.json` if present, else returns `DEFAULT_SETTINGS`.
- `save_settings(dict)`: writes `settings.json` (pretty JSON).
- `settings.json` added to repo root `.gitignore`; `settings.example.json` (same placeholder values) committed so the file's shape is documented without risking real secrets ever being committed.

### `jira_client.py`

- `fetch_ticket(ticket_id, settings)`: GET `{jira_url}/rest/api/3/issue/{ticket_id}` with HTTP Basic Auth (`jira_email`, `jira_token`); extract `fields.summary` and `fields.description` (Jira Cloud v3 description is Atlassian Document Format — flatten to plain text). Raise a clear exception on 401/404 that the UI can display.

### `llm_client.py`

- `generate_test_cases(prompt, settings)`:
  1. Try Ollama: POST `{ollama_url}/api/generate` with `model="gemma3:1b"`, the built prompt, `stream=False`.
  2. On connection error/timeout, fall back to GROQ: POST `https://api.groq.com/openai/v1/chat/completions` with `Authorization: Bearer {groq_token}`.
  3. If both fail, raise/return an error message the chat page displays instead of crashing.

### `prompt_builder.py`

- Reads `Templates/testcase_creator.md`, substitutes placeholders (`[FEATURE]`, `[NUMBER]`, `[PASTE REQUIREMENTS HERE]`) with the Jira ticket's summary/description, and appends a note to follow `CH_01_LLM_Basics/ch_01_anti_hallucination.md` conventions ("Not specified" for missing info), consistent with this repo's established prompt style.

### `.gitignore` update

- Add `settings.json`, `__pycache__/`, `.venv/`, `*.pyc` (none of these are currently ignored at repo root).

## Verification

1. `pip install -r CH_03_Local_TC_Generator/requirements.txt`
2. `streamlit run CH_03_Local_TC_Generator/src/app.py`
3. Open Settings page, confirm placeholder values are visible/editable, fill in the user's real Jira/GROQ credentials manually (not by me), click Save, confirm `settings.json` is written and gitignored.
4. On the chat page, type `create tc for VWO-49`, click Send, confirm: ticket fetched, test cases generated via local Ollama (gemma3:1b) and rendered as a markdown table matching the template's columns.
5. Temporarily stop Ollama (or point `ollama_url` at a bad port) and re-run the same request to confirm GROQ fallback triggers and still returns test cases.
6. Try a message with no valid ticket ID and confirm a friendly inline error instead of a crash.
