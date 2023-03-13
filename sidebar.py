import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

    # Create a sidebar with buttons
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007bff;
        color: #ffffff;
    }
    div.stButton > button:hover {
        background-color: #0069d9;
        color: #ffffff;
    }
    div.stButton > button:focus {
        background-color: #0056b3;
        color: #ffffff;
    }
    </style>""", unsafe_allow_html=True)

    tabs = ["Introduction", "Initial Modelling", "Data Cleaning", "Data Balancing", "Random Forest"]

    # Create a sidebar with buttons for each tab
    st.sidebar.markdown("Navigation")
    selection = [st.sidebar.button(tab, key=tab, help=tab, type='secondary') for tab in tabs]
    return selection

"""
    # Depending on which tab is selected, show the appropriate content
    if selection[0]:
        st.header("Introduction")
        st.write("This is the introduction tab.")
    if selection[1]:
        st.header("Initial Modelling")
        st.write("This is the initial modelling tab.")
    if selection[2]:
        st.header("Decision Tree Improvements")
        st.write("This is the decision tree improvements tab.")
    if selection[3]:
        st.header("Data Balancing")
        st.write("This is the data balancing tab.")
    if selection[4]:
        st.header("Random Forest")
        st.write("This is the random forest tab.")
"""