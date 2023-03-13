import pandas as pd
import streamlit as st


def v4():
    st.title("Data Balancing")
    st.subheader("SMOTE Balancing Using Dataset")
    st.write("Findings: ")
    st.markdown(" - Balanced dataset as training set")
    st.markdown(" - Unbalanced for testing set")
    st.write("F1 score: **0.55**")

    st.subheader("Decision Matrix and Classification Report")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("images/smoteMatrix.jpg", use_column_width=True)

        with col2:
            st.image("images/smoteClassification.jpg", use_column_width=True)

    st.subheader("Prototype Correlation Matrix")
    st.image("images/smoteCorr.jpg", use_column_width=True)