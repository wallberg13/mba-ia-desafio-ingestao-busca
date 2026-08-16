# Desafio MBA Engenharia de Software com IA - Full Cycle

## Passo a passo para executar o projeto

Siga as etapas abaixo para executar a solução:

1. **Clone o repositório**

   ```bash
   git clone https://github.com/wallberg13/mba-ia-desafio-ingestao-busca
   cd mba-ia-desafio-ingestao-busca
   ```

2. **Crie e ative o ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**
   - Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

     ```
     OPENAI_EMBEDDING_MODEL='text-embedding-3-small'
     OPENAI_API_KEY=<sua-chave-openai>
     PDF_PATH=./document.pdf
     DATABASE_URL=<url-do-seu-postgres>
     PG_VECTOR_COLLECTION_NAME=<nome-da-colecao>
     ```

   - Certifique-se de que o arquivo `document.pdf` está na raiz do projeto ou ajuste o caminho em `PDF_PATH`.

5. **Suba os containers com Docker Compose**

   ```bash
   docker compose up -d
   ```

6. **Ingestione o PDF no banco de vetores**

   ```bash
   python ./src/ingest.py
   ```

7. **Execute o Chat e interaja com seu documento**

   ```bash
   python ./src/chat.py
   ```

Pronto! Agora você pode fazer perguntas sobre o conteúdo do PDF via terminal.
Para sair, no terminal, basta digitar "sair".
