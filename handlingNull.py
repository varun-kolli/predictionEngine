import pandas as pd
import streamlit as st
from PIL import Image


def t1():
    image = Image.open('images/nullsRemoved.jpg')
    st.image(image)

def t2():
    image = Image.open('images/nullsDistribution.jpg')
    st.image(image)

def t3():
    image = Image.open('images/nullsMode.jpg')
    st.image(image)


def v3():
    st.header("Handling Missing Values")
    st.write("")
    st.write("Current F1 Score: **0.493**")
    st.write("To improve our F1 score, we decided to train 3 models that handle null values in different ways:")
    data = {'methods': ['Removing Null Values', 'Replacing with Distribution Values', 'Replacing with Mode Values'],
            'F1 score': [0.469, 0.502, 0.503]}

    df = pd.DataFrame(data)
    st.write(df)

    st.subheader("Decision Matrix and Feature Importance")

    tab1, tab2, tab3 = st.tabs(["Removing", "Distribution", "Mode"])
    with tab1:
        t1()
    with tab2:
        t2()
    with tab3:
        t3()