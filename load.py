from langchain_community.document_loaders import PyPDFLoader

def loader():
    loader = PyPDFLoader("Resources/Introduction to stockmarket.pdf")  # Ensure the correct path
    document = loader.load()
    return document

if __name__ == "__main__":
    loader()