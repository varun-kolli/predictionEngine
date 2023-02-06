import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import DecisionTreeClassifier
import numpy as np

fileName = "data.csv"
df = pd.read_csv(fileName).dropna()
df_copy = df.copy()
#model = " "
model = DecisionTreeClassifier.getModel(df)
input = ['1207979', "60-64", "Trauma-related" , "12+", "Not of Hispanic or Latino origin", "White","Male", "Now married", "No", "Unemployed", "Private residence", "1", "CD"]
prediction = DecisionTreeClassifier.getPrediction(df_copy, model, input)

def main():
    st.title("14 Question Web App")
    answers = []
    for i in range(14):
        question = "Question {}".format(i + 1)
        answer = st.text_input(question, "Enter your answer here")
        answers.append(answer)
    result = process_answers(answers)
    st.write("Result: ", result)

if __name__ == '__main__':
    main()

"""

#clean input to a row
#feed row and get prediction
#streamlit input
#output: score, prediction
#how each input demographic is in comparison to the rest of the datasets for the Prediction
 """





