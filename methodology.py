import pandas as pd
import streamlit as st

def methMain():
    st.title("Data Cleaning")
    st.write(" ")
    st.header("Categorical Encoding")
    st.write("")
    columns_included = "Age, Mental Health Disorder History, Education, Ethnicity, Race, Sex, Marital Status, Substance Abuse Problem, Employment, Living Arrangement, Mental Health History, State"

    #columns_included = 'AGE, MH1, EDUC, ETHNIC, RACE, GENDER, MARSTAT, SAP, EMPLOY, LIVARAG, NUMMHS, STATEFIP'
    columns_dropped = 'Veteran Status, Miscellaneous Descriptors of Hospital'

    col1, col2 = st.columns(2)

    with col1:
        st.write('**Included**')
        st.write('' + columns_included)

    with col2:
        st.write('**Dropped**')
        st.write('' + columns_dropped)
    st.caption("        More columns dropped due to high level of nulls, irrelenvant info about the medical center, or redundancy")
    st.write("")

    st.subheader("Why Encode?")
    st.write(" ")
    st.write("      In order to use continuous data as input to a classification model, it needs to be discretized or categorized. This is because classification models are designed to predict the probability of a given input belonging to each possible output category, but continuous data doesn't have distinct categories. Categorical encoding involves converting the continuous data into a set of discrete categories that can be used as input features in the classification model.")
    st.write("")

    st.header("Handling Null Values")
    st.write(" ")
    st.markdown("To determine which approach to take in dealing with null values in the dataset, we trained our machine learning model on data with the null value rows **dropped** and a dataset with the null values replaced by the **mode**.")
    st.write(" ")
    st.subheader("  Methods: ")
    st.write("  ")
    st.write("      i. Dropping Null Values: dropped all rows containing a null value in any of the columns. Unfortunately created more imbalance and data loss")
    st.write("      ii. Replace with Modes: Replaced null values of each column with the mode of the specific column. Another flag column was created for each original column to signifiy if that row had been replaced artificially or not. This trains the model to identify a pattern of features that were modified")