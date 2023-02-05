import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Line Chart Example")
st.set_option('deprecation.showPyplotGlobalUse', False)

# load data
data = pd.DataFrame({
  'Year': [2015, 2016, 2017, 2018, 2019, 2020],
  'Sales': [200, 250, 300, 340, 380, 400]
})

# plot line chart
plt.plot(data['Year'], data['Sales'])

st.pyplot()