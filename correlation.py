import pandas as pd
import streamlit as st
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
import joblib


def correlation_main():
    st.title("Correlation")
    st.write("After attempting a random forest model, found that training it would be computationally expensive with the current data organization. We then decided to train an unsupervised learning models to create clusters of patients with similar disorders to simply the target variable any model will interpret.")

    st.caption("Data selected is from 2019 where all null values were dropped")

    st.header("Clustering")

    df_corr = pd.read_csv("CSV_files/correlation_df.csv")
    x = pd.get_dummies(df_corr.drop(columns = 'Disorder'), drop_first = True)
    kmeans_model = joblib.load('pkl_files/clustering_model.sav')

    ###
    plt.figure(figsize=(10,8))
    sns.heatmap(corr_matrix, cmap='coolwarm', annot=True)
    plt.title('Correlation Matrix of Disorders in the Cluster')
    plt.show()

    ###

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

    #image = Image.open('images/clusters.png')
    #st.image(image)

    st.subheader("Decision Tree Implementation")
    st.write("Now that the clusters have been assigned, we will test the input features to predict for the mental health disorder group.")
    st.markdown("F1 Score: <span style='color:green'>0.62</span>",unsafe_allow_html=True)

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


