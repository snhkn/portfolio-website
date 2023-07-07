import pandas
import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Seniha")
    content = """
        Greetings! I'm Seniha, and I have an immense passion for cats. 
        Presently, I am nurturing four adorable baby cats. 
        Alongside that, I'm actively seeking an exciting job opportunity.
        I hold a degree in Computer Science, although I've taken a break from the workforce for a while. 
        As a way to showcase my capabilities, I've created this portfolio website. 
        Thank you for your interest! Feel free to explore and learn more about my skills and experiences.
        """
    st.info(content)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])