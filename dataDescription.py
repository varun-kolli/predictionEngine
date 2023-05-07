import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt


def display():
    disorders = {
        "Depressive ": 1471993,
        "Anxiety ": 707078,
        "Trauma/stressor-related ": 887413,
        "Schizophrenia /psychotic ": 669384,
        "Bipolar": 595334,
        "ADHD": 443138,
        "Substance Abuse": 187839,
        "Other ": 498034,
        "Oppositional defiance": 109143,
        "Conduct ": 86239,
        "Pervasive developmental": 58396,
        "Personality": 47905,
        "Delirium, dementia": 16873
    }

    df = pd.DataFrame.from_dict(disorders, orient='index', columns=['#Cases'])
    df = df.reset_index().rename(columns={'index': 'Disorder Type'})

    # Create vertical bar chart using Altair
    bars = alt.Chart(df).mark_bar().encode(
        x=alt.X('Disorder Type:N', sort='-y', axis=alt.Axis(labelAngle=90)),
        y='#Cases:Q'
    )

    chart = (bars).properties(
        width=700,
        height=500,
        title='Mental Health Disorders in 2019'
    )

    st.altair_chart(chart, use_container_width=True)
    st.caption("Count of Disorder for each Mental Health Diagnosis. Excludes Missing/unknown/notcollected/invalid/deferred diagnosis")

def about():
    st.subheader("About the Data")
    st.write("")
    st.write('The datasets used to train the machine learning models are from the Substance Abuse and Mental Health Data Archive (SAMHDA) Client-Level data which is specific to facilities in the United States that produce reports about diagnoses and associated demographic information from the years 2013 to 2019. Each row of the dataset corresponds to a patient and their demographic information as well as their mental health diagnosis.')
    st.write("")
    st.write("The machine learning models will be trained on the year 2019 in accounting for computational limitations of processing the data from all years.")
    display()

def display_dataframe(file_path):
    df = pd.read_csv(file_path, index_col=0)
    st.dataframe(df)

def dataCols():
    st.subheader("Features")
    tab1, tab2, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab13, tab14 = st.tabs(["Age", "Disorders", "Education", "Employment","Ethnicity", "Gender", "Living Arrangement", "Marital Status", "Race", "SAP", "States", "Veteran"])
    with tab1:
        display_dataframe("CSV_files/age_key.csv")
    with tab2:
        display_dataframe("CSV_files/Disorders_Key.csv")
    with tab4:
        display_dataframe("CSV_files/educ_key.csv")
    with tab5:
        display_dataframe("CSV_files/employ_key.csv")
    with tab6:
        display_dataframe("CSV_files/ethnic_key.csv")
    with tab7:
        display_dataframe("CSV_files/gender_key.csv")
    with tab8:
        display_dataframe("CSV_files/livarag_key.csv")
    with tab9:
        display_dataframe("CSV_files/marstat_key.csv")
        #st.write("hello")
    with tab10:
        display_dataframe("CSV_files/race_key.csv")
    with tab11:
        display_dataframe("CSV_files/sap_key.csv")
    with tab13:
        display_dataframe("CSV_files/States_ID.csv")
    with tab14:
        display_dataframe("CSV_files/veteran_key.csv")

def dataDesc():
    st.title("Data Description")
    about()
    dataCols()

