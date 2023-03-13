import pandas as pd
import streamlit as st
from PIL import Image


def t1():
    st.markdown(":red[F1 score: 0.469]")
    image = Image.open('images/nullsRemoved.jpg')
    st.image(image, caption='Decision Matrix and Feature Importance')

def t2():
    st.write("")
    st.markdown(":red[F1 score: 0.502]")
    image = Image.open('images/nullsDistribution.jpg')
    st.image(image, caption='Decision Matrix and Feature Importance')

def t3():
    st.write("")
    st.markdown(":green[F1 score: 0.503]")
    image = Image.open('images/nullsMode.jpg')
    st.image(image, caption='Decision Matrix and Feature Importance')

def v3():
    st.header("Handling Missing Values")
    st.write("")
    st.write("Current F1 Score: **0.493**")
    st.write("To improve our F1 score, we decided to train 3 models that handle null values in different ways:")
    st.write("a. Removing Null Values")
    st.write("b. Replacing with Distribution Values")
    st.write("c. Replacing with Mode Values")



    tab1, tab2, tab3 = st.tabs(["Removing", "Distribution", "Mode"])
    with tab1:
        t1()
    with tab2:
        t2()
    with tab3:
        t3()