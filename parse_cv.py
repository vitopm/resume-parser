import streamlit as st
from pyresparser import ResumeParser
import nltk
# nltk.download('stopwords')
import pandas as pd

def parse():
    st.header("CV Extractor")
    
    file = st.file_uploader(
        'Upload your CV in PDF',
        type = "pdf",
        accept_multiple_files = False
        )
    if file is not None:
        # st.write("yooo")
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
