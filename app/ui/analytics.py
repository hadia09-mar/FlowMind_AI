import streamlit as st
import pandas as pd
import plotly.express as px
from app.ui.components import footer
from app.services.analytics_service import AnalyticsService


def analytics_page():

    st.title("📈 Analytics Dashboard")

    stats = AnalyticsService.get_stats()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📄 Reports", stats["reports"])
        st.metric("📂 Documents", stats["documents"])

    with col2:
        st.metric("⚙️ Workflows", stats["workflows"])
        st.metric("📝 Activities", stats["activities"])

    st.divider()

    df = pd.DataFrame({
        "Module": [
            "Reports",
            "Documents",
            "Activities",
            "Workflows"
        ],
        "Count": [
            stats["reports"],
            stats["documents"],
            stats["activities"],
            stats["workflows"]
        ]
    })

    st.subheader("📊 Module Usage")

    fig = px.bar(
        df,
        x="Module",
        y="Count",
        text="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🥧 Distribution")

    pie = px.pie(
        df,
        names="Module",
        values="Count"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )
    footer()