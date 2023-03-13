import pandas as pd
import streamlit as st
from PIL import Image

def v2():
    st.title("Data Cleaning")
    st.header("Methodology")

    st.subheader("1. Filtering")
    st.write("Focusing on 3 most common disorders: **Bipolar, Trauma, Depression**")

    st.subheader("2. Convert Relevant Columns to Categorical Variables")
    codeBooks()

    st.subheader("3. Combined DETNLF and EMPLOY columns")
    image = Image.open('images/dataNumerical2.png')
    st.image(image, use_column_width=True)

def codeBooks():
    tab1, tab2, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab13, tab14 = st.tabs(["Age", "Disorders", "Education", "Employment","Ethnicity", "Gender", "Living Arrangement", "Marital Status", "Race", "SAP", "States", "Veteran"])
    with tab1:
        st.dataframe(pd.read_csv("CSV_files/age_key.csv"))
    with tab2:
        st.dataframe(pd.read_csv("CSV_files/Disorders_Key.csv"))
    with tab4:
        st.dataframe(pd.read_csv("CSV_files/educ_key.csv"))
    with tab5:
        st.dataframe(pd.read_csv("CSV_files/employ_key.csv"))
    with tab6:
        st.dataframe(pd.read_csv("CSV_files/ethnic_key.csv"))
    with tab7:
        st.dataframe(pd.read_csv("CSV_files/gender_key.csv"))
    with tab8:
        st.dataframe(pd.read_csv("CSV_files/livarag_key.csv"))
    with tab9:
        st.dataframe(pd.read_csv("CSV_files/marstat_key.csv"))
    with tab10:
        st.dataframe(pd.read_csv("CSV_files/race_key.csv"))
    with tab11:
        st.dataframe(pd.read_csv("CSV_files/sap_key.csv"))
    with tab13:
        st.dataframe(pd.read_csv("CSV_files/States_ID.csv"))
    with tab14:
        st.dataframe(pd.read_csv("CSV_files/veteran_key.csv"))


