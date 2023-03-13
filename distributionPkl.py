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

def getTestData(model):
    X = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
    y_pred = model.predict(X)

    st.write(y_pred)

def dist():
    st.write("Distribution Null Model")
    model = loadModel()
    df = loadFile()
    st.write(df)
    getTestData(model)





    return df

    st.write(df)