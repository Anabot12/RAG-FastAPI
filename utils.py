import pdfminer
import docx
import os
from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def process_pdf(file_path: str) -> str:
    from pdfminer.high_level import extract_text
    text = extract_text(file_path)
    return text

def process_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def process_txt(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def ingest_document(collection, text: str, document_name: str):
    chunks = text.split("\n\n")
    embeddings = model.encode(chunks)
    document_ids = [f"{document_name}_chunk_{i}" for i in range(len(chunks))]
    metadata = [{"section": f"chunk_{i}"} for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        metadatas=metadata,
        embeddings=embeddings,
        ids=document_ids 
    )

