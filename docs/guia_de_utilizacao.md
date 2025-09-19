# Guia de Utilização — AI CODER 🤖

Este guia tem como objetivo orientar o usuário sobre como utilizar todas as funcionalidades do AI CODER, desde a configuração inicial até o uso avançado da plataforma.

---

## 1. Instalação e Configuração

### 1.1. Instale as dependências
No terminal, execute:
```bash
pip install -r requirements.txt
```

### 1.2. Configure a chave da API Groq
- Crie um arquivo `.env` na raiz do projeto com:
  ```
  GROQ_API_KEY="sua_chave_aqui"
  ```
- Ou insira a chave diretamente na barra lateral da aplicação.

---

## 2. Executando o AI CODER

No terminal, execute:
```bash
streamlit run app.py
```
Acesse o endereço exibido no terminal para abrir a interface web.

---

## 3. Utilizando a Aplicação

### 3.1. Inserindo sua API Key
- Na barra lateral, insira sua chave Groq para habilitar as funcionalidades.

### 3.2. Enviando dúvidas ou códigos
- Use o campo de chat para enviar perguntas sobre Python ou colar trechos de código para análise.

### 3.3. Recebendo análise e sugestões
- O assistente irá:
  - Avaliar o código (nota de 0 a 10)
  - Apontar pontos positivos e negativos
  - Sugerir melhorias e boas práticas
  - Gerar uma versão corrigida do código

### 3.4. Histórico de conversas
- Todas as interações ficam salvas e podem ser consultadas na interface.

---

## 4. Recomendações de Uso

- Envie trechos de código claros e completos para melhor análise.
- Utilize perguntas objetivas para obter respostas mais precisas.
- Consulte o histórico para acompanhar sua evolução e revisitar sugestões anteriores.

---

## 5. Suporte e Contribuição

- Para dúvidas técnicas, utilize o [GitHub Issues](https://github.com/thirabelloo/ai-coder/issues).
- Para contribuir, siga as instruções do README.

---

**AI CODER** — Seu parceiro para evoluir como desenvolvedor Python!