import pandas as pd
import streamlit as st
from introduction import introduction
from sidebar import sideBar
from initialModelling import v1
from dataCleaning import v2
from handlingNull import v3
from dataBalancing import v4

def initializeSideBar():
    selection = sideBar()
    if selection[0] or all(value == False for value in selection):
        introduction()
    if selection[1]:
        v1()
    if selection[2]:
        v2()
    if selection[3]:
        v3()
    if selection[4]:
        v4()
    if selection[5]:
        st.write("5")
    if selection[6]:
        st.write("6")
    if selection[7]:
        st.write("7")
    if selection[8]:
        st.write("8")

def main():
    initializeSideBar()


if __name__ == '__main__':
    main()