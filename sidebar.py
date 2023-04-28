import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Home", "Predictive Dashboard"]
    st.sidebar.subheader("Navigation")

    selection = [st.sidebar.button(tab, key=tab, help=tab, type ="secondary") for tab in tabs]


    with st.expander("Methodology"):
        methodology_tabs = ["Data Description", "Data Cleaning", "Clustering"]

        selection = [st.sidebar.button(tab, key=tab, help=tab, type ="secondary") for tab in methodology_tabs]


    return selection
