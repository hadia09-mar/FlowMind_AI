import streamlit as st


def is_logged_in():

    return st.session_state.get(
        "logged_in",
        False
    )


def login():

    st.session_state.logged_in = True


def logout():

    st.session_state.logged_in = False


def initialize():

    if "logged_in" not in st.session_state:

        st.session_state.logged_in = False