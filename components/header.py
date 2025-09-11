"""Módulo responsável por renderizar o cabeçalho da interface do AI Coder usando Streamlit."""

import streamlit as st


def render_header():
    """
    Exibe o cabeçalho principal da aplicação AI Coder com título, subtítulo e descrição.

    Utiliza componentes visuais do Streamlit para apresentar o nome do projeto,
    uma breve explicação e um toque visual com emojis.
    """

    st.title("💻 AI Coder - Seu Copiloto Python")
    st.subheader("Assistente Inteligente para Programação em Python 🐍")
    st.caption(
        "Explore conceitos, gere códigos sob demanda e aprenda com explicações claras e diretas."
    )
