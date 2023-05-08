import pandas as pd
import streamlit as st

def mlMain():
    st.title("Machine Learning")

    st.subheader("Flowchart")
    st.write(" ")
    img_path = "images/mlChart.png"
    img = open(img_path, "rb").read()
    st.image(img, use_column_width=True)\

    st.subheader("Model Information")
    st.write("Algorithm: Decision Tree Classifier")
    st.write("- K-fold Cross Validation: **k** = 5")
    st.write("- Training/Testing split: 70/30")
    st.write("- Additional hyperparameter tuning")

    st.write(" ")
    st.subheader("AWS EC2 Instance")
    st.write("- instance type: c5.9xlarge")
    st.write("- 36 vCPU")
    st.write("- 72 GiB memory")
    st.caption("$750 dollar funding allocation")

