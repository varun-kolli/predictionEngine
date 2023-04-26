import pandas as pd
import streamlit as st

def sideBar():
    tabs1 = ["Introduction", "Initial Modelling", "Data Cleaning", "Handling Null Values", "Data Balancing", "Correlation", "Model Tracker"]
    tabs2 = ["Backend Interface"]

    st.sidebar.markdown("Navigation")
    selection = [st.sidebar.button(tab, key=tab, help=tab, type='primary') for tab in tabs1]
    selection += [st.sidebar.button(tab, key=tab, help=tab, type='secondary') for tab in tabs2]

    return selection
