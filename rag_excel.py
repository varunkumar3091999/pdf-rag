from langchain_ollama import OllamaLLM
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

db_path = "sqlite:///excel_data.db"
print(1)

db = SQLDatabase.from_uri(db_path)
print(2)

llm = OllamaLLM(model='mistral')
print(3)

sql_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
print(4)

question = "How many cars have fuel type petrol?"
print(5)

prompt = "Convert the natural language question: 'How many cars have fuel type petrol?' into a SQL query on a table named car_price_dataset with a 'fuel_type' column."
print(6)

# answer = sql_chain.invoke(prompt)

response = llm.invoke(prompt)
print(response)

print("Answer:", response)

