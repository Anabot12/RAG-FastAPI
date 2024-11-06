# RAG-FastAPI

## Introduction
This project implements a lightweight FastAPI server for Retrieval-Augmented Generation (RAG). The server utilizes ChromaDB’s persistent client for ingesting and querying documents (PDF, DOC, DOCX, TXT) and leverages the `sentence-transformers/all-MiniLM-L6-v2` model for generating embeddings from the documents and queries. The server provides non-blocking API endpoints to ensure efficient concurrency handling.

The goal of this project is to upload and query documents in a seamless and efficient manner using FastAPI and ChromaDB, enabling document-based queries and retrieval of relevant content using embeddings.

## Requirements

Kindly install all the requirements from [requirements.txt](path/to/your/file)


### Dependencies
- **FastAPI**: A modern, fast web framework for building APIs.
- **Uvicorn**: A fast ASGI server for serving FastAPI applications.
- **ChromaDB**: A persistent database for storing embeddings and performing document-based queries.
- **Sentence-Transformers**: A Python library for generating embeddings from text using models like `all-MiniLM-L6-v2`.

### Install Dependencies
To get started, clone the repository and install the required Python packages.

