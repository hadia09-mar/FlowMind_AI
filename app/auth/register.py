import streamlit as st

from app.auth.auth import register_user


def register_page():

    st.title("📝 Register")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Create Account"):

        if register_user(
            username,
            password
        ):

            st.success("Account Created!")

        else:

            st.error("Username already exists.")