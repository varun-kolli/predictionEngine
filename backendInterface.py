import pandas as pd
import streamlit as st
import numpy as np
import joblib


def modes(column, df_modes):
        new_col = column + '_replaced'
        df_modes[new_col] = False
        mode = df_modes[column].mode()
        #print(mode[0])
        df_modes[column] = df_modes.apply(lambda row: mode[0] if pd.isna(row[column]) else row[column], axis = 1)
        df_modes[new_col] = df_modes.apply(lambda row: True if pd.isna(row[column]) else False, axis = 1)
        return df_modes

def bullet_points(items):
    st.write("- " + "\n- ".join(items))

def highlight_row(df, index):
    """
    Highlights the row with the specified integer index in a pandas DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame to highlight a row in.
    index (int): The integer index of the row to highlight.

    Returns:
    pandas.DataFrame: The original DataFrame with the specified row highlighted.
    """
    # create a copy of the DataFrame with no highlighting
    styled_df = df.style

    # highlight the specified row with a background color
    styled_df = styled_df.apply(lambda x: ['background-color: lightgreen' if x.name == index else '' for i in x], axis=1)

    # display the styled DataFrame in Streamlit
    st.dataframe(styled_df)

def displayPrediction(cluster, query, probs):
    st.title("Prediction Results")
    cluster = str(int(float(cluster)))
    st.write("")
    st.write("")
    st.subheader("Decision Tree Classification: Cluster " + cluster)

    probs_dict = {f"{i}": p for i, p in enumerate(probs.tolist())}

    keys = {
        "0": 'ADHD, Anxiety, Conduct Disorder, Delirium, Substance Abuse, Dementia, Oppositional Defiant Disorder, Other, Personality Disorder, Pervasive Developmental Disorder, Trauma-Related',
        "1": 'Bipolar, Depression',
        "2": 'Schizophrenia/psychotic'
    }

    sorted_keys = sorted(map(int, keys.keys()))
    ordered_dict = {str(key): keys[str(key)] for key in sorted_keys}

    df = pd.DataFrame.from_dict(keys, orient='index', columns=['Disorders'])
    df.index.name = 'Cluster'

    sorted_probs = sorted(map(int, probs_dict.keys()))
    ordered_probs = {str(key): probs_dict[str(key)] for key in sorted_probs}

    cluster_values = [ordered_probs[str(i)] for i in range(len(ordered_probs))]
    cluster_values = cluster_values[0]
    df['Probability'] = cluster_values

    df['Probability'] = df['Probability'].apply(lambda x: float(x) * 100)
    df['Probability'] = df['Probability'].apply(lambda x: format(x, '.2f') + '%')


    #st.dataframe(df)
    highlight_row(df, cluster)

    with st.expander("View Input"):
        smt = query
        headers = ['AGE', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']
        data = {}
        for i in range(len(headers)):
            data['Question'] = headers
            data['Answer'] = smt
            df = pd.DataFrame(data)
        with st.container():
            st.table(df.set_index('Question').T)

def process(query):
    stuff = query
    df = pd.read_csv('CSV_files/dummieCodex.csv')

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

    headers = ['AGE', 'EDUC', 'ETHNIC', 'RACE', 'GENDER', 'MARSTAT', 'SAP', 'EMPLOY', 'LIVARAG', 'NUMMHS', 'STATEFIP']

    df_query = pd.DataFrame(columns=headers)
    df_query.loc[0] = query

    def more(column, df_query):
        new_col = column + '_replaced'
        df_query[new_col] = False

        df_query[new_col] = df_query.apply(lambda row: True if pd.isna(row[column]) else False, axis = 1)
        return df_query

    df_query = more('AGE', df_query)
    df_query = more('EDUC', df_query)
    df_query = more('ETHNIC', df_query)
    df_query = more('RACE', df_query)
    df_query = more('GENDER', df_query)
    df_query = more('MARSTAT', df_query)
    df_query = more('SAP', df_query)
    df_query = more('EMPLOY', df_query)
    df_query = more('LIVARAG', df_query)
    df_query = more('NUMMHS', df_query)
    df_query = more('STATEFIP', df_query)

    first_row = df_query.iloc[0].copy()
    df.loc[0] = first_row
    df_codex = df.reset_index(drop=True)

    x = pd.get_dummies(df_codex.drop(columns = ['MH1']), drop_first = True)
    row = np.array(x.iloc[0]).reshape(1, -1)
    zeros = np.zeros((1, 10), dtype=int)
    row = np.concatenate((row, zeros), axis=1)

    loaded_model = joblib.load("pkl_files/dt_clustered_modes.sav")

    y_predicted = loaded_model.predict(row)
    cluster = y_predicted[0]
    probs = loaded_model.predict_proba(row)

    displayPrediction(cluster, query, probs)



def displayInput(stuff):
        headers = ['Age', 'Education', 'Ethnicity', 'Race', 'Sex', 'Marital Status', 'Substance Abuse Problem', 'Employment', 'Living Arrangement', 'Mental Health History', 'State']
        #query = [stuff[0], stuff[1], stuff[6], stuff[7], stuff[3], stuff[8], stuff[9], stuff[2], stuff[5], stuff[10], stuff[4]]

        df_query = pd.DataFrame(columns=headers)
        df_query.loc[0] = stuff
        df_transposed = df_query.transpose().reset_index()
        df_transposed.columns = df_transposed.iloc[0]
        df_transposed = df_transposed.iloc[1:]
        df_transposed = df_transposed.T

        # create a Streamlit table from the transposed dataframe
        st.table(df_transposed)
        #st.dataframe(df_transposed)

def interface():
    st.title("Backend Interface")
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
        st.session_state.input = []
        st.session_state.ret = []

    def set_stage(stage, input):
        st.session_state.stage = stage
        st.session_state.input= input

        interface()
        #displayInput(input)

    # Some code
    with st.form(key='my_form'):
        ageOptions = ['15-17', '18-20', '21-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65 up']
        agestuff = st.selectbox('Age Group', ageOptions, help = "Select most appropriate age group")

        education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
        educstuff = st.selectbox("Highest Completed Education Level", education_levels, help = "Select the highest level of education you have completed")

        employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
        employstuff = st.selectbox("Employment Status", employment_statuses)

        genderstuff = st.radio("Sex", options=["Male", "Female"], help = "Sex assigned at birth")

        statestuff = st.selectbox("State of Residence",
                                                      ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])


        housing_situations = ["Homeless", "Private residence", "Other"]
        livArangstuff = st.selectbox("Living Arrangement", housing_situations)

        ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]
        ethnicitystuff = st.selectbox("Ethnicity", ethnicities)

        race_options = ['Native', 'Asian', 'Black or African American', 'Pacific Islander', 'White', 'Other/Multiple']
        racestuff = st.selectbox('Race:', options=race_options)

        marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
        marStatstuff = st.selectbox('Marital Status:', options=marital_status_options)

        sapstuff = st.radio("Substance Abuse History", options=["Yes", "No"], help = "Please select 'yes' if you have experienced issues with substance abuse")

        #veteranstuff = st.radio("Veteran", options=["Yes", "No"])
        numhs =  st.selectbox("Number of Previously Diagnosed Mental Health Disorders", options = [1, 2, 3], help = "Please enter the number of mental health disorders you have been clinically diagnosed with")
        veteranstuff = "No"

        submit = st.form_submit_button('Submit', on_click=set_stage, args=(1,
                    [agestuff, educstuff, employstuff, genderstuff, statestuff, livArangstuff, ethnicitystuff, racestuff, marStatstuff, sapstuff, numhs]))

    #if st.session_state.stage > 0 and st.session_state.input != ['15-17', '0 to 8', 'Full time', 'Male', 'AL', 'Homeless', 'Mexican', 'Native', 'Never married', 'Yes', 1]:

    if st.session_state.stage > 0:
        stuff = st.session_state.input
        smt = [stuff[0], stuff[1], stuff[6], stuff[7], stuff[3], stuff[8], stuff[9], stuff[2], stuff[5], stuff[10], stuff[4]]
        headers = ['Age', 'Education', 'Ethnicity', 'Race', 'Sex', 'Marital Status', 'Substance Abuse Problem', 'Employment', 'Living Arrangement', 'Mental Health History', 'State']
        data = {}
        for i in range(len(headers)):
            data['Question'] = headers
            data['Answer'] = smt
            df = pd.DataFrame(data)
        with st.container():
            st.table(df.set_index('Question').T)

    def executeQuery(stuff):
        query = [stuff[0], stuff[1], stuff[6], stuff[7], stuff[3], stuff[8], stuff[9], stuff[2], stuff[5], stuff[10], stuff[4]]

        process(query)


    if st.session_state.stage > 0:
        st.button('View Prediction', on_click=executeQuery, args=(st.session_state.input, ))
