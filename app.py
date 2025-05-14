import streamlit as st
from utils import extract_text_from_pdf, chunk_text
from rag_chain import embed_and_store_chunks, retrieve_relevant_chunks, generate_answer

st.title("📄 AI Chat with Your PDF (RAG + FAISS + Cohere)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Extracting and chunking text..."):
        text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(text)
        embed_and_store_chunks(chunks)
    st.success("PDF processed and stored in FAISS!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask a question about your PDF:")
if query:
    with st.spinner("Retrieving context and generating answer..."):
        relevant_chunks = retrieve_relevant_chunks(query)
        answer = generate_answer(query, relevant_chunks)
        st.session_state.chat_history.append((query, answer))

for q, a in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**AI:** {a}")
