"""Aplicação principal do AI Coder: assistente inteligente para análise e aprimoramento de código
Python via Streamlit."""

import os

import streamlit as st
from dotenv import load_dotenv

from components.header import render_header
from components.sidebar import render_sidebar
from config.prompts_sytem import SYSTEM_PROMPT
from services.groq_client import get_groq_response
from utils.session import init_session, render_chat_history

st.set_page_config(page_title="AI Coder", page_icon="🤖", layout="wide")

load_dotenv()

api_key = render_sidebar()

if not api_key:
    api_key = os.getenv("GROQ_API_KEY")

render_header()
init_session()
render_chat_history()

if user_prompt := st.chat_input("Qual sua dúvida sobre Python?"):
    if not api_key:
        st.warning(
            "Por favor, insira sua API Key da Groq na barra lateral para começar."
        )
        st.stop()

    st.session_state.api_key = api_key
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            response = get_groq_response(user_prompt, SYSTEM_PROMPT)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
