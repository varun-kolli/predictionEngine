import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Introduction", "Initial Modelling", "Data Cleaning", "Handling Null Values", "Data Balancing", "Correlation", "Model Tracker"]
    tabs.append("Backend Interface")

    st.sidebar.subheader("Navigation")
    selection = [st.sidebar.button(tab, key=tab, help=tab, type = 'secondary') for tab in tabs]

    return selection
