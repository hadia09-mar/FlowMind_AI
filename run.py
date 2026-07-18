import streamlit as st

from app.auth.auth import (
    create_user_table,
    create_documents_table,
    create_hr_table,
    create_research_table,
    create_activity_table,
)

from app.auth.login import login_page
from app.auth.register import register_page
from app.auth.session import (
    initialize,
    is_logged_in,
    logout,
)

from app.ui.dashboard import dashboard
from app.ui.hr import hr_page
from app.ui.docs import docs_page
from app.ui.research import research_page
from app.ui.reports import reports_page
from app.ui.mail import mail_page
from app.ui.automation import automation_page
from app.ui.analytics import analytics_page
from app.ui.settings import settings_page
from app.chat.chatbot import ChatBot


# -------------------------
# Streamlit Config
# -------------------------

st.set_page_config(
    page_title="FlowMind AI",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Database
# -------------------------

create_user_table()
create_documents_table()
create_hr_table()
create_research_table()
create_activity_table()

# -------------------------
# Session
# -------------------------

initialize()

if "show_register" not in st.session_state:
    st.session_state.show_register = False

# -------------------------
# Login/Register
# -------------------------

if not is_logged_in():

    if st.session_state.show_register:
        register_page()
    else:
        login_page()

    st.stop()

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("🤖 FlowMind AI")
st.sidebar.caption("Enterprise AI Automation Platform")
st.sidebar.divider()

if st.sidebar.button("Logout"):
    logout()
    st.rerun()

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
    ]
)

# -------------------------
# Pages
# -------------------------

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

st.sidebar.divider()

if st.sidebar.checkbox("💬 AI Assistant"):
    ChatBot.chat()