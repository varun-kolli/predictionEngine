import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# Modeling Packages
import sklearn
from sklearn.model_selection import train_test_split   # For Data Partitioning
from sklearn.linear_model import LinearRegression      # To implement Linear Regression
from sklearn.feature_selection import RFE              # To implement RFE
from sklearn.model_selection import StratifiedKFold, KFold              # For creating folds
from sklearn.model_selection import cross_val_score    # For implementing Cross Validation experiments
from sklearn.model_selection import GridSearchCV       # To implement GridSearch CV
from sklearn.model_selection import RandomizedSearchCV # To implement Randomized Search CV
from sklearn.linear_model import Lasso, Ridge          # To implement Lasso and Ridge Regression
from sklearn.metrics import classification_report
#from sklearn.metrics import plot_confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier

import warnings
warnings.filterwarnings('ignore')

def getPrediction(df, model, input):
    cols =  ["Unnamed: 0", 'AGE', 'MH1', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']
    df.iloc[0] = input
    df_dummies = pd.get_dummies(df.drop(columns = ['MH1', 'Unnamed: 0']), drop_first = True)
    queryRow = np.array(df_dummies.iloc[0]).reshape(1, -1)
    prediction = model.predict(queryRow)
    #print('Score: ', model.best_score_)
    #print('Parameters: ', model.best_params_)
    return prediction

def getModel(df):
    input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
    df.iloc[0] = input
    x = pd.get_dummies(df.drop(columns = ['MH1', 'Unnamed: 0']), drop_first = True)
    y = df['MH1']
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size = 0.4, random_state = 1)
    folds = KFold(n_splits = 5, shuffle = True, random_state = 1)
    clf = DecisionTreeClassifier(random_state = 42)

    hyper_params_new = {
        'max_depth': list(range(50, 55)),
        'min_samples_split': list(range(1, 7)),
        'min_samples_leaf': list(range(42, 47))
    }

    # Call GridSearchCV()
    model_clf = GridSearchCV(estimator = clf,
                            param_grid = hyper_params_new,
                            scoring = 'f1_weighted', # Use a suitable regression metric
                            cv = folds,
                            verbose = 1,
                            n_jobs = -1) # Will utilize all available CPUs

    model_clf.fit(train_x, train_y)
    input = np.array(test_x.iloc[10]).reshape(1, -1)

    return model_clf
    #print('Improved score: ', model_clf.best_score_)
    #print('Improved parameters: ', model_clf.best_params_)

def main():
    fileName = "data.csv"
    df = pd.read_csv(fileName).dropna()
    st.title("Predicting Mental Health Disorder from Demographic Information")
    userInput =  ['AGE', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']
    answers = []
    def ask(header, options):
        selected_option = st.radio("Select" + header + " :", options)
        #st.write(f"You selected: {selected_option}")
        answers.append(selected_option)

    for i in range(len(userInput)):
        header = userInput[i]
        options = df[header].unique()
        ask(header, options)


    answers.insert(0, "1207979")
    answers.insert(2, "Trauma-related")
    backend(df, answers)

def backend(df, answers):
    df_copy = df.copy()
    #st.write(len(answers), answers)

    #model = " "
    #model = getModel(df)
    input = ['1207979', "60-64", "Trauma-related" , "12+", "Not of Hispanic or Latino origin", "White","Male", "Now married", "No", "Unemployed", "Private residence", "1", "CD"]
    st.write(len(input), input)

    prediction = getPrediction(df_copy, model, input)
    st.header(prediction)
    #return prediction

if __name__ == '__main__':
    main()





