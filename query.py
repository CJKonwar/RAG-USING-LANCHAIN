from vector_store import vectorstore

query = "what is finance"


results = vectorstore.similarity_search(
    query,  
    k=3  
)

for i, doc in enumerate(results, 1):
    print(f"Result {i}:")
    print(doc.page_content) 
    print("-" * 80)
