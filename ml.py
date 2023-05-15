import pandas as pd
import streamlit as st
from PIL import Image


def mlMain():
    st.title("Machine Learning")

    st.subheader("Flowchart")
    st.write(" ")
    img_path = "images/mlChart.png"
    img = open(img_path, "rb").read()
    st.image(img, use_column_width=True)

    st.subheader("Model Information")
    st.write("Algorithm: **Decision Tree Classifier**")
    st.write("")
    st.write("A Decision Tree Classifier is a type of supervised learning algorithm used for classification problems. The model uses a tree-like model of decisions, where each internal node represents a test on an attribute, each branch represents the outcome of a test, and each leaf node represents a class label (a decision taken after computing all attributes). The paths from the root to the leaf represent classification rules. The algorithm selects the best attribute using an impurity measure such as Gini impurity or entropy, aiming to partition the data in a way that maximizes homogeneity among class labels in each subset. This model is favored in predictive analytics due to its ability to handle both categorical and numerical data, its interpretability, and its efficient computation.")
    st.write("")
    st.write("K-fold cross-validation is a resampling procedure used in machine learning to evaluate model performance. The method involves dividing the dataset into 'k' groups or folds of approximately equal size. The model is then trained on (k-1) folds while the remaining fold is used for testing, and this process is repeated k times, each time with a different fold used as the test set, to ensure a robust assessment of the model's performance. This Decision Tree Classifier model used: **k = 5**")
    st.write("")
    st.write("This model uses a 70% training and 30% test split, which means 70% of the data is used to train the model and the remaining 30% is used to evaluate its performance. This split is done to ensure that the model learns from a large portion of the data (the training set), and then its ability to generalize to new, unseen data is tested with the remaining portion (the test set).")

    st.write("")
    st.write("""
    In machine learning, a **hyperparameter** is a configuration that is external to the model and whose value cannot be estimated from the data. They are often used in processes to help estimate model parameters.

    Hyperparameter tuning is the process of choosing a set of optimal hyperparameters for a learning algorithm. The same kind of machine learning model can require different constraints, weights or learning rates to generalize different data patterns.

    In our Decision Tree Classifier, we tuned several hyperparameters to optimize its performance:

    1. **max_depth**: This is the maximum depth of the tree. Essentially, it's the maximum number of levels the tree can have. By limiting this, we can prevent overfitting by ensuring the tree doesn't become overly complex and fit to the noise in the training data.

    2. **min_samples_split**: This is the minimum number of samples required to split an internal node. Adjusting this parameter can help control overfitting, as a higher value would require more samples and hence prevent splitting for minor variations.

    3. **min_samples_leaf**: This is the minimum number of samples required to be at a leaf node. A split point at any depth will only be considered if it leaves at least min_samples_leaf training samples in each of the left and right branches. This helps in smoothing the model, especially in regression.
    """)


    st.write(" ")
    st.header("Model Training Infrastructure")
    st.write("For training our model, we utilized Amazon Web Services' (AWS) Elastic Compute Cloud (EC2) instance. EC2 is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.")

    st.subheader("Our AWS EC2 Configuration")
    st.markdown("""
    - **Instance Type**: c5.9xlarge
    - **vCPU**: 36 units
    - **Memory**: 72 GiB
    """)

    with st.expander("What does this mean?"):
        st.markdown("""
        - **Instance Type**: This refers to the type of EC2 instance we're using. Each instance type offers different compute, memory, and storage capabilities. We used `c5.9xlarge`, which is part of the compute-optimized instances, perfect for compute-intensive tasks.
        - **vCPU**: This stands for virtual central processing unit. A vCPU is a unit of capacity that you can use to compare and configure the amount of computing power of instances. We had 36 vCPUs, allowing us to handle multiple tasks quickly.
        - **Memory**: This is the physical memory or RAM (Random Access Memory) of the instance. We had 72 GiB (Gibibytes) of memory, which is important for storing and retrieving information quickly while our model is running.
        """)

    st.caption("This setup was made possible by a funding allocation of $750 from the California Polytechnic University, San Luis Obispo Industrial Engineering and Manufacturing Department")



