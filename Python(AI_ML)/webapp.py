# Streamlit is an open-source Python library that lets you create beautiful web apps for  data science, machine learning, AI, and automation-without needing HTML, CSS, or JavaScript.

import streamlit as st

st.title("Welcome to AI app")
st.header("AI, ML and Automation Demo")

if st.button("Click Me!"):
    st.success("You clicked me.")

name = st.text_input("what is your name?")

if name:
    st.write(f"Hello, {name} !")

age = st.slider("Select your age: ")
st.write("your age is:", age)

# terminal: streamlit run webapp.py