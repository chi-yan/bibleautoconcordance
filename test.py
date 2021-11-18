import tensorflow_hub as hub
import streamlit as st
import urllib.request
import pickle
import numpy as np
from collections import OrderedDict
from operator import itemgetter
import pandas as pd
import string

def cosine_similarities(A, B): #A is the big matrix containing all embeddings, B is the sentence
    return np.divide(np.dot(A,B),np.apply_along_axis(np.linalg.norm, 1, A)*np.linalg.norm(B))[:,0]
    
def generateSimilarities(text, numberOfItems):
  embedded_text = embed([text])
  similarities = cosine_similarities(embeddings.numpy(), embedded_text.numpy().T)
  data = []
  similarities[0] = -0.1
  for i in range(len(embeddings)):
    data.append([versedict[i],d[versedict[i]],similarities[i]])
  return(pd.DataFrame (data, columns = ['Verse', 'Text', 'Similarity']).sort_values(by=['Similarity'], ascending=False).head(numberOfItems))

st.write("hello world")
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
#embeddings = embed(["Hello World", "Cats and dogs"])

#st.write(embeddings)
urllib.request.urlretrieve("https://www.dropbox.com/s/12t9fbnp6skcjun/embeddings.pickle?dl=1", "embeddings.pickle") #too big to upload to Github
    
with open('embeddings.pickle', 'rb') as fp:
    embeddings = pickle.load(fp)
with open('data.pickle','rb') as fp:
    d = pickle.load(fp)
with open('versedict (1).pickle','rb') as fp:
    versedict = pickle.load(fp)
    
sentence="world created"
#st.write(str(list(generateSimilarities(sentence,5).to_records(index=False))))
st.write("ok")
