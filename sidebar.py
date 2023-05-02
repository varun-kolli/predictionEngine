import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Home", "Predictive Dashboard", "Methodology", "Data Description", "Data Cleaning", "Clustering", "Machine Learning", "Results"]

    st.sidebar.subheader("Navigation")
    home_button = st.sidebar.button("Home", key="Home", help="Home", type="secondary", disabled = True)
    dashboard_button = st.sidebar.button("Predictive Dashboard", key="Predictive Dashboard", help="Predictive Dashboard", type="secondary")
    methodology_button = st.sidebar.button("Methodology", key="Methodology", help="Methodology", type="secondary")
    data_description_button = st.sidebar.button("Data Description", key="Data Description", help="Data Description", type="secondary")
    data_cleaning_button = st.sidebar.button("Data Cleaning", key="Data Cleaning", help="Data Cleaning", type="secondary")
    clustering_button = st.sidebar.button("Clustering", key="Clustering", help="Clustering", type="secondary")
    ml_button = st.sidebar.button("Machine Learning", key="Machine Learning", help="Machine Learning", type="secondary")
    results_button = st.sidebar.button("Results", key="Results", help="Results", type="secondary")

    # Store the buttons in a list
    selection = [home_button, dashboard_button, methodology_button, data_description_button, data_cleaning_button, clustering_button, ml_button, results_button]

    # Return the list of buttons
    return selection

    return selection
