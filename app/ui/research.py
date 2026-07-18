import streamlit as st

from app.agents.research.research_agent import ResearchAgent
from app.ui.components import footer

def research_page():

    st.title("🔍 FlowMind Research")

    topic = st.text_input("Research Topic")

    if st.button("Generate Report"):

        report = ResearchAgent.research(topic)

        st.markdown(report)

    footer()