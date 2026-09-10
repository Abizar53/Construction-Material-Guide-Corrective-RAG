from Document_managing import Load_documents,Recursive_chunks
from Vector_Store import EmbeddingVectorStore
# Loader
file_path="Data/Building_Materials_Product_Database (1).pdf"
docs_load=Load_documents(file_path)
print("Documents loaded:", len(docs_load))
# chunking ---> Recursive text splitter
chunked=Recursive_chunks(docs_load)
print("Chunks created:", len(chunked))

# vector Database ---> Typesene
#
Vector_DB=EmbeddingVectorStore(chunked)
print("Vector store created successfully!")

# Till now Data ingestion pipeline completed
# Now retriever pipeline will start






