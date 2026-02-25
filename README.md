# AI CODER 🤖

AI Coder é uma aplicação web desenvolvida em Python com Streamlit, projetada para auxiliar desenvolvedores na análise, avaliação e aprimoramento de códigos Python utilizando inteligência artificial. O sistema integra a API Groq para gerar respostas inteligentes, sugestões de melhorias e correções automáticas, promovendo boas práticas e acelerando o aprendizado de desenvolvedores de todos os níveis.

## Funcionalidades

- **Análise de Código Python:** Avaliação automática de trechos de código, com nota de 0 a 10 baseada em critérios profissionais.
- **Sugestões de Melhoria:** Pontos positivos, negativos e recomendações detalhadas para aprimorar o código.
- **Correção Automática:** Geração de versões corrigidas e otimizadas do código enviado.
- **Chat Interativo:** Interface conversacional para dúvidas sobre Python e boas práticas de programação.
- **Histórico de Conversas:** Registro das interações para consulta e acompanhamento da evolução.
- **Integração com Groq API:** Utilização de modelos avançados de linguagem para respostas precisas e contextualizadas.

## Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Groq API](https://groq.com/)
- [httpx](https://www.python-httpx.org/)

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/thirabelloo/ai-coder.git
   cd ai-coder
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure sua chave da API Groq:**
   - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
     ```
     GROQ_API_KEY="sua_chave_aqui"
     ```
   - Ou insira a chave diretamente na barra lateral da aplicação.

4. **Execute o projeto:**
   ```bash
   streamlit run app.py
   ```

## Estrutura do Projeto

```
ai-coder/
├── app.py                  # Arquivo principal da aplicação Streamlit
├── components/             # Componentes de UI (header, sidebar, etc)
├── config/                 # Configurações e prompts do sistema
├── documentos/             # Documentação e guias de uso do projeto
│   └── guia_de_utilizacao.md
├── services/               # Integração com APIs externas (Groq)
├── utils/                  # Utilitários e funções auxiliares
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## Contribuição

Contribuições são bem-vindas! Siga as etapas abaixo:

1. Fork este repositório.
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Dúvidas, sugestões ou feedback?  
Entre em contato pelo [GitHub Issues](https://github.com/thirabelloo/ai-coder/issues).

---

**AI CODER** — Seu assistente inteligente para escrever, revisar e evoluir código Python!