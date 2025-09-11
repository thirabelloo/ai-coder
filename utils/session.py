"""
Módulo utilitário para gerenciamento de sessão e histórico de mensagens
em aplicações Streamlit com interface de chat.
"""

import streamlit as st


def init_session():
    """
    Inicializa a sessão do Streamlit, garantindo que a chave 'messages'
    esteja presente no estado da sessão.

    Se a chave não existir, ela é criada como uma lista vazia"""
    if "messages" not in st.session_state:
        st.session_state.messages = []


def render_chat_history():
    """
    Renderiza o histórico de mensagens armazenado na sessão do Streamlit.

    Para cada mensagem, exibe o conteúdo formatado de acordo com o papel
    (usuário ou sistema) usando o componente st.chat_message.
    """

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
