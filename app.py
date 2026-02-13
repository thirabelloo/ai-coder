"""
Aplicação principal do AI Coder: assistente inteligente para análise e aprimoramento de código
Python via Streamlit.
"""

import logging
import os

import streamlit as st
from dotenv import load_dotenv

from components.header import render_header
from components.sidebar import render_sidebar
from config.prompts_system import SYSTEM_PROMPT
from services.groq_client import get_groq_response
from utils.session import init_session, render_chat_history

st.set_page_config(page_title="AI Coder", page_icon="🤖", layout="wide")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

load_dotenv()


def _ensure_session_messages() -> None:
    """Garante que a lista de mensagens exista no estado da sessão."""
    if "messages" not in st.session_state:
        st.session_state.messages = []


def _append_message(role: str, content: str) -> None:
    """Adiciona uma mensagem ao histórico da sessão."""
    st.session_state.messages.append({"role": role, "content": content})


def _handle_user_prompt(user_prompt: str, api_key: str) -> None:
    """Processa a pergunta do usuário e exibe a resposta do Groq."""

    if not user_prompt.strip():
        st.warning("Digite uma pergunta válida.")
        return

    # Persistir a chave na sessão
    st.session_state.api_key = api_key

    # Adicionar mensagem do usuário
    _append_message("user", user_prompt)

    # Exibir mensagem do usuário
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Chamada ao Groq
    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            try:
                response = get_groq_response(user_prompt, SYSTEM_PROMPT)
            except Exception as exc:
                st.error(f"Erro ao consultar Groq: {exc}")
                logging.exception("Falha na chamada Groq")
                return

            st.markdown(response)
            _append_message("assistant", response)


def main() -> None:
    """Executa a aplicação Streamlit."""
    api_key = render_sidebar()

    # Se não houver na sidebar, tenta pegar do .env
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")

    # Renderiza cabeçalho e inicializa sessão
    render_header()
    init_session()
    render_chat_history()

    # Garante que a lista de mensagens exista
    _ensure_session_messages()

    # Entrada do usuário
    if user_prompt := st.chat_input("Qual sua dúvida sobre Python?"):
        if not api_key:
            st.warning(
                "Por favor, insira sua API Key da Groq na barra lateral para começar."
            )
            st.stop()

        _handle_user_prompt(user_prompt, api_key)


if __name__ == "__main__":
    main()
