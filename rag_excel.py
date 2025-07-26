from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

model = OllamaLLM(model='mistral')

def llm_generate_sql(user_question, schema_description):
   prompt = f"""You are an expert that writes correct SQL SELECT queries.
    Schema:
    {schema_description}
    Convert this question to an SQL SELECT statement:
    Question: {user_question}
    SQL:"""
    
    # response_text = model.invoke(prompt)
