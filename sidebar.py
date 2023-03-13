import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

    # Create a sidebar with buttons
    m = st.markdown("""
        <style>
        /* Style for selected tabs */
        .streamlit-tabs .streamlit-tab[data-baseweb="tab"] > button[data-baseweb="button"][aria-selected="true"] {
            background-color: #007bff;
            color: #ffffff;
        }
        .streamlit-tabs .streamlit-tab[data-baseweb="tab"] > button[data-baseweb="button"][aria-selected="true"]:hover {
            background-color: #0069d9;
            color: #ffffff;
        }
        .streamlit-tabs .streamlit-tab[data-baseweb="tab"] > button[data-baseweb="button"][aria-selected="true"]:focus {
            background-color: #0056b3;
            color: #ffffff;
        }

        /* Style for unselected tabs */
        .streamlit-tabs .streamlit-tab[data-baseweb="tab"] > button[data-baseweb="button"]:not([aria-selected="true"]):hover {
            background-color: #f0f0f0;
            color: #007bff;
        }
        .streamlit-tabs .streamlit-tab[data-baseweb="tab"] > button[data-baseweb="button"]:not([aria-selected="true"]):focus {
            background-color: #e5e5e5;
            color: #007bff;
        }
        </style>
    """, unsafe_allow_html=True)

    tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

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