import streamlit as st

from app.ui.components import footer
def about_page():

    st.title("ℹ️ About FlowMind AI")

    st.markdown("""
# FlowMind AI

FlowMind AI is an Enterprise AI Automation Platform built using modern AI technologies.

## Features

✅ AI Resume Analyzer

✅ RAG Document QA

✅ AI Email Generator

✅ Automation Center

✅ Analytics Dashboard

✅ Activity Logging

✅ SQLite Database

✅ LangGraph

✅ Google Gemini

## Tech Stack

- Python
- Streamlit
- LangChain
- LangGraph
- ChromaDB
- SQLite
- Google Gemini
- Plotly

---

Developed as an Enterprise AI Automation Portfolio Project.
""")
    footer()