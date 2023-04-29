import pandas as pd
import streamlit as st
from introduction import introduction
from sidebar import sideBar
from dataCleaning import v2
from backendInterface import interface
from tracker import report

def initializeSideBar():
    selection = sideBar()
    introduction()
    if selection[0]:
        introduction()
    if selection[2]:
        backendInterface()


def main():
    initializeSideBar()

if __name__ == '__main__':

    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()