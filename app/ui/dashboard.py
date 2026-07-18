import streamlit as st
import pandas as pd
import plotly.express as px
from app.ui.components import footer
from app.services.analytics_service import AnalyticsService
from app.services.activity_service import ActivityService
from app.services.dashboard_service import DashboardService


def dashboard():

    stats = AnalyticsService.get_stats()
    counts = DashboardService.get_counts()

    st.title("🤖 FlowMind AI")

    st.header("Welcome to FlowMind AI")

    st.write("""
### Enterprise AI Automation Platform

FlowMind AI is an enterprise-level AI Automation Platform where multiple AI Agents collaborate to automate business workflows.

### Available Modules

👨‍💼 HR AI

📄 Docs AI

🔍 Research AI

📊 Reports AI

📧 Mail AI

📈 Analytics
""")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🤖 AI Agents", stats["agents"])

    with col2:
        st.metric("📄 Reports", counts["reports"])

    with col3:
        st.metric("📝 Activities", counts["activities"])

    with col4:
        st.metric("🗄 Database", stats["database"])

    footer()

    # -------------------------------
    # Recent Activity
    # -------------------------------

    st.subheader("📝 Recent Activity")

    logs = ActivityService.get_logs()

    if logs:

        st.dataframe(
            logs,
            use_container_width=True
        )

        # -------------------------------
        # Activity Chart
        # -------------------------------

        st.subheader("📈 Activity Overview")

        df = pd.DataFrame(
            logs,
            columns=[
                "module",
                "activity",
                "created_at"
            ]
        )

        fig = px.bar(
            df,
            x="module",
            title="Activities by Module"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("No activity found.")