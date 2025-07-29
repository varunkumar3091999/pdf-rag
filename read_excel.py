import pandas as pd
import sqlite3
import sqlite3
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def read_csv(filepath):
  try: 
    df = pd.read_csv(filepath)
    print(df)
    return df
  except Exception as e:
    print(f"Error reading Excel file: {e}")
    return None

def read_excel(filepath, sheet_name=0):
  try: 
    df = pd.read_excel(filepath)
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    df = df.dropna(how='all')  # Drop rows where all elements are NaN
    # Further custom cleaning here
    add_to_db(df, filepath)
    return df
  except Exception as e:
    print(f"Error reading Excel file: {e}")
    return None
  
def add_to_db(df, filepath):
  conn = sqlite3.connect("excel_data.db")
  df.to_sql('car_price_dataset', conn, if_exists="replace",index=False)
  

def fetch_rows_from_sqlite(db_path, table_name):
   conn = sqlite3.connect(db_path)
   cursor = conn.cursor()
   cursor.execute(f"select * from {table_name}")
   columns = [desc[0] for desc in cursor.description] 
   rows = cursor.fetchall()
   conn.close()
   
   documents = []
   for row in rows:
      text = "\n".join([f"{col}:{val}" for col, val in zip(columns, row)])
      documents.append(text)      
   return documents


def convert_to_document(text_chunks):
   return [Document(page_content=chunk) for chunk in text_chunks]

def get_embedding_function():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings
 
db = Chroma(
  persist_directory="database", embedding_function=get_embedding_function()
)

def embed_and_store(documents):
   embeddings = get_embedding_function()
   vector_db = Chroma.from_documents(documents, embeddings, persist_directory="chroma_db_excel")
   print("Data stored to Chroma")
   return vector_db

read_excel("./excel/car_price_dataset.xlsx")
text = fetch_rows_from_sqlite("excel_data.db","car_price_dataset")
print(text, "text")
docs = convert_to_document(text)
print(docs, "docs")
embed_and_store(docs)
