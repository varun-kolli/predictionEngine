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
        div.stButton > button.custom1 {
            background-color: #87CEFA;
            color: #ffffff;
        }
        </style>""", unsafe_allow_html=True)

    tabs1 = ["Introduction", "Initial Modelling", "Data Cleaning", "Handling Null Values", "Data Balancing"]
    tabs2 = ["Backend Interface"]

    # Create a sidebar with buttons for each tab
    st.sidebar.markdown("Navigation")
    selection = [st.sidebar.button(tab, key=tab, help=tab, type='primary') for tab in tabs1]
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