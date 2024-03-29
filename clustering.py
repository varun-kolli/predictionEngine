import pandas as pd
import streamlit as st
import altair as alt

from PIL import Image

#arrange in descending order
#make a green bar
#ml range of values
#creat table with range and optimal value

#class report trwo extra rows
#features decription top 3 b3


def clustMain():
    st.title("Clustering")

    st.write(" ")

    image = Image.open('images/kMeansGraph.png')
    st.image(image, use_column_width=True, clamp=True, caption='K-Means Clustering Example')

    st.write(" ")
    st.write("In building the classification model, we decided to use a K-means clustering algorithm to identify meaningful groups. To determine the optimal number of clusters, we tested multiple values of 'k' and calculated the silhouette score for each. Based on these results, we chose a model with 3 clusters as it had the highest silhouette score. This indicates that the 3-cluster model was able to identify natural groupings or clusters in the data that were meaningful and distinct from each other. By using clustering as a pre-processing step, we were able to reduce noise or variability in the data and improve the accuracy of our machine learning model. Furthermore, by only classifying for 3 targets instead of multiple targets, we were able to save computational resources, considering the size of the dataset.")

    clusters = {
        0: ["ADHD", "Anxiety", "Conduct disorder", "Delirium/dementia", "Oppositional defiant disorder", "Substance abuse disorder", "Personality disorders", "Pervasive developmental disorder", "Trauma-related disorders"],
        1: ["Bipolar", "Depression"],
        2: ["Schizophrenia/psychotic disorder"]
    }

    st.write("")
    st.subheader("Results: ")
    st.write("")

    source = pd.DataFrame({
        "Cluster": [0, 1, 2],
        "% of Total Cases": [46.8, 36.3, 16.9]
    })

    c = alt.Chart(source).mark_arc().encode(
        theta=alt.Theta('% of Total Cases', stack=True),
        color=alt.Color('Cluster:N',
                        scale=alt.Scale(domain=[0, 1, 2],
                        range=['red', 'blue', 'green'])
                       )
    )

    st.altair_chart(c, use_container_width=True)

    cluster_data = [
        {
            "name": "Cluster 0",
            "percentage": 46.8,
            "color": "red",
            "disorders": {
                "Trauma-related": 0.3508,
                "Anxiety": 0.2792,
                "ADHD": 0.1751,
                "Substance abuse": 0.0741,
                "Oppositional defiant": 0.0431,
                "Pervasive developmental": 0.023,
                "Personality": 0.0189,
                "Conduct": 0.034,
                "Delirium/dementia": 0.0067
            }
        },
        {
            "name": "Cluster 1",
            "percentage": 36.3,
            "color": "blue",
            "disorders": {
                "Depression": 0.712,
                "Bipolar": 0.2881
            }
        }
    ]

    # Convert the data to pandas DataFrame and normalize it
    cluster_dataframes = [
        pd.DataFrame(list(cluster["disorders"].items()), columns=["Disorder", "Percentage"])
        for cluster in cluster_data
    ]

    # Create an Altair bar chart for each cluster
    charts = [
        alt.Chart(df).mark_bar(color=cluster["color"]).encode(
            x="Percentage", y="Disorder", tooltip=["Disorder", "Percentage"]
        )
        for df, cluster in zip(cluster_dataframes, cluster_data)
    ]

    # Display the charts in Streamlit
    for chart, cluster in zip(charts, cluster_data):
        st.write(f"**{cluster['name']}: {cluster['percentage']}%**")
        st.altair_chart(chart, use_container_width=True)

    # Create a pie chart of the distribution of cluster percentages
    cluster_percentages_df = pd.DataFrame(cluster_data)[["name", "percentage", "color"]]

    st.write("**Cluster 2: 16.9%**")
    st.write("Schizophrenia/psychotic disorder is the only member of this cluster")



