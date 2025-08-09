import pandas as pd
import ollama
import chromadb
from langchain.schema.document import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
# from langchain_community.embeddings import SentenceTransformerEmbeddings





excel_file_path = 'excel/car_price_dataset.xlsx'

df = pd.read_excel(excel_file_path)


print(df.iterrows())

def row_to_sentence():
    sentences = []

    for idx, row in df.iterrows():
        print(idx, "index")
        sentence = (
        f"{row['Year']} {row['Brand']} {row['Model']} with a {row['Engine_Size']}L "
        f"{row['Fuel_Type']} engine, {row['Transmission']} transmission, "
        f"{row['Doors']} doors, {row['Owner_Count']} previous owners, "
        f"total distance driven {row['Total Distance']} km, "
        f"priced at {row['Price']}."
        )
        sentences.append(sentence)
        
    return sentences


def split_documents(documents: list[Document]):
  text_splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0, 
    # saperators=['\n']
  )
  
  return text_splitter.split_documents(documents)


def get_embedding_function():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
  

db = Chroma(
  persist_directory="excel_database", embedding_function=get_embedding_function()
)




def add_to_chroma(chunks: list[Document]):
  print("Adding chunks")
  
  batch_size = 1000
  
  
  for i in range(0,len(chunks), batch_size):
    batch_chunks = chunks[i : i + batch_size]
    batch_ids = [f"chunk_{j}" for j in range(i, min(i + batch_size, len(chunks)))]
    print(f"Adding chunks from ids {batch_ids[0]} to {batch_ids[-1]}")
    db.add_documents(batch_chunks, ids=batch_ids)
  
    print("Data added to chroma")



sentenses = row_to_sentence()
docs = [Document(page_content=sentence, metadata={"chunk_id":ind}) for ind,sentence in enumerate(sentenses)]
chunks = split_documents(docs)
add_to_chroma(chunks)

