import tensorflow_hub as hub
import streamlit as st
import urllib.request

st.write("hello world")
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
#embeddings = embed(["Hello World", "Cats and dogs"])

#st.write(embeddings)
urllib.request.urlretrieve("https://www.dropbox.com/s/12t9fbnp6skcjun/embeddings.pickle?dl=1", "embeddings.pickle")
    
with open('embeddings.pickle', 'rb') as fp:
    embeddings = pickle.load(fp)
with open('data.pickle','rb') as fp:
    d = pickle.load(fp)
with open('versedict (1).pickle','rb') as fp:
    versedict = pickle.load(fp)

st.write("ok")
