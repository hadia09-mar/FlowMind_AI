import streamlit as st

from app.knowledge.loader import DocumentLoader
from app.knowledge.splitter import DocumentSplitter
from app.knowledge.vectorstore import VectorStore
from app.knowledge.retriever import Retriever
from app.knowledge.qa import DocumentQA
from app.ui.components import footer

def docs_page():

    st.title("📄 FlowMind Docs")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        file_path = f"data/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Document Uploaded Successfully")

        docs = DocumentLoader.load_document(file_path)

        chunks = DocumentSplitter.split(docs)

        db = VectorStore.create(chunks)

        question = st.text_input("Ask a Question")

        if question:

            results = Retriever.search(db, question)

            answer = DocumentQA.answer(
                question,
                results
            )

            st.subheader("🤖 AI Answer")

            st.write(answer)
    footer()