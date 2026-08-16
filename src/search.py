import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_openai import ChatOpenAI


PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


def search_prompt(question=None):

  # Montando o Prompt
  template = PromptTemplate(
    input_variables=["contexto", "pergunta"],
    template=PROMPT_TEMPLATE
  )
  model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
  chain = template | model

  # Configuração do store para o PGVector.
  embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))
  store = PGVector(
    embeddings=embeddings,
    connection=os.getenv("DATABASE_URL"),
    collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
    use_jsonb=True,
  )

  results = store.similarity_search_with_score(question, k=10)

  contexto = "\n".join([doc.page_content for doc, _ in results])

  result = chain.invoke({"contexto": contexto, "pergunta": question})
  
  return result.content