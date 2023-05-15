import pandas as pd
import streamlit as st

def clustMain():
    st.title("Clustering")

    st.write(" ")
    st.write("In building the classification model, we decided to use a K-means clustering algorithm to identify meaningful groups. To determine the optimal number of clusters, we tested multiple values of 'k' and calculated the silhouette score for each. Based on these results, we chose a model with 3 clusters as it had the highest silhouette score. This indicates that the 3-cluster model was able to identify natural groupings or clusters in the data that were meaningful and distinct from each other. By using clustering as a pre-processing step, we were able to reduce noise or variability in the data and improve the accuracy of our machine learning model. Furthermore, by only classifying for 3 targets instead of multiple targets, we were able to save computational resources, considering the size of the dataset.")

    clusters = {
        0: ["ADHD", "Anxiety", "Conduct disorder", "Delirium/dementia", "Oppositional defiant disorder", "Substance abuse disorder", "Personality disorders", "Pervasive developmental disorder", "Trauma-related disorders"],
        1: ["Bipolar", "Depression"],
        2: ["Schizophrenia/psychotic disorder"]
    }

    st.write("")
    image = Image.open('kMeansGraph.png')
    st.image(image, use_column_width=True, clamp=True, caption='K-Means Clustering Example')

    st.caption(" 'Cluster #' % represents proportion of total cases")
    st.caption(" 'Disorder' % represents proportion of cases within cluster")
    col1, col2, col3 = st.columns(3)
    st.write(" ")
    st.write(" ")

    st.write(" ")


    # Display the disorders in cluster 0 in the first column
    with col1:
        st.write("**Cluster 0: 46.8%**")
        # Cluster 0 dictionary
        cluster_0_dict = {
                "Trauma-related": 0.3508,
                "Anxiety": 0.2792,
                "ADHD": 0.1751,
                "Substance abuse ": 0.0741,
                "Oppositional defiant": 0.0431,
                "Pervasive developmental": 0.023,
                "Personality": 0.0189,
                "Conduct ": 0.034,
                "Delirium/dementia": 0.0067
        }
        for disorder, percentage in cluster_0_dict.items():
            st.write(f"- {disorder}: {percentage:.2%}")


    # Display the disorders in cluster 1 in the second column
    with col2:
        st.write("**Cluster 1: 36.3%**")
        cluster_1_dict = {
            "Depression": 0.712,
            "Bipolar": 0.2881
        }
        for disorder, percentage in cluster_1_dict.items():
                st.write(f"- {disorder}: {percentage:.2%}")

    # Display the disorders in cluster 2 in the third column
    with col3:
        st.write("**Cluster 2: 11.7%**")
        st.write("- " + "\n- ".join(clusters[2]))
