from app.llm.gemini import llm


class MailService:

    @staticmethod
    def generate_email(recipient, subject, purpose, tone):

        prompt = f"""
Write a {tone} email.

Recipient: {recipient}

Subject: {subject}

Purpose:
{purpose}

Return only the email.
"""

        response = llm.invoke(prompt)

        return response.content