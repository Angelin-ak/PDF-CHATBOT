  1 # 🤖 Local PDF RAG Bot                                                                     │ │
│ │  2                                                                                            │ │
│ │  3 A powerful, privacy-focused Retrieval-Augmented Generation (RAG) application that allows   │ │
│ │    you to chat with your PDF documents locally. Powered by **Ollama**, **LangChain**, and     │ │
│ │    **Streamlit**.                                                                             │ │
│ │  4                                                                                            │ │
│ │  5 ## 🌟 Features                                                                             │ │
│ │  6                                                                                            │ │
│ │  7 -   **100% Local & Private**: No data leaves your machine. Both embeddings and LLM         │ │
│ │    inference run locally via Ollama.                                                          │ │
│ │  8 -   **Multi-PDF Support**: Upload and index multiple PDF documents simultaneously.         │ │
│ │  9 -   **Interactive Chat Interface**: A clean, Streamlit-based UI for seamless communication │ │
│ │    with your documents.                                                                       │ │
│ │ 10 -   **Source Transparency**: View exactly where the information came from with page-level  │ │
│ │    citations and source highlights.                                                           │ │
│ │ 11 -   **Configurable Models**: Easily switch between different Ollama models (Llama 3,       │ │
│ │    Mistral, Phi-3, etc.) for both chat and embeddings.                                        │ │
│ │ 12 -   **Persistent Knowledge Base**: Uses ChromaDB for efficient vector storage and          │ │
│ │    retrieval.                                                                                 │ │
│ │ 13                                                                                            │ │
│ │ 14 ## 🛠️ Tech Stack                                                                           │ │
│ │ 15                                                                                            │ │
│ │ 16 -   **Frontend**: [Streamlit](https://streamlit.io/)                                       │ │
│ │ 17 -   **Orchestration**: [LangChain](https://www.langchain.com/)                             │ │
│ │ 18 -   **Vector Database**: [ChromaDB](https://www.trychroma.com/)                            │ │
│ │ 19 -   **Local LLMs**: [Ollama](https://ollama.com/)                                          │ │
│ │ 20 -   **PDF Processing**: [PyPDF](https://pypi.org/project/pypdf/)                           │ │
│ │ 21                                                                                            │ │
│ │ 22 ## 🚀 Getting Started                                                                      │ │
│ │ 23                                                                                            │ │
│ │ 24 ### Prerequisites                                                                          │ │
│ │ 25                                                                                            │ │
│ │ 26 1.  **Install Ollama**: Download and install from [ollama.com](https://ollama.com/).       │ │
│ │ 27 2.  **Pull Required Models**:                                                              │ │
│ │ 28     ```bash                                                                                │ │
│ │ 29     ollama pull llama3                                                                     │ │
│ │ 30     ollama pull nomic-embed-text                                                           │ │
│ │ 31     ```                                                                                    │ │
│ │ 32                                                                                            │ │
│ │ 33 ### Installation                                                                           │ │
│ │ 34                                                                                            │ │
│ │ 35 1.  **Clone the repository**:                                                              │ │
│ │ 36     ```bash                                                                                │ │
│ │ 37     git clone <repository-url>                                                             │ │
│ │ 38     cd <project-folder>                                                                    │ │
│ │ 39     ```                                                                                    │ │
│ │ 40                                                                                            │ │
│ │ 41 2.  **Set up a virtual environment** (recommended):                                        │ │
│ │ 42     ```bash                                                                                │ │
│ │ 43     python -m venv venv                                                                    │ │
│ │ 44     .\venv\Scripts\activate  # Windows                                                     │ │
│ │ 45     source venv/bin/activate # Linux/macOS                                                 │ │
│ │ 46     ```                                                                                    │ │
│ │ 47                                                                                            │ │
│ │ 48 3.  **Install dependencies**:                                                              │ │
│ │ 49     ```bash                                                                                │ │
│ │ 50     pip install -r requirement.txt                                                         │ │
│ │ 51     ```                                                                                    │ │
│ │ 52                                                                                            │ │
│ │ 53 ### Running the App                                                                        │ │
│ │ 54                                                                                            │ │
│ │ 55 Start the Streamlit server:                                                                │ │
│ │ 56 ```bash                                                                                    │ │
│ │ 57 streamlit run app.py                                                                       │ │
│ │ 58 ```                                                                                        │ │
│ │ 59                                                                                            │ │
│ │ 60 ## 📖 How to Use                                                                           │ │
│ │ 61                                                                                            │ │
│ │ 62 1.  **Upload Documents**: Use the sidebar to upload one or more PDF files.                 │ │
│ │ 63 2.  **Process**: Click "Process Documents" to chunk the text, create embeddings, and store │ │
│ │    them in the local vector database.                                                         │ │
│ │ 64 3.  **Chat**: Once processed, ask questions about your documents in the main chat input.   │ │
│ │ 65 4.  **View Sources**: Expand the "View Sources" section under any response to see the      │ │
│ │    exact text snippets and page numbers used to generate the answer.                          │ │
│ │ 66                                                                                            │ │
│ │ 67 ## 📁 Project Structure                                                                    │ │
│ │ 68                                                                                            │ │
│ │ 69 ```text                                                                                    │ │
│ │ 70 ├── app.py              # Main Streamlit UI and application logic                          │ │
│ │ 71 ├── rag_logic.py        # LangChain RAG pipeline implementation                            │ │
│ │ 72 ├── requirement.txt     # Project dependencies                                             │ │
│ │ 73 └── chroma_db/          # Persistent vector database (generated)                           │ │
│ │ 74 ```                                                                                        │ │
│ │ 75                                                                                            │ │
│ │ 76 ## 🔒 Privacy Note                                                                         │ │
│ │ 77                                                                                            │ │
│ │ 78 This application is designed to be fully self-contained. Your documents never leave your   │ │
│ │    local machine, making it ideal for processing sensitive or confidential information.       │ │
│ │ 79                                                                                            │ │
│ │ 80 ---                                                                                        │ │
│ │ 81 *Created with ❤️ using LangChain and Ollama.* 
