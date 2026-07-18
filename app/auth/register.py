import streamlit as st

from app.auth.auth import register_user


def register_page():

    st.title("📝 Create Account")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Create Account"):

        if username == "" or password == "":

            st.error("All fields are required")

        elif len(username) < 3:

            st.error("Username must be at least 3 characters")

        elif len(password) < 6:

            st.error("Password must be at least 6 characters")

        elif password != confirm_password:

            st.error("Passwords do not match")

        else:

            success = register_user(
                username,
                password
            )

            if success:

                st.success("Account Created Successfully")

                st.info("Please Login")

                st.session_state.show_register = False

                st.rerun()

            else:

                st.error("Username already exists")

    if st.button("⬅ Back to Login"):

        st.session_state.show_register = False

        st.rerun()