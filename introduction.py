import pandas as pd
import streamlit as st

def introduction():

    st.title("Predictive Analytics Framework for Mental Health Diagnoses")

    st.header('Project Goal')
    st.write('Develop a predictive analytics framework using data mining, statistical models, and machine learning that can identify risk factors in diagnosing mental health conditions and facilitate early detection of mental health issues.')

    # Background
    st.header('Background')
    st.write('Mental health issues are a growing problem in the United States, with 1 in 5 Americans experiencing a mental illness in a given year and over 50% being diagnosed with a mental disorder at some point in their lifetimes.')
    st.write('Current research addressing this problem is largely qualitative, but we will be using a data-driven analysis to study this problem.')
    st.write('The model will evaluate machine learning techniques to train our model such as Decision Tree Classifier, Random Forest Classifier, and AdaBoost Classifier.')

    # Data Sources
    st.header('Data Sources')
    st.write('We will leverage the datasets from the Substance Abuse and Mental Health Data Archive (SAMHDA) Client-Level data which is specific to facilities in the United States that produce reports about diagnoses and associated demographic information from the years 2013 to 2019.')

    # Methodology
    st.header('Methodology')
    st.write('In addition to using machine learning methodologies, we will also use Data Analytics techniques such as temporal and spatial data prevalence to study patterns of demographic factors over time and across different regions in the country.')
    st.write('Visualizing this into heat maps and time series plots will allow us to examine how the variables we study change over time and by region, as well as get a better insight into which areas of our data our model should focus on.')

    # Expected Outcomes
    st.header('Expected Outcomes')
    st.write('The resulting framework will implement a data-driven approach in utilizing temporal and spatial data analytics as well as machine learning techniques to identify risk factors as well as visualize the problem in the United States.')


