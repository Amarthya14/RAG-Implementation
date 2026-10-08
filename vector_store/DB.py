from langchain_chroma import Chroma

class VectorStore:
    def __init__(self, embedding_model, persist_directory):
            self.db = Chroma(
                persist_directory=persist_directory,
                embedding_function=embedding_model
            )

    def add_documents(self, documents):
        self.db.add_documents(documents)

    def similarity_search(self, query, k=4):
        return self.db.similarity_search(query, k=k)
    
    def retriver(self,search_type,search_kwargs=None):
        return self.db.as_retriever(
            search_type=search_type,
            search_kwargs=search_kwargs or {}
        )