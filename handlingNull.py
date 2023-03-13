import pandas as pd
import streamlit as st
from PIL import Image

def v3():
    st.header("Handling Missing Values")
    st.write("")
    st.write("To improve our F1 score, we decided to train 3 models that handle null values in different ways:")

    st.write("a. Removing Null Values")
    st.markdown(":red[F1 score: 0.469]")
    image = Image.open('images/nullsRemoved.jpg')
    st.image(image, caption='Decision Matrix and Feature Importance')

    st.write("")
    st.write("b. Replacing with Distribution Values")
    st.markdown(":red[F1 score: 0.502]")
    image = Image.open('images/nullsDistribution.jpg')
    st.image(image, caption='Decision Matrix and Feature Importance')

    st.write("")
    st.write("c. Replacing with Mode Values")
    st.markdown(":green[F1 score: 0.503]")
    image = Image.open('images/nullsMode.jpg')
    st.image(image, caption='Decision Matrix and Feature Importance')