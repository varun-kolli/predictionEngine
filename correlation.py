import pandas as pd
import streamlit as st
from PIL import Image

def correlation_main():
    st.title("Correlation")
    st.write("After attempting a random forest model, found that training it would be computationally expensive with the current data organization. We then decided to train an unsupervised learning models to create clusters of patients with similar disorders to simply the target variable any model will interpret.")

    st.caption("Data selected is from 2019 where all null values were dropped")

    st.markdown("Highest silhouette score: <span style='color:green'>0.66</span> with 3 clusters", unsafe_allow_html=True)

    # Create data
    data = {'N Clusters': [2, 3, 4, 5, 6, 7],
            'Silhouette Score': [0.355, 0.243, 0.209, 0.212, 0.265, 0.295]}
    df = pd.DataFrame(data)

    # Find row with highest score
    max_score_row = df.loc[df['Silhouette Score'].idxmax()]

    # Create expander
    with st.expander("New Results"):
        # Create table with highlighted row
        st.write(df.style.apply(lambda x: ['background-color: lightgreen' if x.equals(max_score_row) else '' for i in x], axis=1))

    st.header("Clusters")
    image = Image.open('images/clusters.png')
    st.image(image)

    st.header("Decision Tree Implementation")
    st.write("Now that the clusters have been assigned, we will test the input features to predict for the mental health disorder group.")
    st.markdown("F1 Score: <span style='color:green'>0.62</span>")

    image = Image.open('images/clf_report.png')
    st.image(image)

    st.header("Confusion Matrix")
    image = Image.open('images/cf_mat.png')
    st.image(image)


