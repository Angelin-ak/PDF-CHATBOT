
import os
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM as Ollama
from langchain_core.documents import Document

def load_pdfs(pdf_files):
    """Extracts text from a list of PDF files and returns a list of Document objects."""
    documents = []
    for pdf_file in pdf_files:
        # pdf_file can be a path or a Streamlit UploadedFile (which is file-like)
        reader = PdfReader(pdf_file)
        # Use the name attribute if it's an UploadedFile, otherwise use the path
        source_name = getattr(pdf_file, "name", "Unknown Source")
        
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                documents.append(Document(
                    page_content=text,
                    metadata={"source": source_name, "page": i + 1}
                ))
    return documents

def get_vector_store(documents, embedding_model="nomic-embed-text", persist_directory="./chroma_db"):
    """Splits documents and creates a persistent Chroma vector store."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    splits = text_splitter.split_documents(documents)
    
    embeddings_engine = OllamaEmbeddings(model=embedding_model)
    
    # Create the vector store and persist it
    vector_store = Chroma.from_documents(
        documents=splits, 
        embedding=embeddings_engine,
        persist_directory=persist_directory
    )
    return vector_store

def get_rag_chain(vector_store, llm_model="llama3"):
    """Creates the RAG chain that returns both the answer and the source documents."""
    llm = Ollama(model=llm_model)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    def format_docs(docs):
        return "\n\n".join(f"--- Source: {doc.metadata.get('source')} (Page {doc.metadata.get('page')}) ---\n{doc.page_content}" for doc in docs)

    system_prompt = (
        "You are a helpful assistant. Use the following pieces of retrieved context "
        "from the PDF documents to answer the question. If you don't know the answer, "
        "say that you don't know. Keep the answer concise.\n\n"
        "Context:\n{context}"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # We use RunnableParallel to return both the answer and the sources
    rag_chain_from_docs = (
        RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
        | prompt
        | llm
        | StrOutputParser()
    )

    rag_chain = RunnableParallel(
        {"context": retriever, "input": RunnablePassthrough()}
    ).assign(answer=rag_chain_from_docs)
    
    return rag_chain
