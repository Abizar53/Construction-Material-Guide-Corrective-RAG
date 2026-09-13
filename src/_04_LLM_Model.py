import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv(r"D:\RAG Projects\Learning_RAG-Langchain\.env")
Grok_API_1=os.getenv("Grok_api")

def LLModel():
    LLM=ChatGroq(model_name="openai/gpt-oss-120b",groq_api_key=Grok_API_1, max_tokens=256)
    return LLM

