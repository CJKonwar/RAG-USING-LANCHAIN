from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
from pinecone import Pinecone as PineconeClient
import os

api_key = os.getenv("PINECONE_API_KEY")
pc = PineconeClient(api_key=api_key)

index_name = "finance"
index = pc.Index(index_name)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


vectorstore = Pinecone(index, embeddings, text_key="text")
