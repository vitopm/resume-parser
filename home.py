import streamlit as st

def description():
    st.header("👋Welcome to our resume parser!")
    st.write(""" 
### This website is to extract and parse your Resume document

#### How to use this application:
1. Choose your Resume document.
2. Go to Parse my Resume menu.
3. Upload the document you have chosen. Please make sure your Resume document is in PDF format.
4. Drop your file or drag and drop it.
5. Voila, your PDF has been parsed!
    """)

def about():
    st.header("👩‍🎓👨‍🎓We are a team of students")
    colpic1, coldesc1 = st.columns([1,3])
    with colpic1:
        st.image("asset/image/cheryl.jpeg")

    with coldesc1:
        st.subheader("Cheryl Almeira")
        st.write("""

        A passionate student with relentless idea to make everything around her better in everyway.

        """)

    colpic2, coldesc2 = st.columns([1,3])

    with colpic2:
        st.image("asset/image/michelle.jpeg")

    with coldesc2:
        st.subheader("Michelle A. Guntoro")
        
        st.write("""
        
        Giving up on a great idea is not on her dictionary. Her team management skills is the main driver of the project. 
        """)

    colpic3, coldesc3= st.columns([1,3])

    with colpic3:
        st.image("asset/image/vito.jpeg")
        
    with coldesc3:

        st.subheader("Vito P. Minardi")

        st.write("""
        
        Idea runs in his blood. Should he be born a hundred years ago, he could've been the picasso of the century.

        """)
