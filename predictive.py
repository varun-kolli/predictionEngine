import pandas as pd
import streamlit as st
import numpy as np


def prompt():

    subgroups = {'0-11': range(0, 12), '12-14': range(12, 15), '15-17': range(15, 18),
                 '18-20': range(18, 21), '21-24': range(21, 25), '25-29': range(25, 30),
                 '30-34': range(30, 35), '35-39': range(35, 40), '40-44': range(40, 45),
                 '45-49': range(45, 50), '50-54': range(50, 55), '55-59': range(55, 60),
                 '60-64': range(60, 65), '65 up': range(65, 150)}

    education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
    employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
    gender_options = ["Male", "Female"]
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS",
              "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY",
              "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    housing_situations = ["Homeless", "Private residence", "Other"]
    ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]
    marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']


   with st.form(key='my_form'):
       selected_age_group = st.selectbox('Select Age Group', list(subgroups.keys()))
       educInput = st.selectbox("Select your education level", education_levels)
       employInput = st.selectbox("Select your employment status", employment_statuses)
       genderInput = st.radio("Select your gender", options=gender_options)
       stateInput = st.selectbox("Select a state", states)
       livArangInput = st.selectbox("Select your living arrangement", housing_situations)
       ethnicityInput = st.selectbox("Select your Ethnicity", ethnicities)
       marStatInput = st.selectbox('Select your marital status:', options=marital_status_options)
       sapInput = st.radio("SAP", options=["Yes", "No"])

       if st.form_submit_button(label='Predict'):
           user_input = [selected_age_group, educInput, ethnicityInput, genderInput, marStatInput, sapInput,
                         employInput, livArangInput, stateInput]
           st.write(user_input)


def predict():
    set_session_state
    prompt()

def set_session_state():

    if 'query' not in st.session_state:
        st.session_state.query = []