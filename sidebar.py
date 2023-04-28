import pandas as pd
import streamlit as st

def sideBar():
    tabs = ["Home", "Predictive Dashboard", "Methodology", "Results"]
    methodology_tabs = ["Data Description", "Data Cleaning", "Clustering"]

    st.sidebar.subheader("Navigation")

    for tab in tabs:
       if tab == "Methodology":
           with st.beta_expander(tab):
               for method_tab in methodology_tabs:
                   selection = st.sidebar.button(method_tab, key=method_tab, help=method_tab, type="secondary")
       else:
           selection = st.sidebar.button(tab, key=tab, help=tab, type="secondary")


    return selection
