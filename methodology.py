import pandas as pd
import streamlit as st

def methMain():
    st.title("Data Cleaning")

    st.subheader("Categorical Encoding")
    st.write(" ")
    st.subheader("Filtering")
    columns = 'AGE, MH1, EDUC, ETHNIC, RACE, GENDER, MARSTAT, SAP, EMPLOY, LIVARAG, NUMMHS, STATEFIP'
    st.write("Columns included: " + columns)
    st.write("Columns dropped: VETERAN, DETNLF")
    st.caption("More columns dropped due to high level of nulls, irrelenvant info about the medical center, or redundancy")
    st.write("")

    st.subheader("Why Encode?")
    st.write(" ")
    st.write("In order to use continuous data as input to a classification model, it needs to be discretized or categorized. This is because classification models are designed to predict the probability of a given input belonging to each possible output category, but continuous data doesn't have distinct categories. Categorical encoding involves converting the continuous data into a set of discrete categories that can be used as input features in the classification model.")
    st.write("")

    st.subheader("Handling Null Values")
    st.write(" ")
    st.markdown("**To determine which approach to take in dealing with null values in the dataset, we trained our machine learning model on data with the null value rows *dropped* and a dataset with the null values replaced by the *mode*.**")
    st.write(" ")
    st.write("a. Dropping Null Values: dropped all rows containing a null value in any of the columns. Unfortunately created more imbalance and data loss")
    st.write("b. Replace with Mdoes: Replaced null values of each column with the mode of the specific column. Another flag column was created for each original column to signifiy if that row had been replaced artificially or not. This trains the model to identify a pattern of features that were modified")