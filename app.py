# pip install spacy==2.3.5

# pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz

# pip install pyresparser

import streamlit as st
from parse_cv import parse
from home import description, about

st.image("asset\image\gambar-resume.jpg")
st.title("📑Resume Parser")
st.write("------------")
page = st.selectbox('Navigate', ['Home', 'Parse my CV', 'About us'])

if page =="Home":
    description()
elif page =="Parse my CV":
    parse()
elif page == "About us":
    about()
