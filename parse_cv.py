from numpy import empty
import streamlit as st
import pandas as pd
import time

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
        with st.spinner(text='🤖***Our evil robot is reading your resume***'):
            time.sleep(2)
            data = ResumeParser(file).get_extracted_data()
            file_details = {
                "filename":file.name, 
                "filetype":file.type,
                "filesize":file.size
                }
            st.subheader("File details:")
            st.write("**File name**: " + file_details["filename"])
            st.write("**File type**: " + file_details["filetype"])
            st.write("**File size**: " + str(file_details["filesize"]) + " bytes" )
            st.write("---")
            st.header("Extracted data")
            # st.json(data)

            # st.info("""
            # Scroll down to see your result or click the button here
            # """)
            st.markdown("[Click here to go to Result](#result)", unsafe_allow_html=True)
            # link = '[GitHub](http://github.com)'
            # st.markdown(link, unsafe_allow_html=True)

            num_of_error = 0 #max 9

            for key, values in data.items():
                key = key.replace("_", " ").capitalize()
                st.write("##### {key}:".format(key=key))
                if type(values) == list and len(values) > 5:
                    count = 1
                    with st.expander("Detailed information", expanded=False):
                        for value in values:
                            st.write(str(count) + ". " + str(value))
                            count += 1
                    if len(values) > 10:
                        st.warning("Are you sure they will read this many?")
                        num_of_error += 1
                elif type(values) == list and len(values) < 5:
                    count = 1
                    for value in values:
                            st.write(str(count) + ". " + str(value))
                            count += 1
                else:
                    st.write(str(values))
                if values == None:
                    st.warning("Our system can't detect information regarding your " + key.lower())
                    num_of_error += 1
            
            st.write("---")

            st.header("Result")
            if num_of_error == 0:
                st.success("Your resume is good to go!🥳🎉")
            elif num_of_error <= 3:
                st.warning("Your resume has a few errors")
            elif num_of_error <=8:
                st.error("Your resumes contains more than 3 errors, it needs to be fixed!")
            else:
                st.error("Are you submitting empty pdf? Resubmit your resume again!")
                    
    # data = ResumeParser('CV.pdf').get_extracted_data()
    # data
    
    # df = pd.DataFrame()
