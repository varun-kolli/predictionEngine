import pandas as pd
import streamlit as st
import numpy as np

def process(input):
    df = pd.read_csv('CSV_files/dummieCodex.csv')
    cols = ['Age Group', 'Education Level', 'Employment Status', 'Sex', 'State', 'Living Arrangement', 'Ethnicity', "Race", 'Marital Status', 'Substance Abuse History', 'Veteran Status', 'Mental Health Diagnosis History']

    df_resp = pd.DataFrame({'Question': cols, 'Answer': input})
    st.dataframe(df_resp)

    def modes(column, df_modes):
            new_col = column + '_replaced'
            df_modes[new_col] = False
            mode = df_modes[column].mode()
            #print(mode[0])
            df_modes[column] = df_modes.apply(lambda row: mode[0] if pd.isna(row[column]) else row[column], axis = 1)
            df_modes[new_col] = df_modes.apply(lambda row: True if pd.isna(row[column]) else False, axis = 1)
            return df_modes

    # replace each row with its mode
    df = modes('AGE', df)
    df = modes('EDUC', df)
    df = modes('ETHNIC', df)
    df = modes('RACE', df)
    df = modes('GENDER', df)
    df = modes('MARSTAT', df)
    df = modes('SAP', df)
    df = modes('EMPLOY', df)
    df = modes('LIVARAG', df)
    df = modes('NUMMHS', df)
    df =modes('STATEFIP', df)
    
    df_resp = modes('AGE', df_resp)
    df_resp = modes('EDUC', df_resp)
    df_resp = modes('ETHNIC', df_resp)
    df_resp = modes('RACE', df_resp)
    df_resp = modes('GENDER', df_resp)
    df_resp = modes('MARSTAT', df_resp)
    df_resp = modes('SAP', df_resp)
    df_resp = modes('EMPLOY', df_resp)
    df_resp = modes('LIVARAG', df_resp)
    df_resp = modes('NUMMHS', df_resp)
    df_resp =modes('STATEFIP', df_resp)


    st.dataframe(df_resp)
    x = pd.get_dummies(df_modes.drop(columns = ['MH1']), drop_first = True)




    #display input
    #process through model
    #probability or smt
    #prompt()


def prompt():

    with st.form(key='my_form'):
        user = []

        ageOptions = ['15-17', '18-20', '21-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65 up']
        ageInput = st.selectbox('Select Age Group', ageOptions)

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

        race_options = ['Native', 'Asian', 'Black or African American', 'Pacific Islander', 'White', 'Other/Multiple']
        raceInput = st.selectbox('Select your Race:', options=race_options)

        marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
        marStatInput = st.selectbox('Select your marital status:', options=marital_status_options)


        sapInput = st.radio("SAP", options=["Yes", "No"])

        veteranInput = st.radio("Veteran", options=["Yes", "No"])
        numhs =  st.selectbox("Select the number of mental health disorders you have been diagnosed with", options = [1, 2, 3])

        submit = st.form_submit_button('Submit', on_click = process, args = ([ageInput, educInput, employInput, genderInput, stateInput, livArangInput, ethnicityInput, raceInput, marStatInput, sapInput, veteranInput, numhs], ) )

        if submit:
            form_data = [ageInput, educInput, employInput, genderInput, stateInput, livArangInput, ethnicityInput, raceInput, marStatInput, sapInput, veteranInput, numhs]
            #compute(form_data)
            #st.write(form_data)



def interface():
    st.title("Backend Interface")
    seshUser = prompt()




