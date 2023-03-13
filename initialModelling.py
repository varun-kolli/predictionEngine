import pandas as pd
import streamlit as st

def v1():
    data = {
       'Hyperparameters': ['Initial', 'Improved'],
       'F1-Score Weighted': [0.493, 0.493],
       'Max Depth': [60, 45],
       'Min Samples Leaf': [45, 56],
       'Min Samples Split': [10, 2],
       'Fits': [135, 500]
    }

    # Create DataFrame
    df = pd.DataFrame(data).reset_index

    # Define cross-validation information
    n_folds = 5
    total_fits = 135 + 500
    folds_text = f'{n_folds}-fold cross-validation'
    fits_text = f'{total_fits} fits'

    # Define container width for table and text
    container_width = st.container().width

    # Display information
    st.title('Decision Tree Model Hyperparameter Tuning Report')
    with st.container():
        st.header('Methodology')
        st.write('In this section, we explore the hyperparameter tuning process for a decision tree model using the GridSearchCV function from scikit-learn library. The data used in this report contains information about mental health diagnoses from multiple years, and we filter the data to create a subset of interest.')
        st.write(f'The hyperparameters we tune are the maximum depth of the tree, the minimum number of samples required to split an internal node, and the minimum number of samples required to be at a leaf node. We use {folds_text} and the F1-score weighted metric for evaluation.')
        st.subheader('Grid Search Cross Validation Model Performance')
        st.write(df)
        st.caption("Training Size", "70%")
        st.caption("Testing Size", "30%")
