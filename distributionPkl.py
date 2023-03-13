import pandas as pd
import streamlit as st
import joblib
import numpy as np

def dist():
    st.write("Distribution Null Model")
    # Load the model from the .sav file
    model = joblib.load('model.sav')

    # Prepare the input data for the model
    input_data = np.array([[1, 2, 3, 4]])  # replace with your own input data

    # Use the loaded model to make predictions
    output = model.predict(input_data)

    # Print the output
    print(output)