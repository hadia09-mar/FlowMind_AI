import streamlit as st
import pandas as pd

from app.services.hr_service import HRService
from app.services.export_service import ExportService
from app.ui.components import footer

def reports_page():

    st.title("📊 Reports Center")

    reports = HRService.get_reports()

    # Convert to DataFrame
    if reports:
        df = pd.DataFrame(
            reports,
            columns=[
                "ID",
                "Candidate",
                "ATS Score",
                "Created At"
            ]
        )

        # Search Box
        search = st.text_input("🔍 Search Candidate")

        if search:
            df = df[
                df["Candidate"]
                .str.contains(search, case=False, na=False)
            ]

        st.dataframe(
            df,
            use_container_width=True
        )

        # Export CSV
        if st.button("⬇ Export CSV"):

            filename = ExportService.export_csv(
                df,
                "reports.csv"
            )

            with open(filename, "rb") as f:

                st.download_button(
                    "📥 Download CSV",
                    data=f,
                    file_name="reports.csv",
                    mime="text/csv"
                )

    else:

        st.info("No Reports Available")
        footer()