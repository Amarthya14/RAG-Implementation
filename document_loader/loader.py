from langchain_community.document_loaders import TextLoader,PyPDFLoader,WebBaseLoader

def text_loader(file_path):
    loader = TextLoader(file_path)
    docs = loader.load()
    return docs

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs
def webpage_loader(file_path):
    loader = WebBaseLoader(file_path)
    docs = loader.load()
    return docs

