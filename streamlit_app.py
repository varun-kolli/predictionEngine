import pandas as pd
import streamlit as st
from phase1 import introduction
from sidebar import sideBar

selection = sideBar()

st.write(selection)