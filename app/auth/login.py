import streamlit as st

from app.auth.auth import login_user
from app.auth.session import login


def login_page():

    st.title("🔐 Login")

    username = st.text_input(
        "Username",
        value=st.session_state.get(
            "remember_user",
            ""
        )
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    remember = st.checkbox("Remember Me")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Login"):

            user = login_user(
                username.strip(),
                password
            )

            if user:

                login()

                if remember:

                    st.session_state.remember_user = username.strip()

                st.success("Login Successful")

                st.rerun()

            else:

                st.error("Invalid Username or Password")

    with col2:

        if st.button("Create Account"):

            st.session_state.show_register = True

            st.rerun()