import pandas as pd
import streamlit as st

def methMain():
    st.title("Methodology")

    st.header("My Page")

    # Create a link to a specific location on the page
    st.markdown("<a id='section1'></a>", unsafe_allow_html=True)

    # Add a button to navigate to the section
    if st.button("Go to Section 1"):
        st.experimental_set_query_params(section="1")

    # Add some content
    st.write("This is the main content of the page.")

    # Add a section to navigate to
    st.header("Section 1")
    st.write("This is the content of Section 1.")

    # Create a link back to the top of the page
    st.markdown("<a id='top'></a>", unsafe_allow_html=True)

    # Add a button to navigate back to the top
    if st.button("Back to top"):
        st.experimental_set_query_params(section=None)