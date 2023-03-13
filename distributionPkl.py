import pandas as pd
import streamlit as st
import joblib
import numpy as np

def dist():
    st.write("Distribution Null Model")
    model = joblib.load('pkl_files/dt_dist.sav')

    fileName = "CSV_files/data.csv"
    df = pd.read_csv(fileName).dropna()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    st.write(df)