import pandas as pd
import streamlit as st

def clustMain():
    st.title("Clustering")

    st.write(" ")
    st.write("In building the classification model, we decided to use a K-means clustering algorithm to identify meaningful groups. To determine the optimal number of clusters, we tested multiple values of 'k' and calculated the silhouette score for each. Based on these results, we chose a model with 3 clusters as it had the highest silhouette score. This indicates that the 3-cluster model was able to identify natural groupings or clusters in the data that were meaningful and distinct from each other. By using clustering as a pre-processing step, we were able to reduce noise or variability in the data and improve the accuracy of our machine learning model. Furthermore, by only classifying for 3 targets instead of multiple targets, we were able to save computational resources, considering the size of the dataset.")

    clusters_df = pd.DataFrame({
        'Cluster': ['0', '1', '2'],
        'Disorders': ['ADHD, Anxiety, Conduct disorder, Delirium/dementia, Oppositional defiant disorder, Substance abuse disorder, Personality disorders, Pervasive developmental disorder, Trauma-related disorders', 'Bipolar, Depression', 'Schizophrenia/psychotic disorder'],
        'Total Cases': [2527901, 742327, 669384],
        '% of Total Cases': [61.6, 18.1, 16.4]
    })

    disorders_df_0 = pd.DataFrame({
        'Disorder': ['ADHD', 'Anxiety', 'Conduct disorder', 'Delirium/dementia', 'Oppositional defiant disorder', 'Substance abuse disorder', 'Personality disorders', 'Pervasive developmental disorder', 'Trauma-related disorders'],
        'Total Cases': [443138, 707078, 86239, 16873, 109143, 187839, 47905, 58396, 887413],
        '% of Cluster Total': [17.6, 28.0, 3.4, 0.7, 43.5, 75.9, 100.0, 100.0, 100.0]
    })

    disorders_df_1 = pd.DataFrame({
        'Disorder': ['Bipolar', 'Depression'],
        'Total Cases': [595334, 1471993],
        '% of Cluster Total': [80.0, 20.0]
    })

    disorders_df_2 = pd.DataFrame({
        'Disorder': ['Schizophrenia/psychotic disorder'],
        'Total Cases': [669384],
        '% of Cluster Total': [100.0]
    })

    # Display the data frames in separate columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(clusters_df)

    with col2:
        st.write(disorders_df_0)

    with col3:
        st.write(disorders_df_1)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.write("")

    with col5:
        st.write(disorders_df_2)

    with col6:
        st.write("")
