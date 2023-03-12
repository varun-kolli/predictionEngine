import pandas as pd
import streamlit as st
from phase1 import *

# Read in the CSV file
df = pd.read_csv("CSV_files/data.csv")

# Write out the first 10 rows of the DataFrame
st.write("First 10 rows:", df.head(10))
