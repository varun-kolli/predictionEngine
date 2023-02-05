import streamlit as st
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

@st.cache
def data():
    return pd.read_csv('data.csv')

@st.write
def display_data():
    data_df = data()
    st.write(data_df)

#display_data()