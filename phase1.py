import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt


def introduction():
    st.title("SAMDHA Mental Health Client Level Data")
    st.markdown("Client level information containing patient demographic and diagnoses from 2004 - 2020")
    with st.expander("View Dataframe"):
        image = Image.open('images/dataNumerical.png')
        st.image(image, use_column_width=True)

def v1():
    st.header("Version 1: Basic Decision Tree")
    st.markdown("Imported data and attempted a basic decision tree model")
    st.markdown("Excluded unnecessary or skewing data columns")
    st.markdown("Subset of 100,000 rows, year 2013, only three most common disorders")
    st.markdown("F1 weighted score of around 0.3")

def v2():
    st.header("Version 2: Data cleaning + More Decision Trees")
    st.markdown("Due to lack of categorical variables, null values, and overlapping rows, more cleanup needed to happen to improve performance")

    with st.expander("View Dataframe"):
        image = Image.open('images/dataNumerical2.png')
        st.image(image, use_column_width=True)

    st.markdown("Combined DETNLF and EMPLOY columns")
    st.markdown("Converted all relevant columns to categorical variables")
    codeBooks()

    st.markdown("Removed null values by three different methods;")
    st.markdown("Replace null values with the mode of each column")
    st.markdown("Replace null values with the distribution of that column")
    st.markdown("Remove all rows with null values")

    with st.container():
        data = [("Removed Null Values", 0.469), ("Mode Replacing Nulls", 0.503), ("Distribution Replacing Nulls", 0.502)]
        df = pd.DataFrame(data, columns=["Method", "F1 Score"])
        df = df.reset_index(drop=True)
        bar = alt.Chart(df).mark_bar().encode(
            x = alt.X("Method:O", title = None, sort = alt.SortField(field = "F1 Score", order = "descending")),
            y = alt.Y("F1 Score:Q", title = "F1 Score"),
            color = alt.Color("Method", legend=None)
        )

        st.altair_chart(bar)


    st.markdown("Ran three separate models (scores in powerpoint from last week)")
    st.markdown("All years, three most common disorders, subset of 200,000")
    st.markdown("Very good at predicting depression, very low at everything else")

def v3():
    st.header("Version 3: revisions to models")
    st.markdown("Used SMOTE to balance the dataset")
    st.markdown("Used balanced dataset as training set, unbalanced for testing set")
    st.markdown("Slightly improved performance")

def sideBar():
    tabs = ["Introduction", "Phase 1", "Phase 2", "Phase 3"]
    tab_selector = st.sidebar.selectbox("Select a Tab", ["Introduction", "Phase 1", "Phase 2", "Phase 3"])

    if tab_selector == "Introduction":
        introduction()
    elif tab_selector == "Phase 1":
        v1()
    elif tab_selector == "Phase 2":
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
    sideBar()

if __name__ == '__main__':
    main()