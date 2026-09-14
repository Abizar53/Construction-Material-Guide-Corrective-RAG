from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import typesense
from langchain_community.vectorstores import Typesense
from dotenv import load_dotenv
import os


load_dotenv(r"D:\RAG Projects\Basic Rag\src\ENV\.env")
Typesense_API_1=os.getenv("Typesense_API")


client=typesense.Client({
            "api_key": Typesense_API_1,
            "nodes": [{"host": "a2bqkhfzjwopd5e6p-1.a1.typesense.net",
                       "port": "443",
                       "protocol": "https"}],    
            "connection_timeout_seconds": 300,
            "typesense_collection_name": "Langchain_DB"
     })

client

# Generate Embeddigs + vector data(Typesense)
# this function could take both argument,runs in two ways (if model is provided / model not provided)
def EmbeddingVectorStore(
    documents: list[Document],
    Model=None
):
    if Model is None:
        Model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    Cloud_DB = Typesense.from_documents(documents=documents , embedding=Model , typesense_client=client
    )

    return Cloud_DB

#print(client.collections.retrieve())