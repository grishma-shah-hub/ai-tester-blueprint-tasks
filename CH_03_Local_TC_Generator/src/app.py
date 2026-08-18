import re

import streamlit as st

from jira_client import JiraFetchError, fetch_ticket
from llm_client import GenerationError, generate_test_cases
from prompt_builder import build_prompt
from settings_store import load_settings

TICKET_ID_PATTERN = re.compile(r"[A-Z][A-Z0-9]*-\d+")

st.set_page_config(page_title="Local TC Generator", page_icon="🧪")
st.title("🧪 Local Test Case Generator")
st.caption("Type a request like: create tc for VWO-49")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("create tc for VWO-49")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    match = TICKET_ID_PATTERN.search(user_input.upper())

    with st.chat_message("assistant"):
        if not match:
            reply = (
                "I couldn't find a Jira ticket ID in that message. "
                "Try something like: `create tc for VWO-49`"
            )
            st.markdown(reply)
        else:
            ticket_id = match.group(0)
            settings = load_settings()
            try:
                with st.spinner(f"Fetching {ticket_id} from Jira..."):
                    ticket = fetch_ticket(ticket_id, settings)
                prompt = build_prompt(ticket)
                with st.spinner("Generating test cases..."):
                    reply = generate_test_cases(prompt, settings)
                st.markdown(reply)
            except JiraFetchError as e:
                reply = f"⚠️ Jira error: {e}"
                st.markdown(reply)
            except GenerationError as e:
                reply = f"⚠️ Generation error: {e}"
                st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
