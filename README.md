# RAG PDF Chat with FAISS & Cohere

This is an AI-powered **RAG (Retrieval-Augmented Generation)** system that allows users to upload a PDF, split the content into chunks, generate embeddings using **Cohere**, and then use **FAISS** for fast retrieval of relevant text. Users can ask questions about the content of the PDF, and the AI will generate answers based on the retrieved text.

## Features

- Upload PDF files.
- Automatically extract text from the PDF.
- Split the text into manageable chunks.
- Use **Cohere's embeddings API** to generate vector representations of the text.
- Store the vectors using **FAISS** for fast similarity search.
- Ask questions about the PDF, and get responses based on the relevant text from the document.
- **Streamlit** interface for easy interaction.

## Requirements

- Python 3.7+
- Install dependencies using the `requirements.txt` file.

### Dependencies:

- **streamlit**: Web UI for interacting with the PDF.
- **PyPDF2**: For extracting text from PDF files.
- **cohere**: For generating text embeddings and model-based answers.
- **faiss-cpu**: For vector similarity search.
- **python-dotenv**: For securely storing API keys.

## Setup & Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/rag_pdf_faiss.git
   cd rag_pdf_faiss
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate  
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your Cohere API Key in a .env file:
    ```bash
    COHERE_API_KEY=your_cohere_api_key_here
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```