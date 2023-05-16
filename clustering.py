import pandas as pd
import streamlit as st
import altair as alt

from PIL import Image


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
    pie_chart = (
        alt.Chart(cluster_percentages_df)
        .mark_arc(innerRadius=50, outerRadius=100, cornerRadius=5)
        .encode(
            alt.Theta(
                "percentage",
                stack=True,
                scale=alt.Scale(domain=[0, 100]),
                legend=None,
            ),
            color=alt.Color(
                "color:N",
                scale=None,
                legend=None,
            ),
            tooltip=["name", "percentage"],
        )
        .properties(width=300, height=300)
    )

    st.write("**Pie chart of cluster distribution**")
    st.altair_chart(pie_chart, use_container_width=True)

