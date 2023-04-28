import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Home", "Predictive Dashboard", "Results"]
    #methodology_tabs = ["Data Description", "Data Cleaning", "Clustering"]
    st.sidebar.subheader("Navigation")

    selection = [st.sidebar.button(tab, key=tab, help=tab, type ="secondary") for tab in tabs]


    return selection
