import pandas as pd
import streamlit as st
from introduction import introduction
from sidebar import sideBar
from dataCleaning import v2
from backendInterface import interface
from tracker import report

def initializeSideBar():
    selection = sideBar()
    if selection[0]:
        introduction()
    if selection[1]:
        interface()
    if all(value is None for value in selection):
        introduction()


def main():
    introduction()
    initializeSideBar()

if __name__ == '__main__':

    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()