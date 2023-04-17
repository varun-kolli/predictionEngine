import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

import joblib


def correlation_main():
    st.title("Correlation")
    st.write("After attempting a random forest model, found that training it would be computationally expensive with the current data organization. We then decided to train an unsupervised learning models to create clusters of patients with similar disorders to simply the target variable any model will interpret.")

    st.caption("Data selected is from 2019 where all null values were dropped")

    st.header("Clustering")

    df_corr = pd.read_csv("CSV_files/correlation_df.csv").reset_index(drop=True)
    kmeans = joblib.load('pkl_files/clustering_model.sav')

    #x = pd.get_dummies(df_corr.drop(columns = 'Disorder'), drop_first = True)
    #The values of 'X_pca[:, 0]' and 'X_pca[:, 1]' are obtained by multiplying the original data by the eigenvectors corresponding to the two largest eigenvalues of the covariance matrix.
    ###
    x = pd.get_dummies(df_corr.drop(columns=['Disorder', 'CLUSTER']), drop_first=True)
    cluster_labels = [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0]
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(x)

    # Create a scatter plot of the clusters
    fig, ax = plt.subplots()
    scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.title('Cluster Visualization (Principal Component Analysis) ')
    legend1 = ax.legend(*scatter.legend_elements(),
                        loc="upper right", title="Clusters")
    ax.add_artist(legend1)
    st.pyplot(fig)

    ###
    df = df_corr.copy()
    disorders_by_cluster = {}
    for i, label in enumerate(cluster_labels):
        if label not in disorders_by_cluster:
            disorders_by_cluster[label] = []
        disorders_by_cluster[label].append(df['Disorder'][i])

    # Print the disorders in each cluster
    for label, disorders in disorders_by_cluster.items():
        print(f"Cluster {label}: {disorders}")

    # Compute the mean correlation values for each cluster
    mean_corrs_by_cluster = {}
    for label in set(cluster_labels):
        cluster_x = x[cluster_labels == label]
        mean_corrs = np.mean(cluster_x, axis=0)
        mean_corrs_by_cluster[label] = mean_corrs

    # Create bar charts of the mean correlation values for each cluster
    fig, ax = plt.subplots(figsize=(10, 5))
    for label, mean_corrs in mean_corrs_by_cluster.items():
        ax.bar(x.columns, mean_corrs, label=f"Cluster {label}")
    ax.set_xlabel('Features')
    ax.set_ylabel('Mean correlation values')
    ax.set_title('Mean Correlation Values by Cluster')
    ax.legend()
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


