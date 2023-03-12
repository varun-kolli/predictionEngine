import pandas as pd
import streamlit as st
from phase1 import introduction

tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

# Create a sidebar with buttons
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Data Balancing", "Random Forest"]

# Create a sidebar with buttons for each tab
st.sidebar.markdown("# Tab Selector")
selection = st.sidebar.button(tabs[0], key=tabs[0], help=tabs[0], type='default')
for tab in tabs[1:]:
    selection |= st.sidebar.button(tab, key=tab)

# Depending on which tab is selected, show the appropriate content
if "Introduction" in selection:
    st.header("Introduction")
    st.write("This is the introduction tab.")
if "Initial Modelling" in selection:
    st.header("Initial Modelling")
    st.write("This is the initial modelling tab.")
if "Decision Tree Improvements" in selection:
    st.header("Decision Tree Improvements")
    st.write("This is the decision tree improvements tab.")
if "Data Balancing" in selection:
    st.header("Data Balancing")
    st.write("This is the data balancing tab.")
if "Random Forest" in selection:
    st.header("Random Forest")
    st.write("This is the random forest tab.")
