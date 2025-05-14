import faiss
import numpy as np
import cohere
import os
from dotenv import load_dotenv
import pickle

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

# In-memory FAISS index + document mapping
index = None
document_chunks = []

def embed_and_store_chunks(chunks):
    global index, document_chunks
    document_chunks = chunks
    embeddings = co.embed(texts=chunks, model="embed-english-v3.0", input_type="search_document").embeddings
    vectors = np.array(embeddings).astype("float32")
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

def retrieve_relevant_chunks(query, top_k=5):
    if index is None:
        return []
    query_vec = co.embed(texts=[query], model="embed-english-v3.0", input_type="search_document").embeddings[0]
    query_vec = np.array(query_vec).astype("float32").reshape(1, -1)
    D, I = index.search(query_vec, top_k)
    return [document_chunks[i] for i in I[0]]

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""
You are an assistant helping answer questions based on a PDF.
Here is the context:

{context}

Question: {query}
Answer:"""

    response = co.generate(prompt=prompt, model="command", max_tokens=300)
    return response.generations[0].text.strip()
