import pandas as pd
import streamlit as st
import numpy as np

def get_user_age():
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
    return selected_age_group

def get_user_education():
    education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
    educInput = st.selectbox("Select your education level", education_levels)
    return educInput

def get_user_employment_status():
    employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
    employInput = st.selectbox("Select your employment status", employment_statuses)
    return employInput

def get_user_gender():
    genderInput = st.radio("Select your gender", options=["Male", "Female"])
    return genderInput

def get_user_state():
    stateInput = st.selectbox("Select a state",
                                                  ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                                   "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                                   "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                                   "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                                   "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
    return stateInput

def get_user_living_arrangement():
    housing_situations = ["Homeless", "Private residence", "Other"]
    livArangInput = st.selectbox("Select your living arrangement", housing_situations)
    return livArangInput

def get_user_ethnicity():
    ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]
    ethnicityInput = st.selectbox("Select your Ethnicity", ethnicities)
    return ethnicityInput

def get_user_marital_status():
    marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
    marStatInput = st.selectbox('Select your marital status:', options=marital_status_options)
    return marStatInput

def get_user_sap():
    sapInput = st.radio("SAP", options=["Yes", "No"])
    return sapInput


def prompt():

    st.markdown(
            f"""
            <div style='text-align:center'>
                <h1>Predictive Dashboard</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.form(key='my_form'):
        selected_age_group = get_user_age()
        educInput = get_user_education()
        employInput = get_user_employment_status()
        genderInput = get_user_gender()
        stateInput = get_user_state()
        livArangInput = get_user_living_arrangement()
        ethnicityInput = get_user_ethnicity()
        marStatInput = get_user_marital_status()
        sapInput = get_user_sap()

        submit_button = st.form_submit_button(label='Run')
        user_input = []
        if submit_button:
            user_input = [selected_age_group, educInput, ethnicityInput, genderInput, marStatInput, sapInput, employInput, livArangInput, stateInput]
            st.write(user_input)



def predict():
    prompt()