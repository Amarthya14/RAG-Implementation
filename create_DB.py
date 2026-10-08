# from langchain_google_genai import GoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from document_loader.loader import text_loader,pdf_loader,webpage_loader
from text_splitter.splitters import split_text,split_tokens,split_recursive
from vector_store.DB import VectorStore
from EmbeddingModel.embedding import EmbeddingModel
from dotenv import load_dotenv

load_dotenv()


embedding_model=EmbeddingModel()

vector_store=VectorStore(embedding_model.model,persist_directory="./database/chroma_db")

prompt=ChatPromptTemplate.from_messages([("system","Give the summary of the texts"),("human","{content}")])

# doc =text_loader("./files/text.txt")
doc=pdf_loader("./files/UVCE_BTech_CashfreePayments_JD_2027.pdf")

splitted_text=split_recursive(doc)

vector_store.add_documents(splitted_text)


# contents = [doc.page_content for doc in docs]

# final_prompt=prompt.invoke({"content":doc[0].page_content})



# result=model.invoke(final_prompt)

# print(result.content)
