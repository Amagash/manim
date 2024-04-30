import streamlit as st
import pandas as pd
import gensim.downloader as gen
import numpy as np


st.write("Choose up to 4 words you would like to visualize:")
st.text_input("word_1", key="word_1")
st.text_input("word_2", key="word_2")
st.text_input("word_3", key="word_3")
st.text_input("word_4", key="word_4")

# You can access the value at any point with:
word_1, word_2, word_3, word_4 = st.session_state.word_1, st.session_state.word_2, st.session_state.word_3, st.session_state.word_4


model = gen.load('glove-wiki-gigaword-50')
words = [word_1, word_2, word_3, word_4]

print(model[words[0]])

st.write(pd.DataFrame({
    word_1 : np.array(model[words[0]]),
    # word_2 : np.array(model[words[1]]),
    # word_3 : np.array(model[words[2]]),
    # word_4 : np.array(model[words[3]]),
}))