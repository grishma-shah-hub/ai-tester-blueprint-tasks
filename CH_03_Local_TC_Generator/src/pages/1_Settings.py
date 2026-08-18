import streamlit as st

from settings_store import load_settings, save_settings

st.set_page_config(page_title="Settings", page_icon="⚙️")
st.title("⚙️ Settings")

current = load_settings()

with st.form("settings_form"):
    jira_email = st.text_input("Jira Email", value=current["jira_email"])
    jira_token = st.text_input("Jira Token", value=current["jira_token"], type="password")
    jira_url = st.text_input("Jira URL", value=current["jira_url"])
    ollama_url = st.text_input("Ollama URL", value=current["ollama_url"])
    groq_token = st.text_input("GROQ Token", value=current["groq_token"], type="password")

    submitted = st.form_submit_button("Save Settings")

    if submitted:
        save_settings(
            {
                "jira_email": jira_email,
                "jira_token": jira_token,
                "jira_url": jira_url,
                "ollama_url": ollama_url,
                "groq_token": groq_token,
            }
        )
        st.success("Settings saved.")
