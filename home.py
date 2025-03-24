import streamlit as st
import streamlit_lottie as st_lottie
from streamlit_extras.switch_page_button import switch_page
from modules import *

with open("letter.txt", encoding="utf-8") as f:
    text = f.read()

st.session_state.stage = 0

if st.session_state.stage == 0:
    st.title("Welcome to our project.")
    name = st.text_input("Before we start, please enter your name.")
        
    if name:
        st.session_state.stage = 1

if st.session_state.stage == 1:
    st.write(f"Hi, {name}")
    pw = st.text_input("Please enter the password.", type="password")
    st.write("Hint: There are only 1 person knowing the password. The creator does not explicitly provide the password to anyone.")
    st.write("If you are the chosen one, you will know the password.")
    if pw:
        if Heart.login(name, pw):
            st.write("Successfully logging in!")
            st.session_state.stage = 2
        else:
            st.write("You are not authorized for this. I'm sorry.")

if st.session_state.stage == 2:
    
    button = st.button("Click Me")
    if button:
        st.session_state.stage = 3

if st.session_state.stage == 3:
    col1, col2 = st.columns(2)
    with col1:
        Heart.print_heart()
    with col2:
        st.markdown(text, unsafe_allow_html = True)



