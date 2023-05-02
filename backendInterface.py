import pandas as pd
import streamlit as st
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
import numpy as np

counter = 0


#input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
def convertAge(age):
    # define subgroups with corresponding age ranges
    subgroups = {
        '0-11': range(0, 12),
        '12-14': range(12, 15),
        '15-17': range(15, 18),
        '18-20': range(18, 21),
        '21-24': range(21, 25),
        '25-29': range(25, 30),
        '30-34': range(30, 35),
        '35-39': range(35, 40),
        '40-44': range(40, 45),
        '45-49': range(45, 50),
        '50-54': range(50, 55),
        '55-59': range(55, 60),
        '60-64': range(60, 65),
        '65 up': range(65, 150)  # use a large upper bound to include all ages 65 and above
    }

    # classify the age variable
    for group, age_range in subgroups.items():
        if age in age_range:
            age_group = group
            break
    else:
        age_group = '-9'

    # store the age group as a string variable
    age_group_str = age_group.replace(' ', '')  # remove any spaces

    return age_group_str

def smt(input):
    """ Callback function during adding a new project. """
    # display a warning if the user entered an existing name
    if input in st.session_state.user:
        st.warning(f'The name "{input}" is already exists.')
    else:
        st.session_state.projects.append(input)

def prompt():

    """
    if "user" not in st.session_state:
        st.session_state.user = []


    with st.form(key='my_form'):
        user = []

        subgroups = {
            '0-11': range(0, 12),
            '12-14': range(12, 15),
            '15-17': range(15, 18),
            '18-20': range(18, 21),
            '21-24': range(21, 25),
            '25-29': range(25, 30),
            '30-34': range(30, 35),
            '35-39': range(35, 40),
            '40-44': range(40, 45),
            '45-49': range(45, 50),
            '50-54': range(50, 55),
            '55-59': range(55, 60),
            '60-64': range(60, 65),
            '65 up': range(65, 150)  # use a large upper bound to include all ages 65 and above
        }

        selected_age_group = st.selectbox('Select Age Group', list(subgroups.keys()))


        education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
        educInput = st.selectbox("Select your education level", education_levels)

        employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
        employInput = st.selectbox("Select your employment status", employment_statuses)

        genderInput = st.radio("Select your gender", options=["Male", "Female"])

        stateInput = st.selectbox("Select a state",
                                                      ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])


        housing_situations = ["Homeless", "Private residence", "Other"]
        livArangInput = st.selectbox("Select your living arrangement", housing_situations)

        ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]

        ethnicityInput = st.selectbox("Select your Ethnicity", ethnicities)

        marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
        marStatInput = st.selectbox('Select your marital status:', options=marital_status_options)

        sapInput = st.radio("SAP", options=["Yes", "No"])

        veteranInput = st.radio("Veteran", options=["Yes", "No"])
        numhs =  st.selectbox("Select the number of mental health disorders you have been diagnosed with", options = [1, 2, 3])

        submit_button = st.form_submit_button(label='Run', on_click=smt, args=([ageInput, educInput, ethnicityInput, raceInput, genderInput, marStatInput, sapInput, employInput, livArangInput, veteranInput, stateInput, numhs], ))

        #if submit_button:
            #user_input = [ageInput, educInput, ethnicityInput, raceInput, genderInput, marStatInput, sapInput, employInput, livArangInput, veteranInput, stateInput, numhs]
            #st.session_state.user.append(user_input)


    if st.session_state.user:
            st.write("User inputs:")
            st.write(user_input)

    st.session_state.user = []
    return st.session_state.user
    """
    pass

import streamlit as st


def show():

    st.write(
        """
        ## 💯 Counter

        The most basic example: Store a count in `st.session_state` and increment when
        clicked.
        """
    )

    if "counter" not in st.session_state:
            st.session_state.counter = 0

    def increment():
        st.session_state.counter += 1

    st.write("Counter:", st.session_state.counter)
    st.button("Plus one!", on_click=show)

    if st.session_state.counter >= 50:
        st.success("King of counting there! Your trophy for reaching 50: 🏆")
    elif st.session_state.counter >= 10:
        st.warning("You made it to 10! Keep going to win a prize 🎈")


def getCounter():
    return counter

def interface():
    st.title("Backend Interface")
    show()

    #seshUser = prompt()




