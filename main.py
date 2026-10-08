from langchain_mistralai import ChatMistralAI
from vector_store.DB import VectorStore
from dotenv import load_dotenv
from EmbeddingModel.embedding import EmbeddingModel
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model = EmbeddingModel()

llm = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.5
)

vector_store = VectorStore(
    embedding_model.model,
    "./database/chroma_db"
)

retriver=vector_store.retriver( search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 20,
        "lambda_mult": 0.5
    }
    )

multi_query_retriver=MultiQueryRetriever.from_llm(
    retriever=retriver,llm=llm
)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Use only the provided context to answer the user's question.

Instructions:
- Answer only from the given context.
- If the answer is not present in the context, say:
  "I couldn't find the answer in the provided documents."
- Do not make up information.
- Be clear and concise."""
    ),
    (
        "human",
        """Context:
{context}

Question:
{question}"""
    )
])

print("-----welcome-----press 0 for exit--------")
while True:
    
    query=input("You :")
    
    if query=="0":
        break
    docs=multi_query_retriver.invoke(query)

    final_prompt = prompt.invoke({
        "context": "\n\n".join([doc.page_content for doc in docs]),
        "question": query
    })


    response = llm.invoke(final_prompt)

    print("\nAI :\n\n",response.content)


    