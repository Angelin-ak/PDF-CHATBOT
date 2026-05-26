import streamlit as st
import os
import shutil
from rag_logic import load_pdfs, get_vector_store, get_rag_chain

# Page configuration
st.set_page_config(
    page_title="Local PDF RAG Bot", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stChatFloatingInputContainer {
        padding-bottom: 2rem;
    }
    .main {
        padding-top: 2rem;
    }
    .st-emotion-cache-1c7n2ka {
        max-width: 800px;
        margin: 0 auto;
    }
</style>
""", unsafe_allow_html=True)

# Constants
CHROMA_PATH = "./chroma_db"

def delete_db(path):
    """Safely delete the Chroma database directory handling Windows file locks."""
    if os.path.exists(path):
        import gc
        import time
        # 1. Release references
        st.session_state.rag_chain = None
        gc.collect()
        time.sleep(0.5) # Give OS a moment to release locks
        
        # 2. Try to delete with retries
        for i in range(3):
            try:
                shutil.rmtree(path)
                return True
            except Exception:
                time.sleep(1)
                gc.collect()
    return False

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

# Sidebar for configuration and file management
with st.sidebar:
    st.title("🤖 Chatbot Control")
    st.divider()
    
    # 1. File Uploader
    st.subheader("📚 Knowledge Base")
    uploaded_files = st.file_uploader(
        "Upload PDF documents", 
        type="pdf", 
        accept_multiple_files=True,
        help="Select one or more PDF files to index."
    )
    
    # 2. Process Button
    process_button = st.button("🚀 Process Documents", use_container_width=True)
    
    if st.session_state.processed_files:
        st.info(f"Files in index: {', '.join(st.session_state.processed_files)}")
    
    st.divider()
    
    # 3. Settings
    with st.expander("⚙️ Settings"):
        llm_model = st.selectbox(
            "LLM Model", 
            ["llama3", "mistral", "phi3"], 
            index=0,
            help="Choose the model for generating responses."
        )
        embedding_model = st.selectbox(
            "Embedding Model", 
            ["nomic-embed-text"], 
            index=0,
            help="Choose the model for creating vector embeddings."
        )
    
    # 4. Clear Database/Chat Button
    if st.button("🗑️ Clear All", use_container_width=True, type="secondary"):
        delete_db(CHROMA_PATH)
        st.session_state.messages = []
        st.session_state.rag_chain = None
        st.session_state.processed_files = []
        st.success("Database and chat history cleared!")
        st.rerun()

# Main UI Area
st.title("Local PDF RAG Bot")
st.caption("Chat with your documents locally using Ollama.")

# Handle processing
if process_button:
    if uploaded_files:
        with st.spinner("Indexing documents... this may take a moment."):
            try:
                # 1. Safely delete old DB
                delete_db(CHROMA_PATH)
                
                # 2. Load and index
                documents = load_pdfs(uploaded_files)
                
                if not documents:
                    st.error("Could not extract text from the uploaded PDFs.")
                else:
                    vector_store = get_vector_store(documents, embedding_model, CHROMA_PATH)
                    st.session_state.rag_chain = get_rag_chain(vector_store, llm_model)
                    st.session_state.processed_files = [f.name for f in uploaded_files]
                    st.success(f"Successfully processed {len(uploaded_files)} files!")
                    st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("💡 Ensure Ollama is running and you have run `ollama pull " + embedding_model + "` and `ollama pull " + llm_model + "`.")
    else:
        st.warning("Please upload at least one PDF file.")

# Display chat messages
if not st.session_state.messages:
    if not st.session_state.processed_files:
        st.info("👈 Start by uploading and processing some PDF documents in the sidebar.")
    else:
        st.success("Knowledge base ready! Ask me anything about your documents below.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message:
            with st.expander("🔍 View Sources"):
                for source in message["sources"]:
                    st.write(f"- {source}")

# Chat input
if user_input := st.chat_input("Ask a question about your documents:"):
    if st.session_state.rag_chain is None:
        st.warning("Please upload and process documents first.")
    else:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate and display response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    result = st.session_state.rag_chain.invoke(user_input)
                    answer = result["answer"]
                    sources = [f"{doc.metadata.get('source')} (Page {doc.metadata.get('page')})" for doc in result["context"]]
                    unique_sources = sorted(list(set(sources)))
                    
                    st.markdown(answer)
                    with st.expander("🔍 View Sources"):
                        for source in unique_sources:
                            st.write(f"- {source}")
                    
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": answer,
                        "sources": unique_sources
                    })
                except Exception as e:
                    st.error(f"Error during inference: {e}")
                    st.info("Check if the selected Ollama model is available.")
