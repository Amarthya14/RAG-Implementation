from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

class EmbeddingModel:
    def __init__(self):
        self.model=MistralAIEmbeddings(model="mistral-embed-2312",
                                       )
    # def embedd_query(self,text):
    #     return self.model.embed_query(text)
    # def embedd_document(self,doc):
    #     return self.model.embed_documents_documents(doc)
        

