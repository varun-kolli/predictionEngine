import streamlit as st

st.title("SAMDHA Mental Health Client Level Data")
st.markdown("Client level information containing patient demographic and diagnoses from 2004 - 2020")

st.header("Version 1: Basic Decision Tree")
st.markdown("Imported data and attempted a basic decision tree model")
st.markdown("Excluded unnecessary or skewing data columns")
st.markdown("Subset of 100,000 rows, year 2013, only three most common disorders")
st.markdown("F1 weighted score of around 0.3")

st.header("Version 2: Data cleaning + More Decision Trees")
st.markdown("Due to lack of categorical variables, null values, and overlapping rows, more cleanup needed to happen to improve performance")
st.markdown("Combined DETNLF and EMPLOY columns")
st.markdown("Made all relevant columns categorical")
st.markdown("Removed null values by three different methods;")
st.markdown("Replace null values with the mode of each column")
st.markdown("Replace null values with the distribution of that column")
st.markdown("Remove all rows with null values")
st.markdown("Ran three separate models (scores in powerpoint from last week)")
st.markdown("All years, three most common disorders, subset of 200,000")
st.markdown("Very good at predicting depression, very low at everything else")

st.header("Version 3: revisions to models")
st.markdown("Used SMOTE to balance the dataset")
st.markdown("Used balanced dataset as training set, unbalanced for testing set")
st.markdown("Slightly improved performance")
