import pandas as pd
import streamlit as st
from introduction import introduction
from sidebar import sideBar
from dataCleaning import v2
from tracker import report
from backendInterface import interface


def initializeSideBar():
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    selection = sideBar()
    if selection[0]:
        st.session_state.counter += 1
        introduction()
    if selection[1]:
        interface()
    elif st.session_state.counter == 0:
        introduction()


def main():
    initializeSideBar()

if __name__ == '__main__':
    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()