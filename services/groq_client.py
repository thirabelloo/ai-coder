"""Módulo responsável por interagir com a API Groq para gerar respostas baseadas em prompts."""

import streamlit as st
from groq import Groq


def get_groq_response(
    prompt, system_prompt, model="openai/gpt-oss-20b", temperature=0.1, max_tokens=2048
):
    """
    Gera uma resposta da API Groq com base em um prompt fornecido.

    Parâmetros:
        prompt (str): O conteúdo da mensagem do usuário.
        system_prompt (str): Instruções para o comportamento do modelo.
        model (str): Identificador do modelo a ser utilizado.
        temperature (float): Grau de aleatoriedade na resposta.
        max_tokens (int): Número máximo de tokens na resposta.

    Retorna:
        str: Conteúdo da resposta gerada pelo modelo, ou None se a API Key não estiver definida.
    """

    api_key = st.session_state.get("api_key")

    if not api_key:
        st.error("API Key não definida. Por favor, configure-a primeiro.")
        return None

    client = Groq(api_key=api_key)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    if "messages" in st.session_state:
        messages.extend(st.session_state.messages)

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return chat_completion.choices[0].message.content
