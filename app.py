from analytics_by_months import month_analytics
from update_tab import add_update_tab
from analytics_tab import add_analytics_tab
import streamlit as st
st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)
st.title("EXPENSE TRACKER")
tab1,tab2,tab3=st.tabs(["Update","Analytics by category","Analytics by Month"])
with tab1:
    add_update_tab()
with tab2:
    add_analytics_tab()
with tab3:
    month_analytics()

