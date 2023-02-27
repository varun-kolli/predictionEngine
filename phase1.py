import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt
from streamlit import set_page_config


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
    st.write('The resulting framework will implement a data-driven approach in utilizing temporal and spatial data analytics as well as machine learning techniques to identify risk factors as well as visualize the problem in the United States. Using Streamlit functions and code such as st.header, st.write statements display this in a clean interface.')


def v1():
    data = {
       'Hyperparameters': ['Initial', 'Improved'],
       'F1-Score Weighted': [0.493, 0.493],
       'Max Depth': [60, 45],
       'Min Samples Leaf': [45, 56],
       'Min Samples Split': [10, 2],
       'Fits': [135, 500]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Define cross-validation information
    n_folds = 5
    total_fits = 135 + 500
    folds_text = f'{n_folds}-fold cross-validation'
    fits_text = f'{total_fits} fits'

    # Define container width for table and text
    container_width = st.container().width

    # Display information
    st.title('Decision Tree Model Hyperparameter Tuning Report')
    with st.container():
        st.header('Methodology')
        st.write('In this section, we explore the hyperparameter tuning process for a decision tree model using the GridSearchCV function from scikit-learn library. The data used in this report contains information about mental health diagnoses from multiple years, and we filter the data to create a subset of interest.')
        st.write(f'The hyperparameters we tune are the maximum depth of the tree, the minimum number of samples required to split an internal node, and the minimum number of samples required to be at a leaf node. We use {folds_text} and the F1-score weighted metric for evaluation.')
        st.subheader('Grid Search Cross Validation Model Performance')
        st.write(df)
        col1, col2 = st.columns(2)
        col1.metric("Training Size", "70%")
        col2.metric("Testing Size", "30%")


def v2():
    st.header("Version 2: Data cleaning")

    st.subheader("Methodology")

    st.text("1. Convert Relevant Columns to Categorical Variables")
    codeBooks()
    st.text("2. Combined DETNLF and EMPLOY columns")

    with st.expander("Resultant Dataframe"):
        image = Image.open('images/dataNumerical2.png')
        st.image(image, use_column_width=True)

    st.text("3. Handling Missing Values")


    st.markdown("Removed null values by three different methods;")
    st.markdown("Replace null values with the mode of each column")
    st.markdown("Replace null values with the distribution of that column")
    st.markdown("Remove all rows with null values")

    with st.container():
        data = [("Removed Null Values", 0.469), ("Mode Replacing Nulls", 0.503), ("Distribution Replacing Nulls", 0.502)]
        df = pd.DataFrame(data, columns=["Method", "F1 Score"])
        df = df.reset_index(drop=True)
        bar = alt.Chart(df).mark_bar(size=15).encode(
            x=alt.X("Method:O", title=None, sort=alt.SortField(field="F1 Score", order="descending"), axis=alt.Axis(labelAngle=90)),
            y=alt.Y("F1 Score:Q", title="F1 Score", scale=alt.Scale(domain=[0.4, 0.5]), axis=alt.Axis(grid=False)),
            color=alt.Color("Method", legend=None),
            opacity=alt.value(0.7),
        ).properties(
            width=alt.Step(50),
            height=alt.Step(80),
        )

        st.altair_chart(bar, use_container_width=True)


        col1, col2, col3 = st.columns(3)
        col1.metric("Removed Null Values", "0.469", "-0.33")
        col2.metric("Mode Replacing Nulls", "0.503")
        col3.metric("Distribution Replacing Nulls", "0.502", "-0.01")

    st.markdown("Ran three separate models (scores in powerpoint from last week)")
    st.markdown("All years, three most common disorders, subset of 200,000")
    st.markdown("Very good at predicting depression, very low at everything else")

def v3():
    st.header("Version 3: revisions to models")
    st.markdown("Used SMOTE to balance the dataset")
    st.markdown("Used balanced dataset as training set, unbalanced for testing set")
    st.markdown("Slightly improved performance")

def sideBar():
    tabs = ["Introduction", "Initial Modelling", "Decision Tree Improvements", "Phase 3"]
    tab_selector = st.sidebar.selectbox("Navigate", tabs)

    if tab_selector == "Introduction":
        introduction()
    elif tab_selector == "Initial Modelling":
        v1()
    elif tab_selector == "Decision Tree Improvements":
        v2()
    elif tab_selector == "Phase 3":
        v3()

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


def main():
    #with open('my_custom_theme.css') as f:
        #st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

    sideBar()

if __name__ == '__main__':
    main()