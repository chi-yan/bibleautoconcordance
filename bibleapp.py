import tensorflow_hub as hub
import streamlit as st
st.set_page_config(layout="wide")
import urllib.request
import pickle
import numpy as np
from collections import OrderedDict
from operator import itemgetter
import pandas as pd
import string
from st_aggrid import AgGrid

def cosine_similarities(A, B): #A is the big matrix containing all embeddings, B is the sentence
#    return np.divide(np.dot(A,B),np.apply_along_axis(np.linalg.norm, 1, A)*np.linalg.norm(B))[:,0]
    return np.dot(A,B).flatten()
    
def generateSimilarities(text, numberOfItems):
  embedded_text = embed([text])
  similarities = cosine_similarities(embeddings.numpy(), embedded_text.numpy().T)
  data = []
  similarities[0] = -0.1
  for i in range(len(embeddings)):
    data.append([versedict[i],d[versedict[i]],similarities[i]])
  return(pd.DataFrame (data, columns = ['Verse', 'Text', 'Similarity']).sort_values(by=['Similarity'], ascending=False).head(numberOfItems))

@st.cache
def load_hub():
    return hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

@st.cache
def load_embeddings():
    urllib.request.urlretrieve("https://www.dropbox.com/s/12t9fbnp6skcjun/embeddings.pickle?dl=1", "embeddings.pickle") #too big to upload to Github
    with open('embeddings.pickle', 'rb') as fp:
        embeddings = pickle.load(fp)
    return embeddings

embed = load_hub()

embeddings = load_embeddings()
with open('data.pickle','rb') as fp:
    d = pickle.load(fp)
with open('versedict (1).pickle','rb') as fp:
    versedict = pickle.load(fp)
    
st.markdown("""<h1>Bible Auto-Concordance Web App</h1> <p>Enter a sentence, phrase or word you want to look for in the KJV Bible.</p><p>Built with NLP, Streamlit, AgGrid and the Universal Sentence Encoder.</p><p>Works best on a desktop, if you are trying this from a mobile device, try ending the sentence with a space or a dot.</p>""", unsafe_allow_html=True)
sentence = st.text_input('Input sentence here: ')

if sentence:
    response = generateSimilarities(sentence,5).to_records(index=False)
    df = pd.DataFrame(response, columns=['Verse','Text','Similarity'])
    AgGrid(df)
    
