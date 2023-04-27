import pandas as pd
import streamlit as st
from introduction import introduction
from sidebar import sideBar
from dataCleaning import v2
from dataBalancing import v4
from backendInterface import interface
from tracker import report

def initializeSideBar():
    selection = sideBar()
    if selection[0]:
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
        correlation_main()
    if selection[6]:
        report()
    if selection[7] or all(value == False for value in selection) :
        interface()


def main():
    initializeSideBar()

if __name__ == '__main__':

    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()