import streamlit as st


def initialize():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "show_register" not in st.session_state:
        st.session_state.show_register = False

    if "remember_user" not in st.session_state:
        st.session_state.remember_user = ""


def login():

    st.session_state.logged_in = True


def logout():

    st.session_state.logged_in = False


def is_logged_in():

    return st.session_state.logged_in