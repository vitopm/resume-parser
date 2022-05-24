import streamlit as st
import pandas as pd

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from pyresparser import ResumeParser


def parse():
    st.header("🧐Resume Extractor")
    
    file = st.file_uploader(
        'Upload your Resume in PDF',
        type = "pdf",
        accept_multiple_files = False
        )
    if file is not None:
        # st.write("yooo")
        with st.spinner(text='Our evil robot is reading your resume'):
            data = ResumeParser(file).get_extracted_data()
            file_details = {
                "filename":file.name, 
                "filetype":file.type,
                "filesize":file.size
                }
            st.subheader("File details:")
            for key, value in file_details.items():
                st.write(str(key) + ": " + str(value) + " bytes")
            st.subheader("Extracted data")
            st.write(data)

    # data = ResumeParser('CV.pdf').get_extracted_data()
    # data
    
    # df = pd.DataFrame()
