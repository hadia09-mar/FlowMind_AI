import streamlit as st

from app.knowledge.loader import DocumentLoader
from app.agents.hr.analyzer import HRAnalyzer
from app.services.hr_service import HRService
from app.services.activity_service import ActivityService
from app.ui.components import footer

def hr_page():

    st.title("👨‍💼 FlowMind HR")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        file_path = f"data/{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        docs = DocumentLoader.load_document(file_path)

        resume_text = "\n".join(
            doc.page_content for doc in docs
        )

        with st.spinner("Analyzing Resume..."):

            report = HRAnalyzer.analyze(resume_text)

        # ==========================
        # Save Report to SQLite
        # ==========================

        candidate_name = uploaded_file.name
        ats_score = 80        # Temporary value

        HRService.save_report(
            candidate_name,
            ats_score
        )
        ActivityService.log(
        "HR",
        f"Resume analyzed: {candidate_name}"
)
        st.success("Analysis Complete")

        st.markdown(report)

    footer()

    st.subheader("📄 Previous HR Reports")

    reports = HRService.get_reports()

    if reports:

        st.dataframe(
            reports,
            use_container_width=True
        )