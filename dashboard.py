import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Mental Health Disorders by Age, Education, Ethnicity, Race, and Gender")

df = pd.read_csv("data.csv")
df.set_index("AGE", inplace=True)

# Show a histogram of the number of mental health disorders per age cohort
st.bar_chart(df["MH1"].groupby(df.index).count())

# Show a bar chart of the number of mental health disorders per education level
st.bar_chart(df["EDUC"].value_counts())

# Show a countplot of the number of mental health disorders per ethnicity
st.write(sns.countplot(x="ETHNIC", data=df))

# Show a countplot of the number of mental health disorders per race
st.write(sns.countplot(x="RACE", data=df))

# Show a countplot of the number of mental health disorders per gender
st.write(sns.countplot(x="GENDER", data=df))

# Show a heatmap of the correlation between the different mental health disorders
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True)
st.pyplot()
