
# RAG Learning Project

A Retrieval-Augmented Generation (RAG) project built from scratch to understand the complete data pipeline 

## Features

* Load data from multiple sources

  * Text Files (.txt)
  * PDF Files (.pdf)
  * Excel Files (.xlsx)

* Convert data into LangChain Document objects

* Multiple Chunking Strategies

  * Recursive Character Text Splitter
  * SpaCy Text Splitter
  * NLTK Text Splitter

* Embedding Generation

  * Sentence Transformers
  * all-MiniLM-L6-v2 model

* Vector Storage

  * ChromaDB Persistent Client
  * Metadata and document storage

* Retrieval Pipeline

  * User query input
  * Query embedding generation
  * Similarity search against multiple collections
  * Top-K relevant chunk retrieval

---

## Project Structure

```text
RAGLearning/
│
├── Data/
│   ├── textfiles/
│   ├── pdf_files/
│   └── excelfiles/
│
├── codes/
│   ├── data_loading/
│   │   ├── textdata.py
│   │   ├── pdfdata.py
│   │   └── exceldata.py
│   │
│   ├── data_chunkinng/
│   │   └── textsplitter.py
│   │
│   ├── data_embeddings/
│   │   └── embeddings.py
│   │
│   ├── embedding_storage/
│   │   └── database.py
│   │
│   └── user_query/
│       └── dataentry.py
│
└── notebook/
```

---

## Workflow


Documents
    ↓
Load Data
    ↓
Convert to Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB Storage
    ↓
User Query
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Chunks Retrieved


---

## Technologies Used

* Python
* LangChain
* ChromaDB
* Sentence Transformers
* Hugging Face
* SpaCy
* NLTK
* Pandas
* PyMuPDF

---

## Learning Goals

This project focuses on understanding:

* Document Loading
* Text Chunking Strategies
* Embedding Models
* Vector Databases
* Similarity Search
* Retrieval Pipelines
* RAG Architecture

Instead of using a single framework abstraction, every stage is implemented separately to understand the internals of Retrieval-Augmented Generation systems.

---

## Future Improvements

* Semantic Chunking
* Hybrid Search



