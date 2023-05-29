import pandas as pd
import streamlit as st
import altair as alt


def resultMain():
    st.title("Results")

    cols = st.columns(2)

    with cols[0]:
        st.subheader("Classification Report")

        data = {
            'precision': [0.63, 0.62, 0.54],
            'recall': [0.66, 0.61, 0.02],
            'f1-score': [0.64, 0.62, 0.04],
            'support': [204486, 194977, 6017]
        }

        df = pd.DataFrame(data)

        st.dataframe(df)

    with cols[1]:
        st.subheader("Confusion Matrix")

        img_path = "images/cf_mat.png"
        img = open(img_path, "rb").read()
        st.image(img, use_column_width=True)


    st.subheader("Feature Importance")
    data = {
            "Feature": ["State", "Age", "Marital Status", "Sex", "Education", "Employment Status", "#Mental Health Disorders", "Substance Abuse", "Living Arrangement", "Race", "Ethnicity"],
            "Importance": [0.247583, 0.239926, 0.14362, 0.090526, 0.079785, 0.07844, 0.037469, 0.033961, 0.021968, 0.021573, 0.00515]
        }

    # Convert the data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Sort the DataFrame by importance in descending order
    df = df.sort_values(by="Importance", ascending=False)

    # Create the bar chart using Altair
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Feature", sort=alt.EncodingSortField(field="Importance", op="sum", order="descending")),
        y="Importance",
        tooltip=["Feature", "Importance"]
    ).properties(
        width=700,
        height=400
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)

    st.write(" ")

    st.subheader("Decision Tree")

    if 'rest' not in st.session_state:
        st.session_state.rest = 0

    def set_stage():
        resultMain()


    img_path = "images/modes_decision_tree-1.png"
    img = open(img_path, "rb").read()
    st.image(img, use_column_width=True)
    with open("images/modes_decision_tree-1.png", "rb") as file:
        btn = st.download_button(
            label="Download Image",
            data=file,
            file_name="modes_decision_tree-1.png",
            mime="image/png", on_click = set_stage
        )

