import streamlit as st

from app.auth.auth import login_user
from app.auth.session import login


def login_page():

    st.title("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    remember = st.checkbox("Remember Me")

    if st.button("Login"):

        user = login_user(
            username,
            password
        )

        if user:

            login()

            # Save username only
            st.session_state["username"] = username

            if remember:
                st.session_state["remember"] = True

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Username or Password")