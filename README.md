# 🤖 Local PDF RAG Bot

A powerful, privacy-focused Retrieval-Augmented Generation (RAG) application that allows you to chat with your PDF documents locally. Powered by **Ollama**, **LangChain**, and **Streamlit**.

## 🌟 Features

-   **100% Local & Private**: No data leaves your machine. Both embeddings and LLM inference run locally via Ollama.
-   **Multi-PDF Support**: Upload and index multiple PDF documents simultaneously.
-   **Interactive Chat Interface**: A clean, Streamlit-based UI for seamless communication with your documents.
-   **Source Transparency**: View exactly where the information came from with page-level citations and source highlights.
-   **Configurable Models**: Easily switch between different Ollama models (Llama 3, Mistral, Phi-3, etc.) for both chat and embeddings.
-   **Persistent Knowledge Base**: Uses ChromaDB for efficient vector storage and retrieval.

## 🛠️ Tech Stack

-   **Frontend**: [Streamlit](https://streamlit.io/)
-   **Orchestration**: [LangChain](https://www.langchain.com/)
-   **Vector Database**: [ChromaDB](https://www.trychroma.com/)
-   **Local LLMs**: [Ollama](https://ollama.com/)
-   **PDF Processing**: [PyPDF](https://pypi.org/project/pypdf/)

## 🚀 Getting Started

### Prerequisites

1.  **Install Ollama**: Download and install from [ollama.com](https://ollama.com/).
2.  **Pull Required Models**:
    ```bash
    ollama pull llama3
    ollama pull nomic-embed-text
    ```

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <project-folder>
    ```

2.  **Set up a virtual environment** (recommended):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # Linux/macOS
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirement.txt
    ```

### Running the App

Start the Streamlit server:
```bash
streamlit run app.py
```

## 📖 How to Use

1.  **Upload Documents**: Use the sidebar to upload one or more PDF files.
2.  **Process**: Click "Process Documents" to chunk the text, create embeddings, and store them in the local vector database.
3.  **Chat**: Once processed, ask questions about your documents in the main chat input.
4.  **View Sources**: Expand the "View Sources" section under any response to see the exact text snippets and page numbers used to generate the answer.

## 📁 Project Structure

```text
├── app.py              # Main Streamlit UI and application logic
├── rag_logic.py        # LangChain RAG pipeline implementation
├── requirement.txt     # Project dependencies
└── chroma_db/          # Persistent vector database (generated)
```

## 🔒 Privacy Note

This application is designed to be fully self-contained. Your documents never leave your local machine, making it ideal for processing sensitive or confidential information.

---
*Created with ❤️ using LangChain and Ollama.*
