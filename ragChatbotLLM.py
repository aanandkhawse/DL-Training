import os
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

st.title("C++ RAG Assistant using LLM")

@st.cache_resource
def load_vectorstore():
    loader = TextLoader("CPP.txt", encoding="utf-8")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    final_documents = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(final_documents, embeddings)
    return db

db = load_vectorstore()
llm = OllamaLLM(model="gemma2:2b")

user_qustion = st.text_input("Ask a question about C++:")

if user_qustion:
    with st.spinner("Thinking..."):
        docs = db.similarity_search(user_qustion, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""Answer using ONLY the document context below.

        context:
        {context}
        question:
        {user_qustion}
        Answer:
        """

        response = llm.invoke(prompt)
        st.subheader("Answer:")
        st.write(response)
