"""Este módulo define a barra lateral do app Streamlit, com informações, links e campo para a API Key."""

import streamlit as st


def render_sidebar():
    """Renderiza a barra lateral do aplicativo com título, descrições, links e campo para API Key."""
    st.sidebar.title("AI Coder 🤖")
    st.sidebar.markdown(
        "Um assistente Brasilero focado em ajudar desenvolvedores a escreverem códigos de alta qualidade."
    )
    st.sidebar.markdown("---")
    st.sidebar.info(
        "👤 Desenvolvido por [Thiago Rabello](https://br.linkedin.com/in/thiago-rabelloo) "
    )
    st.sidebar.markdown(
        "📚 Documentação: [GitHub](https://github.com/thirabelloo/ai-coder/blob/main/docs/guia_de_utilizacao.md)"
    )

    st.sidebar.markdown("🔑 Obtenha uma chave em  [Groq](https://console.groq.com/)")
    st.sidebar.markdown("---")

    return st.sidebar.text_input(
        "Insira sua API Key da Groq", type="password", placeholder="Ex: groq-abc123..."
    )
