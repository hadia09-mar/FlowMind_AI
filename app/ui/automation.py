import streamlit as st

from app.services.automation_service import AutomationService
from app.ui.components import footer

def automation_page():

    st.title("⚙️ Automation Center")

    trigger = st.selectbox(

        "Trigger",

        [

            "New Resume",

            "New Email",

            "New Document",

            "Daily Report"

        ]

    )

    action = st.selectbox(

        "Action",

        [

            "Send Email",

            "Generate Report",

            "Notify Admin",

            "Save to Database"

        ]

    )

    if st.button("Create Workflow"):

        AutomationService.save_workflow(
            trigger,
            action
        )

        st.success("Workflow Created Successfully")

    st.divider()

    st.subheader("📋 Saved Workflows")

    workflows = AutomationService.get_workflows()

    if workflows:

        st.dataframe(
            workflows,
            use_container_width=True
        )

    else:

        st.info("No Workflows Created Yet")
        footer()