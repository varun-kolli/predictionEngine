import pandas as pd
import streamlit as st
from phase1 import introduction

tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

# Create a sidebar with buttons
st.sidebar.markdown("# Tab Selector")
if st.sidebar.button(tabs[0]):
    selection = tabs[0]
if st.sidebar.button(tabs[1]):
    selection = tabs[1]
if st.sidebar.button(tabs[2]):
    selection = tabs[2]
if st.sidebar.button(tabs[3]):
    selection = tabs[3]
if st.sidebar.button(tabs[4]):
    selection = tabs[4]

# Depending on which tab is selected, show the appropriate content
if selection == "Introduction":
    st.header("Introduction")
    st.write("This is the introduction tab.")
elif selection == "Initial Modelling":
    st.header("Initial Modelling")
    st.write("This is the initial modelling tab.")
elif selection == "Decision Tree Improvements":
    st.header("Decision Tree Improvements")
    st.write("This is the decision tree improvements tab.")
elif selection == "Data Balancing":
    st.header("Data Balancing")
    st.write("This is the data balancing tab.")
elif selection == "Random Forest":
    st.header("Random Forest")
    st.write("This is the random forest tab.")