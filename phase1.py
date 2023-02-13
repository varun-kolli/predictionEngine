import streamlit as st
from PIL import Image

st.title("SAMDHA Mental Health Client Level Data")
st.markdown("Client level information containing patient demographic and diagnoses from 2004 - 2020")
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
    image = Image.open('images/dataNumerical2.png')
    st.image(image, use_column_width=True)

    st.markdown("Combined DETNLF and EMPLOY columns")
    st.markdown("Made all relevant columns categorical")
    st.markdown("Removed null values by three different methods;")
    st.markdown("Replace null values with the mode of each column")
    st.markdown("Replace null values with the distribution of that column")
    st.markdown("Remove all rows with null values")
    st.markdown("Ran three separate models (scores in powerpoint from last week)")
    st.markdown("All years, three most common disorders, subset of 200,000")
    st.markdown("Very good at predicting depression, very low at everything else")

def v3():
    st.header("Version 3: revisions to models")
    st.markdown("Used SMOTE to balance the dataset")
    st.markdown("Used balanced dataset as training set, unbalanced for testing set")
    st.markdown("Slightly improved performance")

def sideBar():
    # Define the tabs
    tab1_content = "Tab 1 Content"
    tab2_content = "Tab 2 Content"
    tab3_content = "Tab 3 Content"

    # Create a selection widget for the tabs
    tab_selector = st.sidebar.selectbox("Select a Tab", ["Tab 1", "Tab 2", "Tab 3"])

    # Show the selected tab content based on the selection
    if tab_selector == "Tab 1":
        st.sidebar.markdown(tab1_content)
    elif tab_selector == "Tab 2":
        st.sidebar.markdown(tab2_content)
    elif tab_selector == "Tab 3":
        st.sidebar.markdown(tab3_content)

def codeBooks():
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 =
        st.tabs(["Age", "Disorders", "Education", "Employment",
        "Ethnicity", "Gender", "Living Arrangement", "Marital Status", "Race", "SAP", "States", "Veteran"])

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
    with tab12:
        st.dataframe(pd.read_csv("CSV_files/marstat_key.csv"))
    with tab13:
        st.dataframe(pd.read_csv("CSV_files/States_ID.csv"))
    with tab14:
        st.dataframe(pd.read_csv("CSV_files/veteran_key.csv"))



def main():
    codeBooks()


if __name__ == '__main__':
    main()