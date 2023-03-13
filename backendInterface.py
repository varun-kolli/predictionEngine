import pandas as pd
import streamlit as st


#input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
def convertAge(age):
    # define subgroups with corresponding age ranges
    subgroups = {
        '0-11': range(0, 12),
        '12-14': range(12, 15),
        '15-17': range(15, 18),
        '18-20': range(18, 21),
        '21-24': range(21, 25),
        '25-29': range(25, 30),
        '30-34': range(30, 35),
        '35-39': range(35, 40),
        '40-44': range(40, 45),
        '45-49': range(45, 50),
        '50-54': range(50, 55),
        '55-59': range(55, 60),
        '60-64': range(60, 65),
        '65 up': range(65, 150)  # use a large upper bound to include all ages 65 and above
    }

    # classify the age variable
    for group, age_range in subgroups.items():
        if age in age_range:
            age_group = group
            break
    else:
        age_group = '-9'

    # store the age group as a string variable
    age_group_str = age_group.replace(' ', '')  # remove any spaces

    return age_group_str


def interface():
    st.title("Backend Interface")

    age = st.number_input("Please enter your age:", min_value=0, max_value=120, step=1)
    ageInput = convertAge(age)
    st.write(ageInput)
    pass