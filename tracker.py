import pandas as pd
import streamlit as st

def report():
    st.markdown(
        f"""
        <div style='text-align:center'>
            <h1>Model Tracker</h1>
        </div>
        """,
        unsafe_allow_html=True
    )