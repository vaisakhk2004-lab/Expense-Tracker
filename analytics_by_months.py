import requests
import streamlit as st

import pandas as pd

API_URL = "http://localhost:8000"
def month_analytics():
    if st.button("Analyze Monthly"):
        payload={"start_date":"2024-08-03","end_date":"2024-09-30"}
        analytics=requests.post(f"{API_URL}/analytics_by_month", json=payload)
        analytics_data=analytics.json()
        df = pd.DataFrame(analytics_data)

        df["total"] = df["total"].round(2)

        st.table(df)

        st.bar_chart(
            data=df,
            x="month",
            y="total"
        )




