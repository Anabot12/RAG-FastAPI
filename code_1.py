from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import chromadb
from sentence_transformers import SentenceTransformer
import os
from utils import process_pdf, process_docx, process_txt, ingest_document

app = FastAPI()


client = chromadb.Client()
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

collection_name = "documents"
collection = client.create_collection(collection_name)

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    """
    Uploads a document (PDF, DOCX, TXT) and ingests it into ChromaDB.
    """
    file_extension = file.filename.split('.')[-1].lower()
    file_path = f"temp_files/{file.filename}"

    # Saving the uploaded file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Process the document
    if file_extension == 'pdf':
        text = process_pdf(file_path)
    elif file_extension == 'docx':
        text = process_docx(file_path)
    elif file_extension == 'txt':
        text = process_txt(file_path)
    else:
        return JSONResponse(content={"error": "Unsupported file type"}, status_code=400)

    ingest_document(collection, text, file.filename)
    return {"message": f"{file.filename} uploaded and ingested successfully"}

from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str

@app.post("/query/")
async def query_document(request: QueryRequest):
    query = request.query
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=5)


    if results['documents']:
        relevant_document = results['documents'][0]
        return {"result": relevant_document}
    else:
        return {"message": "No relevant results found."}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
