ROLE:
You are a Senior Python Developer building a lightweight local automation tool for QA test case generation.

INSTRUCTIONS:
- Build a simple two-page Python web application with a frontend (e.g. Streamlit or an equivalent simple Python frontend framework).
- Page 1 (main/chat page): a ChatGPT-like interface where the user types a request (e.g. "create test cases for this Jira ID") and clicks a "Send" button.
- On Send, the app must automatically fetch the corresponding ticket's details from Jira.
- The app must then generate test cases based on the fetched Jira ticket content, using the template already present in the template folder.
- Page 2 (settings page): a configuration screen where the user can enter and save: Jira email ID, Jira URL, Jira API token, and GROQ token.
- Use the already-running local Ollama connection (model: gemma3:1b) as the primary engine for generating test cases.
- [Fallback] If the user does not want to use Ollama, fall back to GROQ (groq.com) as a cloud LLM option, using the GROQ token saved on the settings page.

CONTEXT:
- Jira URL, Jira API token, and Jira email ID will be provided by the user (entered and saved via the settings page).
- Ollama is already installed and running locally with the gemma3:1b model available.
- A template folder already exists in the project containing the test case template(s) to follow when generating output.

EXPECTED:
A working, simple two-page local application: one page for chat-style interaction (request → fetch Jira ticket → generate test cases), and one settings page to configure and persist Jira and GROQ credentials.

PARAMETERS:
- Do not hardcode any credentials (Jira token, GROQ token) into the code — they must be entered via the settings page and saved/read from there.
- Primary generation engine is local Ollama (gemma3:1b); GROQ is a fallback only, used when Ollama is not selected/available.
- Test case generation must follow the format/structure defined in the existing template folder.

OUTPUT:
A simple two-page Python application (chat/interaction page + settings page), with working Jira fetch integration, Ollama as primary LLM, and GROQ as fallback.

TONE: Simple, functional, minimal — this is a lightweight local tool, not a production enterprise system.