# 📄 PDF-RAG (Retrieval-Augmented Generation for PDF)

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that allows you to parse a PDF file, split the content into meaningful chunks, generate embeddings, store them in a vector database (ChromaDB), and retrieve the most relevant chunks to answer user queries.

---

## 🚀 Features

- Parse and clean text from PDF files
- Split text into overlapping chunks using `RecursiveCharacterTextSplitter`
- Generate embeddings using `sentence-transformers/all-MiniLM-L6-v2`
- Store embeddings in Chroma vector database
- Retrieve top relevant chunks for user questions
- Supports local LLMs (Ollama), and can be easily extended to online models

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-rag.git
cd pdf-rag
```

### 2. Create and activate a virtual environment

```bash
python -m venv environment
source environment/bin/activate  # macOS/Linux
# OR
environment\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### 1️⃣ Download Ollama

- Download Ollama: [https://ollama.com/download](https://ollama.com/download)

### 2️⃣ Pull the Mistral model

```bash
ollama pull mistral
```

### 3️⃣ Start the Ollama server

```bash
ollama serve
```

### 4️⃣ Parse PDF

```bash
python read_pdf.py
```

- Parses the PDF, cleans text, splits it into chunks, generates embeddings, and adds them to ChromaDB.

### 5️⃣ Start RAG server

```bash
python rag.py
```

- Prompts you to enter a question in the terminal.
- Returns top matching chunks from the PDF content.

---

## ⚡ Notes

- Using local Ollama models can slow down your machine; you can switch to online APIs (e.g., OpenAI, Anthropic) if needed.
- Update the PDF file path in the script as needed.

---

## ✨ Future Improvements

- Add a web-based UI (Streamlit or Gradio) to upload PDFs and chat with them
- Support multiple PDFs and metadata filtering
- Show sources and references for retrieved answers

---

## 🧑‍💻 Author

Varun Kumar Saravanan
