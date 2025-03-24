import re
import json
import streamlit as st
import streamlit_lottie as st_lottie

class Heart:
    name = "thao"
    password = "25032023"

    @classmethod
    def login(cls, name, password):
        name = name.lower()
        password = re.sub(r"[^\w\s]", "", password)
        if password == cls.password and name == cls.name:
            return True
        else:
            return False

    @classmethod
    def print_heart(self):

        with open("Animation - 1742833383797.json", "r") as f:
            heart = json.load(f)
        
        st.lottie(heart)