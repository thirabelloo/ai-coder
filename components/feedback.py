"""Módulo responsável por renderizar o componente de feedback no Streamlit."""

import streamlit as st


def render_feedback(pergunta, resposta):
    """
    Renderiza um formulário de feedback com avaliação positiva/negativa,
    campo de comentário opcional e botão de envio.

    Args:
        pergunta (str): A pergunta feita pelo usuário.
        resposta (str): A resposta gerada que será avaliada.
    """

    st.markdown("### Avalie esta resposta:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Útil"):
            st.session_state.feedback = "positivo"

    with col2:
        if st.button("👎 Não ajudou"):
            st.session_state.feedback = "negativo"

    comentario = st.text_area(
        "Comentário (opcional):", placeholder="Conte por que foi útil ou não..."
    )

    if st.button("Enviar Feedback"):
        st.session_state.feedback_data = {
            "avaliacao": st.session_state.get("feedback"),
            "comentario": comentario,
            "pergunta": pergunta,
            "resposta": resposta,
        }
        st.success("Feedback enviado com sucesso!")
