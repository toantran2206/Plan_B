from os import write
import streamlit as st
import numpy as np

st.title('This is a tile')

st.header('Diver-conscinousness')
write('Hi there! Welcome to our diver-consciousness app!')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)