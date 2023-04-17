import pandas as pd
import streamlit as st
from PIL import Image

def correlation_main():
    st.title("Correlation")
    st.write("After attempting a random forest model, found that training it would be computationally expensive with the current data organization. We then decided to train an unsupervised learning models to create clusters of patients with similar disorders to simply the target variable any model will interpret.")

    st.caption("Data selected is from 2019 where all null values were dropped")

    st.markdown("Highest silhouette score: <span style='color:green'>0.66</span> with 3 clusters", unsafe_allow_html=True)
