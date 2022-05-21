import streamlit as st

#UI
def actionsEditor():
    filename = st.text_input("Filename")
    actionsTxt = st.text_area("Actions Editor")
    if st.button("Save Action"):
        saveAction(filename, actionsTxt)

#Functions
def saveAction(filename, actionsTxt):
    file = open("./actions/"+filename+".rlu", "a")
    file.write(actionsTxt)
    file.close()