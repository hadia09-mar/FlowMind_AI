import streamlit as st

from app.services.mail_service import MailService
from app.ui.components import footer

def mail_page():

    st.title("📧 AI Email Generator")

    recipient = st.text_input("Recipient")

    subject = st.text_input("Subject")

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Apology",
            "Follow-up"
        ]
    )

    purpose = st.text_area(
        "Purpose"
    )

    if st.button("Generate Email"):

        with st.spinner("Generating..."):

            email = MailService.generate_email(
                recipient,
                subject,
                purpose,
                tone
            )

        st.success("Email Generated")

        st.text_area(
            "Generated Email",
            email,
            height=300
        )
        footer()