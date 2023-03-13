import pandas as pd
import streamlit as st
import joblib
import numpy as np

def loadFile():
    fileName = "CSV_files/data.csv"
    df = pd.read_csv(fileName).dropna()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def loadModel():
    model = joblib.load('pkl_files/dt_modes.sav')
    return model

def getTestData(model):
    X = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
    y_pred = model.predict(X)

    st.write(y_pred)

def getPrediction(df, model, input):
    cols =  ["Unnamed: 0", 'AGE', 'MH1', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']
    df.iloc[0] = input
    df_dummies = pd.get_dummies(df.drop(columns = ['MH1', 'Unnamed: 0']), drop_first = True)
    print(df_dummies.columns)
    queryRow = np.array(df_dummies.iloc[0]).reshape(1, -1)
    prediction = model.predict(queryRow)
    #print('Score: ', model.best_score_)
    #print('Parameters: ', model.best_params_)
    return prediction

def dist():
    st.write("Distribution Null Model")
    model = loadModel()
    df = loadFile()
    st.write(df)
    input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
    y_pred = getPrediction(df, model, input)
    st.write(y_pred)

    return df

