import streamlit as st
import pages.actionsEditor as actEd
import pages.robotController as rtC
import pages.ttsController as ttsC
import executer.recognitionController as recC

def main():
    pages = {
        "Robot Controller": rtC.robotController,
        "Text to Speech": ttsC.ttsController,
        "Actions Editor": actEd.actionsEditor
    }
    page = st.sidebar.radio("Select your page", tuple(pages.keys()))
    pages[page]()

if __name__ == "__main__":
    main()