import pandas as pd
import streamlit as st

def mlMain():
    st.title("Machine Learning")

    st.subheader("Flowchart")
    st.write(" ")
    img_path = "images/mlChart.png"
    img = open(img_path, "rb").read()
    st.image(img, use_column_width=True)
