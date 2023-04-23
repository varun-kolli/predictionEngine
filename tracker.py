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

    st.subheader("Initial Decision Tree Attempt")

   st.write("First Attempt with the partially cleaned SAMDHA data resulted in a low F1 score of <span style='color:red'>0.493</span>.", unsafe_allow_html=True)
