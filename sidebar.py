import pandas as pd
import streamlit as st

def sideBar():

    def e1():
        tabs = ["Home", "Predictive Dashboard", "Methodology", "Results"]
        methodology_tabs = ["Data Description", "Data Cleaning", "Clustering"]
        st.sidebar.subheader("Navigation")

        selection = [st.sidebar.button(tab, key=tab, help=tab, type ="secondary") for tab in tabs]

    return selection

    methodology = selection[2]

    if methodology:
        st.write("sidebar")





    return selection
