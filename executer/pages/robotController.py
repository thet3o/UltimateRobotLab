import streamlit as st
import body_controller as bc
import actionsReader as ar
import os

#Functions
def load_actions():
    actions = []
    for action in os.listdir("./actions"):
        if action.endswith(".rlu"):
            actions.append(action)
    return actions

#UI
def robotController():
    st.title("Robot Controller")

    if st.button("Load Actions"):
        actions = load_actions()
        st.write(actions)

    if st.button("Check Boards"):
        bc.checkArduinos()

    st.text("Move with actions")
    action = st.selectbox("Select action", load_actions())
    if st.button("Move with action"):
        ar.executer(ar.read("./actions/"+action))