import pandas as pd
import streamlit as st
from phase1 import introduction

tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

# Create a sidebar with buttons without the button box
st.sidebar.markdown("# Tab Selector")
for tab in tabs:
    if st.sidebar.button(tab, key=tab, help=tab, type='default', css=".streamlit-button button {border:none}"):
        selection = tab

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