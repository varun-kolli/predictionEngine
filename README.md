# Prediction Engine

Hosted at [https://varun-kolli-predictionengine-streamlit](https://varun-kolli-predictionengine-streamlit.com).

## Table of Contents
1. [About The Project](#about-the-project)
2. [Built With](#built-with)
3. [Getting Started](#getting-started)
4. [Contributors](#contributors)
5. [Contact](#contact)

## About The Project
Prediction Engine is a Streamlit application that allows users to interact with the decision tree classifier machine learning model. The application displays information about the creation of the model and provides a prediction dashboard where users can input data and see the predicted output.

## Built With
- **Streamlit:** The web application framework used.
- **Pandas:** Used for data manipulation and analysis.
- **Altair:** A statistical visualization library.
- **Scikit Learn:** Machine learning library.

# Getting Started

This guide will assist you in setting up a local development environment for this project.

## Prerequisites
You should have the following tools installed on your system before you proceed:
- [Python 3.7 or later](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- [pip](https://pip.pypa.io/en/stable/installation/)

## Instructions
Follow the steps below to get the project up and running on your machine.

**Step 1: Clone the repository**
Use `git clone` to download a copy of the repository. Run the following command in your terminal:

```bash
git clone https://github.com/varun-kolli/predictionEngine.git
```

# Step 2: Navigate into the project directory
```bash
cd predictionEngine
```

# Step 3: Set up a virtual environment
```bash
python3 -m venv env
```

# Step 4: Activate the virtual environment
# For Unix or MacOS:
```bash
source env/bin/activate
```

# For Windows:
```bash
env\Scripts\activate
```

# Step 5: Install the necessary packages
```bash
pip install streamlit pandas altair scikit-learn
```

# Step 6: Run Streamlit to start the application
```bash
streamlit run stremlit_app.py
```

## Code Structure
The main page of the application is `streamlit_app.py`. This serves as the launching point of the application. The sidebar of the application houses links to different functionalities, each of which corresponds to a different file in the codebase. 

The "Predictive Dashboard" functionality is handled by a separate file that contains a pickled (serialized) SciKit Learn Decision Tree Classifier. This file is read in when the "Predictive Dashboard" link is clicked, and the model contained within is used to make predictions based on user input.

## Contributors
- **Project Advisor:** Tali Freed
- **Project Sponsor:** Punnet Agarwal
- **Team Members:** Varun Kolli, Eliza Badiozamani, Kerry Fung, Om Kumar

## Contact
For any inquiries or concerns, please open an issue in this repository.
