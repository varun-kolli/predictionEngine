import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Introduction", "Initial Modelling", "Data Cleaning", "Handling Null Values", "Data Balancing", "Correlation", "Model Tracker"]
    tabs.append("Backend Interface")

    st.sidebar.subheader("Navigation")
    selection = [st.sidebar.button(tab, key=tab, help=tab) for tab in tabs]

    st.sidebar.css(
        """
        .sidebar-content {
            border: 1px solid gray;
            padding: 10px;
        }
        """
    )

    return selection
