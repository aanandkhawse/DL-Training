
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

@st.cache_resource
def load_vectorstore():
    # 1. Load document
    loader = TextLoader("CPP.txt", encoding="utf-8")
    documents = loader.load()

    # 2. Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    final_documents = text_splitter.split_documents(documents)

    # 3. Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 4. Create FAISS vector store
    db = FAISS.from_documents(final_documents, embeddings)

    # 5. Return the vector store
    return db


# Load vector store
db = load_vectorstore()

# User input
query = st.text_input("Ask a question about C++:")

if query:
    docs = db.similarity_search(query, k=3)

    st.subheader("Retrieved Context:")

    for i, doc in enumerate(docs, start=1):
        st.write(f"**Document {i}:**")
        st.write(doc.page_content)
        st.write("---")
