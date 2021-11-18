
import streamlit as st
sentence = st.text_input('Input sentence here: ')

st.write("stuff")

if sentence:
    st.write(sentence)
