import pandas as pd
import streamlit as st
from phase1 import introduction, v3, v4
from sidebar import sideBar
from initialModelling import v1
from dataCleaning import v2

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

def main():
    initializeSideBar()


if __name__ == '__main__':
    main()