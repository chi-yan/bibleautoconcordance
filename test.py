import tensorflow_hub as hub
import streamlit as st

st.write("hello world")
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
embeddings = embed(["Hello World", "Cats and dogs"])

st.write(embeddings)
