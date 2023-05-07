import pandas as pd
import streamlit as st

def about():
    st.subheader("About the Data")

def display_dataframe(file_path):
    df = pd.read_csv(file_path, index_col=0)
    df = df.rename(columns={df.columns[0]: "", df.columns[1]: "Value"})
    st.dataframe(df)

def dataCols():
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

