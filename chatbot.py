from langchain.prompts import PromptTemplate
from llm import llm  
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from vector_store import vectorstore
from langchain.tools import Tool
from langchain.agents import initialize_agent

def conversational_memory():
    return ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
    )

def retrievalQA():
    
    qa = RetrievalQA.from_chain_type(
        llm=llm(),  # Call llm() to get the instance
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
        
    )
    return qa

def tools():
    qa = retrievalQA()
    Tools = [
        Tool(
            name='Knowledge Base',
            func=lambda query: qa.run(query), 
            description='Use this tool to answer questions using the knowledge base'
        )
    ]
    return Tools

def agent():
    
    chat_agent = initialize_agent(
        tools=tools(),
        llm=llm(),  
        agent="zero-shot-react-description",
        memory=conversational_memory(),
        verbose=True,
        handle_parsing_errors=True  
    )
    return chat_agent

if __name__ == "__main__":
    chat_agent = agent()
    message = str(input("Enter your message: "))
    response = chat_agent.run(message)
    print(response)