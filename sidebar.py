import pandas as pd
import streamlit as st

#disable homes
#hyper link samdha
#advsor + team in box
#round poredict proba
#center text align indexes cluster
#comma separate bars
#features -> predictors + drop veteran column
#data cleaningn columns full name
#clustering image\#new flowchart
#Machine Learning: Explain what that is
#details on stuff. data partitioning, which hyperparameters

#explain more about AWS

#more about feature importance
#decision tree download
#hardcode 0 as 1


def sideBar():
    tabs = ["Home", "Predictive Dashboard", "Methodology", "Data Description", "Data Cleaning", "Clustering", "Machine Learning", "Results"]

    st.sidebar.subheader("Navigation")
    home_button = st.sidebar.button("Home", key="Home", type="primary")
    dashboard_button = st.sidebar.button("Predictive Dashboard", key="Predictive Dashboard", type="primary")
    st.write(" ")
    st.sidebar.subheader("Methodology")
    data_description_button = st.sidebar.button("Data Description", key="Data Description", type="primary")
    data_cleaning_button = st.sidebar.button("Data Cleaning", key="Data Cleaning", type="primary")
    clustering_button = st.sidebar.button("Clustering", key="Clustering", type="primary")
    ml_button = st.sidebar.button("Machine Learning", key="Machine Learning", type="primary")
    results_button = st.sidebar.button("Results", key="Results", type="primary")

    # Store the buttons in a list
    selection = [home_button, dashboard_button, data_description_button, data_cleaning_button, clustering_button, ml_button, results_button]

    # Return the list of buttons
    return selection


