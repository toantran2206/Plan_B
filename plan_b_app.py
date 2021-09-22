from os import write
import streamlit as st
import numpy as np

st.title('This is a tile')

st.header('Diver-conscinousness')
st.write('Hi there! Welcome to our diver-consciousness app!')
user_input = st.text_input("Please tell us your name:")
if user_input:
    st.write('Hi, ',user_input)
    st.write('This a diver-consciousness quiz with 40 questions. There is not right or wrong answer. You just need to think carefully and choose which suites you best!')
    if st.button("Click here to start"):
        values = st.slider(
            'Select a range of values',
            0.0, 100.0, (25.0, 75.0))
        st.write('Values:', values)