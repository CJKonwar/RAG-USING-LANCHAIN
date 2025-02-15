from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_google_genai import HarmCategory, HarmBlockThreshold

load_dotenv()

def llm():
    os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
    chatbot = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Updated model name
        temperature=0.7,
        max_tokens=512,
        max_retries=2,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return chatbot