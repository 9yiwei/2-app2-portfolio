import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", use_column_width="auto")

with col2:
    st.title("Howard Chou")
    content1 = """
    My last job was as a software project assistant, so I understand the program development process and due to work 
    requirements, I will need to conduct website testing and record bugs, prepare relevant test documents, etc.
    
    Also because of the requirements of my last job, I also need to simplify the requests of customers or superiors 
    so that the people receiving the message can understand the problem in a simple and easy-to-understand manner.
    
    Because I understand my own shortcomings in programming, I have continued to self-study Python-related courses 
    on the website so far.
    """
    st.info(content1)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

