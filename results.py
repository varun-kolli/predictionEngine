import pandas as pd
import streamlit as st

def resultMain():
    st.title("Results")

    st.subheader("Classification Report")

    data = {
        'precision': [0.63, 0.62, 0.54],
        'recall': [0.66, 0.61, 0.02],
        'f1-score': [0.64, 0.62, 0.04],
        'support': [204486, 194977, 6017]
    }

    df = pd.DataFrame(data)

    st.dataframe(df)

    st.subheader("Confusion Matrix")
    image = Image.open('images/cf_mat.png')
    st.image(image)

    st.subheader("Feature Importance")
    data = {
        "Feature": ["STATEFIP", "AGE", "MARSTAT", "GENDER", "EDUC", "EMPLOY", "NUMMHS", "SAP", "LIVARAG", "RACE", "ETHNIC"],
        "Importance": [0.247583, 0.239926, 0.14362, 0.090526, 0.079785, 0.07844, 0.037469, 0.033961, 0.021968, 0.021573, 0.00515]
    }

    # create a Pandas dataframe from the dictionary
    df = pd.DataFrame(data)

    # create a Streamlit table from the dataframe
    st.table(df)

    st.write(" ")

    st.subheader("Decision Tree")
    image = Image.open('images/modes_decision_tree-1.png')
    st.image(image)
