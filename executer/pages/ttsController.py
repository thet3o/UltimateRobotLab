import streamlit as st
import otherAccessories as othA

def ttsController():
    st.title("Text to Speech")
    toSpeech = st.text_input("TextToSpeech")
    if st.button("Play TextToSpeech"):
        othA.speakEngine(toSpeech)
