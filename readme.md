# RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot built using **LangChain**, **ChromaDB**, and **Mistral AI**.

## Prerequisites

Before running the project, make sure you have:

* Python installed
* All required dependencies installed
* Your API keys configured in the `.env` file

---

## Project Workflow

### Step 1: Add Your Documents

Place the document(s) you want to query inside the `files/` directory.

Example:

```text
files/
├── sample.pdf
├── notes.txt
└── document.pdf
```

---

### Step 2: Create the Vector Database

Run the `create_db.py` file.

```bash
python create_db.py
```

This script will:

1. Load the document(s).
2. Split the document into chunks.
3. Generate embeddings for each chunk.
4. Store the chunks and embeddings in the Chroma vector database.

> **Important:** Run this script whenever you add or replace documents in the `files/` folder.

---

### Step 3: Start the Chatbot

Run:

```bash
python main.py
```

Once the chatbot starts, you can begin asking questions about the uploaded document.

Example:

```text
----- Welcome -----

You: What is the role?

AI:
<Generated response>
```

To exit the application:

```text
You: 0
```

---

# How the Chatbot Works

The chatbot follows a Retrieval-Augmented Generation (RAG) pipeline:

1. You ask a question.
2. The question is expanded using a **MultiQuery Retriever**.
3. The retriever searches the Chroma vector database for the most relevant document chunks.
4. The retrieved context is passed to the Mistral LLM.
5. The LLM generates an answer based only on the retrieved context.

---

# Current Limitations

This project is currently a basic implementation of a RAG chatbot.

The following features have **not** been implemented yet:

* Chat history (conversation memory)
* Runnable chains / LCEL pipeline
* Streaming responses
* Source citation in responses
* Multiple document management
* Document upload through a user interface
* Metadata filtering

Each question is treated as a completely new query, so the chatbot does **not** remember previous conversations.

---

# Project Structure

```text
.
├── EmbeddingModel/
├── document_loader/
├── files/
├── text_splitter/
├── vector_store/
├── create_db.py
├── main.py
├── .env
└── README.md
```

---

# Notes

* Upload your documents to the `files/` folder **before** running `create_db.py`.
* If you change or add documents, run `create_db.py` again to update the vector database.
* `main.py` is only responsible for querying the existing vector database.
* The chatbot answers only from the retrieved document context. If the answer is not found in the uploaded documents, it will indicate that the information is unavailable.

---

# Future Improvements

Planned enhancements include:

* Chat history and conversational memory
* Runnable chains (LCEL)
* Better prompt engineering
* Support for multiple uploaded documents
* Web-based user interface
* Document source references
* Streaming responses
* Advanced retrievers (Parent Document, Contextual Compression, Ensemble Retriever, etc.)
