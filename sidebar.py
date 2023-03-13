import pandas as pd
import streamlit as st

def sideBar():

    # Create a sidebar with buttons
    m = st.markdown("""
    <style>
    div.stButton > button.primary {
        background-color: #007bff;
        color: #ffffff;
    }
    div.stButton > button.default {
        background-color: #6c757d;
        color: #ffffff;
    }
    div.stButton > button.custom1 {
        background-color: #28a745;
        color: #ffffff;
    }
    div.stButton > button.custom2 {
        background-color: #dc3545;
        color: #ffffff;
    }
    div.stButton > button.custom3 {
        background-color: #ffc107;
        color: #ffffff;
    }
    </style>""", unsafe_allow_html=True)

    tabs1 = ["Introduction", "Initial Modelling", "Data Cleaning", "Handling Null Values", "Data Balancing"]
    tabs2 = ["Tab 1", "Tab 2", "Tab 3", "Tab 4"]

    # Create a sidebar with buttons for each tab
    st.sidebar.markdown("Navigation")
    selection = [st.sidebar.button(tab, key=tab, help=tab, type='primary') for tab in tabs1]
    st.sidebar.markdown("Backend Interface")
    selection += [st.sidebar.button(tab, key=tab, help=tab, type='custom1') for tab in tabs2]

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