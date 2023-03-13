import pandas as pd
import streamlit as st
import joblib
import numpy as np

@st.cache_data
def loadFile():
    fileName = "CSV_files/data.csv"
    df = pd.read_csv(fileName).dropna()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df

@st.cache_data
def loadModel():
    model = joblib.load('pkl_files/dt_dist.sav')
    return model

def dist():
    st.write("Distribution Null Model")
    model = loadModel()
    file = loadFile()



    return df

    st.write(df)