import pandas as pd
import streamlit as st

def report():
    custom_css = f"""
        <style>
            body {{
                background-color: #1B2437;
                color: #fff;
            }}

            .streamlit-container {{
                max-width: 800px;
                padding: 2rem 1rem;
                background-color: #2A3E60;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }}

            .streamlit-header {{
                font-size: 2rem;
                color: #fff;
                font-weight: bold;
                margin-bottom: 1.5rem;
            }}

            .streamlit-markdown {{
                font-size: 1.1rem;
                line-height: 1.6;
                color: #fff;
            }}

            .streamlit-expanderHeader {{
                font-size: 1.2rem;
                color: #fff;
                font-weight: bold;
            }}

            .streamlit-expanderContent {{
                font-size: 1.1rem;
                line-height: 1.6;
                color: #fff;
                margin-top: 1rem;
            }}

            .bullet-points {{
                margin-left: 20px;
            }}

            .bullet-points > * {{
                margin-top: 0.25rem;
            }}
        </style>
    """

    st.markdown(custom_css, unsafe_allow_html=True)

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
        st.write("Here are some bullet points:")
        st.markdown(bullet_points_str, unsafe_allow_html=True)

    st.subheader("")