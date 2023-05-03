import pandas as pd
import streamlit as st
from introduction import introduction
from sidebar import sideBar
from dataCleaning import v2
from tracker import report
from backendInterface import interface
from methodology import methMain


def initializeSideBar():
    if "counter" not in st.session_state:
        st.session_state.counter = 0
        introduction()

    selection = sideBar()
    if selection[0]:
        introduction()
        st.session_state.counter = 1
    if selection[1]:
        interface()
    if selection[2]:
        methMain()




def main():
    initializeSideBar()


if __name__ == '__main__':
    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()