import pandas as pd
import streamlit as st

def report():

    st.markdown(
        f"""
        <div style='text-align:center'>
            <h1>Model Tracker</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header("Initial Decision Tree")

    st.write("First Attempt with the partially cleaned SAMDHA data resulted in a low F1 score of <span style='color:red'>0.493</span>.", unsafe_allow_html=True)
    st.caption("5 Fold Cross Validation       Training Size: 70%      Test Size: 30%")

    st.subheader("Data Processing")

    bullet_points = [
        "Filtering disorders to **Bipolar, Trauma, Depression**",
        "3 different approaches to handling null values: Remove Null Values, Replace with Distribution, Replace with Mode",
        "Converted relevant input column data to categorical variables"
    ]

    st.markdown("""
        <style>
        .bullet-points { margin-left: 20px; }
        .bullet-points > * { margin-top: 0.25rem; }
        </style>
    """, unsafe_allow_html=True)

    # Concatenate the bullet points into a single string
    bullet_points_str = ""
    for bullet_point in bullet_points:
        bullet_points_str += f"<div class='bullet-points'>• {bullet_point}</div>"

    # Display the bullet points using a single st.markdown call
    with st.container():
        st.write("Methods:")
        st.markdown(bullet_points_str, unsafe_allow_html=True)

    st.subheader("Results")

    with st.container():
        col1, col2, col3 = st.beta_columns(3)


