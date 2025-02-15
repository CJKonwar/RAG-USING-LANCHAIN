from pinecone import Pinecone, ServerlessSpec
import os
from embeddings import embeddings 

api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=api_key)

pc.create_index(
    name="finance",
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ),
    deletion_protection="disabled",
    tags={
        "environment": "development"
    }
)


index = pc.Index("finance")


texts, vectors = embeddings()


result = [(str(i), vector, {"text": text}) for i, (text, vector) in enumerate(zip(texts, vectors))]


index.upsert(vectors=result)

print("Data upserted successfully!")
