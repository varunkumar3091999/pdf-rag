import pandas as pd
import ollama
import chromadb
from langchain.schema.document import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma




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
  persist_directory="database", embedding_function=get_embedding_function()
)




# def add_to_chroma(chunks: list[Document]):
#   last_page_id = None
#   current_chunk_index = 0
  
#   new_chunks = []
#   new_chunk_ids = []
  
#   for chunk  in chunks:
#     source = chunk.metadata.get("source")
#     page = chunk.metadata.get("page")
#     current_page_id = f"{source}:{page}"
#     if(current_page_id == last_page_id):
#       current_chunk_index += 1
#     else:
#       current_chunk_index = 0
#     chunk_id = f"{current_page_id}:{current_chunk_index}"
#     last_page_id = current_page_id
#     new_chunk_ids.append(chunk_id)
#     chunk.metadata["id"] = chunk_id
#     new_chunks.append(chunk)

#   existing_items = db.get(include=[])
  
#   print(f"Number of documents in DB: {len(new_chunk_ids)}")
#   # for chunk in chunk_id

#   db.add_documents(new_chunks,ids=new_chunk_ids)
#   return f"Number of documents in DB: {len(new_chunk_ids)}"
#   # db.persist()
  
  
  
sentenses = row_to_sentence()
docs = [Document(page_content=sentence, ) for ind,sentence in sentenses]

chunks = split_documents(docs)


print(chunks, "chunksc")
# add_to_chroma(chunks)

