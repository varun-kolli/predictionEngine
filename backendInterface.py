import pandas as pd
import streamlit as st

from streamlit.state.session_state import SessionState

def initialize_session():
    return SessionState.get(age='', educ='', employ='', ethnicity='', gender='', liv_arang='', race='', sap='', state='', veteran='')


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

def display_user_input(state):
    st.write(f"Age: {state.age}")
    st.write(f"Education Level: {state.educ}")
    st.write(f"Employment Status: {state.employ}")
    st.write(f"Ethnicity: {state.ethnicity}")
    st.write(f"Gender: {state.gender}")
    st.write(f"Living Arrangement: {state.liv_arang}")
    st.write(f"Racial Group: {state.race}")
    st.write(f"SAP: {state.sap}")
    st.write(f"State: {state.state}")
    st.write(f"Veteran: {state.veteran}")

def get_user_input(state):
    age = st.number_input(label='Enter Age')
    educ_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
    educ = st.selectbox("Select your education level", educ_levels)
    employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
    employ = st.selectbox("Select your employment status", employment_statuses)
    ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]
    ethnicity = st.selectbox("Select your Ethnicity", ethnicities)
    gender = st.radio("Select your gender", options=["Male", "Female"])
    housing_situations = ["Homeless", "Private residence", "Other"]
    liv_arang = st.selectbox("Select your living arrangement", housing_situations)
    racial_groups = ["Native", "Asian", "Black or African American", "Pacific Islander", "White", "Other/Multiple"]
    race = st.selectbox("Select your racial group", racial_groups)
    sap = st.radio("SAP", options=["Yes", "No"])
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    state = st.selectbox("Select a state", states)
    veteran = st.radio("Veteran", options=["Yes", "No"])

    state.age = convertAge(int(age))
    state.educ = educ
    state.employ = employ
    state.ethnicity = ethnicity
    state.gender = gender
    state.liv_arang = liv_arang
    state.race = race
    state.sap = sap
    state.state = state
    state.veteran = veteran

def interface():
    st.title("Backend Interface")
    state = initialize_session()
    get_user_input(state)
    display_user_input(state)