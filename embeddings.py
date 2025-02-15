from textsplitter import splitter
from langchain.embeddings import HuggingFaceEmbeddings

def embeddings():
    texts = splitter()  
    
    # Extract page content from each text document
    text_list = [doc.page_content for doc in texts]
    
    # Initialize HuggingFace embeddings (384 dimensions)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Generate embeddings for each text
    embedding_vectors = embeddings.embed_documents(text_list)
    
    # Return both text data and embeddings
    return text_list, embedding_vectors

if __name__ == "__main__":
    texts, vectors = embeddings()
    print(texts)
    print(vectors)
