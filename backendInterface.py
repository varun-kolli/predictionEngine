import pandas as pd
import streamlit as st
import numpy as np

def modes(column, df_modes):
        new_col = column + '_replaced'
        df_modes[new_col] = False
        mode = df_modes[column].mode()
        #print(mode[0])
        df_modes[column] = df_modes.apply(lambda row: mode[0] if pd.isna(row[column]) else row[column], axis = 1)
        df_modes[new_col] = df_modes.apply(lambda row: True if pd.isna(row[column]) else False, axis = 1)
        return df_modes

def process(stuff):
    stuff = stuff
    df = pd.read_csv('CSV_files/dummieCodex.csv')
    cols = ['Age Group', 'Education Level', 'Employment Status', 'Sex', 'State', 'Living Arrangement', 'Ethnicity', "Race", 'Marital Status', 'Substance Abuse History', 'Veteran Status', 'Mental Health Diagnosis History']

    df_resp = pd.DataFrame({'Question': cols, 'Answer': stuff})
    st.dataframe(df_resp)

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
    df = modes('STATEFIP', df)
    st.header("hey")

    headers = ['AGE', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']

    query = [stuff[0], stuff[1], stuff[6], stuff[7], stuff[3], stuff[8], stuff[9], stuff[2], stuff[5], stuff[10], stuff[-1], stuff[4]]
    st.write(query)

    df_query = pd.DataFrame(columns=headers)
    #df_query.loc[0] = query

    st.write(df_query)
# Load the model from the file
   # loaded_model = joblib.load('pkl_files/dt_clustered_modes.sav')
    #loaded_model.predict(query)

    #x = pd.get_dummies(df_modes.drop(columns = ['MH1']), drop_first = True)




    #display stuff
    #process through model
    #probability or smt
    #prompt()


def prompt():

    with st.form(key='my_form'):
        user = []

        ageOptions = ['15-17', '18-20', '21-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65 up']
        agestuff = st.selectbox('Select Age Group', ageOptions)

        education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
        educstuff = st.selectbox("Select your education level", education_levels)

        employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
        employstuff = st.selectbox("Select your employment status", employment_statuses)

        genderstuff = st.radio("Select your gender", options=["Male", "Female"])

        statestuff = st.selectbox("Select a state",
                                                      ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])


        housing_situations = ["Homeless", "Private residence", "Other"]
        livArangstuff = st.selectbox("Select your living arrangement", housing_situations)

        ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]

        ethnicitystuff = st.selectbox("Select your Ethnicity", ethnicities)

        race_options = ['Native', 'Asian', 'Black or African American', 'Pacific Islander', 'White', 'Other/Multiple']
        racestuff = st.selectbox('Select your Race:', options=race_options)

        marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
        marStatstuff = st.selectbox('Select your marital status:', options=marital_status_options)


        sapstuff = st.radio("SAP", options=["Yes", "No"])

        veteranstuff = st.radio("Veteran", options=["Yes", "No"])
        numhs =  st.selectbox("Select the number of mental health disorders you have been diagnosed with", options = [1, 2, 3])

        submit = st.form_submit_button('Submit', on_click = process, args = ([agestuff, educstuff, employstuff, genderstuff, statestuff, livArangstuff, ethnicitystuff, racestuff, marStatstuff, sapstuff, veteranstuff, numhs], ) )

        if submit:
            form_data = [agestuff, educstuff, employstuff, genderstuff, statestuff, livArangstuff, ethnicitystuff, racestuff, marStatstuff, sapstuff, veteranstuff, numhs]
            #compute(form_data)
            #st.write(form_data)



def interface():
    st.title("Backend Interface")
    seshUser = prompt()




