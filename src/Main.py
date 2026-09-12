from Document_managing import Load_documents,Recursive_chunks
from Vector_Store import EmbeddingVectorStore
from Temlates import Get_Prompt_template


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

Question="dimension of ceramic floor tiles"
# Retirver pipeline from vector store
Retriver_pipeline=Vector_DB.as_retriever(search_type='similarity',search_kwargs={"k":4})  
# Retrive Relevant content
Retrived_docs=Retriver_pipeline.invoke(Question)
# convert into text, (take only page content)
Content_text="\n\n".join(docs.page_content for docs in Retrived_docs)
#prompt template
Template = Get_Prompt_template()
Retrived_docs=Template.invoke({
    "Context": Context,
    "Question": "What is cement used for?"
})

print(Retrived_docs)






