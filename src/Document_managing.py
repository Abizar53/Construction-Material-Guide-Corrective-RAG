from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader, CSVLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

def Load_documents(file_path):
    Documents=PyPDFLoader(file_path)
    loaded_document=Documents.load()
    return loaded_document

def Recursive_chunks(documents : list[Document]):
    splitter=RecursiveCharacterTextSplitter(chunk_size=452, chunk_overlap=52)
    chunked_document=splitter.split_documents(documents)
    return chunked_document 




