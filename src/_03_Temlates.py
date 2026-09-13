from langchain_core.prompts import PromptTemplate

# prompt Template
def Get_Prompt_template():
    
    Template =PromptTemplate(template="""
    [SYSTEM]
    You are a helpful, knowledgeable, and concise material guide agent assistant.
    - Answer directly and stay on topic.
    - Cite any external information you use (e.g., “According to …”).
    - If you don’t know the answer, say so honestly.
    {Context}
    the question is : {Question}""",
                    
    input_variables={"Context","Question"}

                            )
    return Template