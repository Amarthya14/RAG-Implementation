from langchain_text_splitters import  CharacterTextSplitter,TokenTextSplitter,RecursiveCharacterTextSplitter
from document_loader.loader import text_loader


def split_text(doc):
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=100,
        chunk_overlap=20,
        # length_function=len,
        # is_separator_regex=False,
    )
    texts = text_splitter.split_documents(doc)
    return texts

def split_tokens(doc):
    text_splitter = TokenTextSplitter(chunk_size=10, chunk_overlap=2)

    texts = text_splitter.split_documents(doc)
    return texts

def split_recursive(doc):
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=20,
    # length_function=len,
    # is_separator_regex=False,
)
    texts = text_splitter.split_documents(doc)
    return texts
    

if __name__ == "__main__":
    doc=text_loader("./files/text.txt")
    splitted_text=split_recursive(doc)
    for i in splitted_text:
        print(i.page_content)
    