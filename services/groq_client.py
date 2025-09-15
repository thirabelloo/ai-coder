"""Módulo responsável por interagir com a API Groq para gerar respostas baseadas em prompts."""

import httpx
import streamlit as st
from groq import Groq


def get_groq_response(
    prompt, system_prompt, model="openai/gpt-oss-20b", temperature=0.1, max_tokens=2048
):
    """
    Envia um prompt para a API Groq e retorna a resposta gerada pelo modelo.

    Esta função constrói uma estrutura de mensagens com base no conteúdo do usuário e nas instruções do sistema,
    realiza a chamada ao endpoint de completions da Groq e retorna o conteúdo gerado. Suporta histórico de mensagens
    via sessão e trata erros comuns como ausência de chave de API ou falhas na requisição.

    Parâmetros:
        prompt (str): Texto da mensagem do usuário que será processada pelo modelo.
        system_prompt (str): Instruções que definem o comportamento e o estilo da resposta do modelo.
        model (str, opcional): Identificador do modelo a ser utilizado. Padrão: "openai/gpt-oss-20b".
        temperature (float, opcional): Controla o grau de aleatoriedade da resposta. Padrão: 0.1.
        max_tokens (int, opcional): Número máximo de tokens permitidos na resposta. Padrão: 2048.

    Retorna:
        str | None: Conteúdo da resposta gerada pelo modelo, ou None se a chave da API estiver ausente ou ocorrer erro.

    Raises:
        RuntimeError: Se ocorrer falha na comunicação com a API, parâmetros inválidos ou erro interno do servidor.
    """

    api_key = st.session_state.get("api_key")

    if not api_key:
        st.error("API Key não definida. Por favor, configure-a primeiro.")
        return None

    try:
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

    except httpx.ConnectError as ce:
        st.error(f"Erro de conexão com a API Groq: {type(ce).__name__} - {str(ce)}")
        return None

    except httpx.TimeoutException as te:
        st.error(f"A requisição à API Groq expirou: {type(te).__name__} - {str(te)}")
        return None

    except httpx.HTTPError as he:
        st.error(f"Erro HTTP ao acessar a API Groq: {type(he).__name__} - {str(he)}")
        return None

    except Exception as e:
        st.error(f"Erro inesperado: {type(e).__name__} - {str(e)}")
        raise
