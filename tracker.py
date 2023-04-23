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

    st.subheader("Initial Decision Tree")

    st.write("First Attempt with the partially cleaned SAMDHA data resulted in a low F1 score of <span style='color:red'>0.493</span>.", unsafe_allow_html=True)
    st.caption("5 Fold Cross Validation       Training Size: 70%      Test Size: 30%")

    st.header("Data Processing")

    st.write("Methods:")
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

    # Display the bullet points using a div element with the 'bullet-points' class
    with st.container():
        st.write("Here are some bullet points:")
        with st.markdown(""):
            for bullet_point in bullet_points:
                st.markdown(f"<div class='bullet-points'>• {bullet_point}</div>", unsafe_allow_html=True)

    st.subheader("")