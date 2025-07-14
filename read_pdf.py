from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def load_documents():
  document_loader = PyPDFDirectoryLoader("data")
  documents = document_loader.load()
  return documents

def split_documents(documents: list[Document]):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800, 
    chunk_overlap=80, 
    length_function=len, 
    is_separator_regex=False
  )
  
  return text_splitter.split_documents(documents)


def get_embedding_function():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
  

db = Chroma(
  persist_directory="database", embedding_function=get_embedding_function()
)


def add_to_chroma(chunks: list[Document]):
  last_page_id = None
  current_chunk_index = 0
  
  new_chunks = []
  new_chunk_ids = []
  
  for chunk  in chunks:
    source = chunk.metadata.get("source")
    page = chunk.metadata.get("page")
    current_page_id = f"{source}:{page}"
    if(current_page_id == last_page_id):
      current_chunk_index += 1
    else:
      current_chunk_index = 0
    chunk_id = f"{current_page_id}:{current_chunk_index}"
    last_page_id = current_page_id
    new_chunk_ids.append(chunk_id)
    chunk.metadata["id"] = chunk_id
    new_chunks.append(chunk)

  existing_items = db.get(include=[])
  existing_ids = set(existing_items["ids"])
  
  print(f"Number of documents in DB: {len(new_chunk_ids)}")
  # for chunk in chunk_id

  db.add_documents(new_chunks,ids=new_chunk_ids)
  # db.persist()
  
documents = load_documents()
chunks = split_documents(documents)
add_to_chroma(chunks)

