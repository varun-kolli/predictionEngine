import pandas as pd
import streamlit as st

def v3():
    st.subheader("3. Handling Missing Values")
    st.write("")
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