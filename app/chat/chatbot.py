import streamlit as st

from app.llm.gemini import llm


class ChatBot:

    @staticmethod
    def chat():

        st.subheader("💬 AI Assistant")

        question = st.text_input(
            "Ask anything..."
        )

        if question:

            with st.spinner("Thinking..."):

                answer = llm.invoke(question)

            st.success("Done")

            st.write(answer.content)