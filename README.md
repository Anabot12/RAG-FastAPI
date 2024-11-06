# RAG-FastAPI

## Introduction
This project implements a lightweight FastAPI server for Retrieval-Augmented Generation (RAG). The server utilizes ChromaDB’s persistent client for ingesting and querying documents (PDF, DOC, DOCX, TXT) and leverages the `sentence-transformers/all-MiniLM-L6-v2` model for generating embeddings from the documents and queries. The server provides non-blocking API endpoints to ensure efficient concurrency handling.

The goal of this project is to upload and query documents in a seamless and efficient manner using FastAPI and ChromaDB, enabling document-based queries and retrieval of relevant content using embeddings.

## Requirements

Kindly install all the requirements from [requirements.txt](requirements.txt)


### Dependencies
- **FastAPI**: A modern, fast web framework for building APIs.
- **Uvicorn**: A fast ASGI server for serving FastAPI applications.
- **ChromaDB**: A persistent database for storing embeddings and performing document-based queries.
- **Sentence-Transformers**: A Python library for generating embeddings from text using models like `all-MiniLM-L6-v2`.


### Outputs

/upload/ 
![image](https://github.com/user-attachments/assets/28e9cb02-dcce-4d65-affb-a59c50bf74e0)

/query/
![image](https://github.com/user-attachments/assets/4f51d744-9170-4d77-b801-8abf5567b086)


