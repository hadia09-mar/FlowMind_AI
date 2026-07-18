import streamlit as st
from app.ui.components import footer

def settings_page():

    st.title("⚙️ Settings")

    st.write("FlowMind AI Settings")

    st.toggle("Dark Mode")

    st.toggle("Enable Notifications")

    st.toggle("Auto Save")

    st.success("Settings Loaded")
    footer()