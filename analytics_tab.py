import requests
import streamlit as st
from datetime import datetime
import pandas as pd

API_URL = "http://localhost:8000"
def add_analytics_tab():
    st.form("analysis")
    col1,col2 = st.columns(2)
    with col1:
              start_date = st.date_input("Enter start Date", datetime(2024, 8, 1), label_visibility="collapsed")
    with col2:
              end_date = st.date_input("Enter end Date", datetime(2024, 8, 15), label_visibility="collapsed")
    if st.button("Analyze"):
        payload={"start_date":start_date.strftime("%Y-%m-%d"),"end_date":end_date.strftime("%Y-%m-%d")}
        analytics=requests.post(f"{API_URL}/analytics_by_summary", json=payload)
        analytics_data=analytics.json()
        data=[]
        for category,values in analytics_data.items():
            data.append({"category":category,
             "total":values["total"],
                "percentage":values["percentage"]})
        df=pd.DataFrame(data)
        st.table(df)
        st.bar_chart(
            data=df.set_index("category") ["total"]

        )


