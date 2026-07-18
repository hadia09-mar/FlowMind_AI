import streamlit as st

from app.auth.auth import create_user_table
from app.auth.login import login_page
from app.auth.session import is_logged_in, initialize

from app.ui.dashboard import dashboard
from app.ui.hr import hr_page
from app.ui.docs import docs_page
from app.ui.research import research_page
from app.ui.reports import reports_page
from app.ui.mail import mail_page
from app.ui.automation import automation_page
from app.ui.analytics import analytics_page
from app.chat.chatbot import ChatBot
from app.ui.settings import settings_page
from app.ui.about import about_page

from app.auth.auth import (
    create_user_table,
    create_documents_table,
    create_hr_table,
    create_research_table,
    create_activity_table,
    create_automation_table,
)


# -----------------------------
# Streamlit Config
# -----------------------------

st.set_page_config(
    page_title="FlowMind AI",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Database
# -----------------------------

create_user_table()
create_documents_table()
create_hr_table()
create_research_table()
create_activity_table()
create_automation_table()
# -----------------------------
# Session
# -----------------------------

initialize()

# -----------------------------
# Login Gate
# -----------------------------

if not is_logged_in():

    login_page()

    st.stop()

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🤖 FlowMind AI")
st.sidebar.image(
    "assets/logo.png",
    width=140
)
st.sidebar.caption("Enterprise AI Automation Platform")
st.sidebar.divider()

# Logout Button

if st.sidebar.button("🚪 Logout"):

    st.session_state.clear()

    initialize()

    st.rerun()

# -----------------------------
# Navigation
# -----------------------------

menu = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",

        "HR",

        "Docs",

        "Research",

        "Reports",

        "Mail",

        "Automation",

        "Analytics",
        "Settings",
        "About"
    ],

)

# -----------------------------
# Pages
# -----------------------------

if menu == "Dashboard":

    dashboard()

elif menu == "HR":

    hr_page()

elif menu == "Docs":

    docs_page()

elif menu == "Research":

    research_page()

elif menu == "Reports":

    reports_page()

elif menu == "Mail":

    mail_page()

elif menu == "Automation":

    automation_page()

elif menu == "Analytics":

    analytics_page()
elif menu == "Settings":
    settings_page()
elif menu == "About":
    about_page()
st.sidebar.divider()

if st.sidebar.checkbox("💬 AI Assistant"):

    ChatBot.chat()