from load import loader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def splitter():
   
    document = loader()  
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    
    
    texts = splitter.split_documents(document)
    return texts


if __name__ == "__main__":
    chunks = splitter()
    
