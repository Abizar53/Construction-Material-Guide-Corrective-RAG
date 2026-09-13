from _01_Document_managing import Load_documents,Recursive_chunks,Format_docs
from _02_Vector_Store import EmbeddingVectorStore
from _03_Temlates import Get_Prompt_template
from _04_LLM_Model import LLModel
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# Loader
file_path="Data/Building_Materials_Product_Database (1).pdf"
docs_load=Load_documents(file_path)
print("Documents loaded:", len(docs_load))
# chunking ---> Recursive text splitter
chunked=Recursive_chunks(docs_load)
print("Chunks created:", len(chunked))

# vector Database ---> Typesene

Vector_DB=EmbeddingVectorStore(chunked)
print("Vector store created successfully!")

# Till now Data ingestion pipeline completed
# Now retriever pipeline will start

Question="dimension of ceramic floor tiles"
# Retirever pipeline from vector store
Retriever_pipeline=Vector_DB.as_retriever(search_type='similarity',search_kwargs={"k":4})  
# Retrieve Relevant content
Retrieved_docs=Retriever_pipeline.invoke(Question)
# convert into text, (take only page content)
Context=Format_docs(Retrieved_docs)
#prompt template
Template = Get_Prompt_template()
Formatted_template=Template.invoke({
    "Context": Context,
    "Question": "What is cement used for?"
})    
# print("----> this is context",Context)
# print("----> this is retrived docs",Retrived_docs)


# Forming LLM 
LLM=LLModel()
LLM_Response=LLM.invoke(Formatted_template)
#print(LLM_Response)

# Forming Runnables 
Template_chain=RunnableParallel({   # this will create a template for passing onto the LM
    "Question": RunnablePassthrough(),
    "Context": Retriever_pipeline | RunnableLambda(Format_docs)
})

Main_chain= Template_chain | Get_Prompt_template() | LLM | StrOutputParser()
Result=Main_chain.invoke(Question)
print("This is the final answer ",Result)





