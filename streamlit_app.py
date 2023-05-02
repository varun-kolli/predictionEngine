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
        introduction()

    selection = sideBar()
    if selection[0]:
        introduction()
        st.session_state.counter = 1
    if selection[1]:
        interface()




def main():
    #initializeSideBar()
    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def set_stage(stage):
        st.session_state.stage = stage

    # Some code
    st.button('First Button', on_click=set_stage, args=(1,))

    if st.session_state.stage > 0:
        # Some code
        st.button('Second Button', on_click=set_stage, args=(2,))
    if st.session_state.stage > 1:
        # More code, etc
        st.button('Third Button', on_click=set_stage, args=(3,))
    if st.session_state.stage > 2:
        st.write('The end')
    st.button('Reset', on_click=set_stage, args=(0,))

if __name__ == '__main__':
    with open("style.css") as f:
     st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html = True)
    main()