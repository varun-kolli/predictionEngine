import pandas as pd
import streamlit as st


#input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
def interface():
    st.title("Backend Interface")

    age = st.number_input("Please enter your age:", min_value=0, max_value=120, step=1)

    pass