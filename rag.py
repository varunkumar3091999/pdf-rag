from flask import jsonify
from langchain_chroma import Chroma
from read_pdf import get_embedding_function
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import json



model = OllamaLLM(model='mistral')

db = Chroma(
  persist_directory="database", embedding_function=get_embedding_function()
)


def query_rag(query_text):
  prompt_text = """
  Answer the question only based on the following context:{context}
  
  Answer the question based on the above context: {query_text}
  """

  results = db.similarity_search_with_score(query_text, k=5)
  
  context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
  prompt_template = ChatPromptTemplate.from_template(prompt_text)
  prompt = prompt_template.format(context=context_text, query_text=query_text)
    
  response_text = model.invoke(prompt)

  response_data = {
    "answer": response_text,
    "matches": [{
        "text": doc.page_content,
        "metadata": doc.metadata,
        "score": score
    } for doc, score in results]
  }
  
  return json.dumps(response_data, indent=2)

# while True:
#   query = input("💬 Ask me something (or type 'exit' to quit): ")
#   if query.lower() == "exit":
#       break
#   print("Loading...")
#   response = query_rag(query)
#   print(response)