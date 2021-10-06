import streamlit as st
from PIL import Image


def app():
    st.title("Home")

    st.markdown("""Roderick Perez""")

    col1, col2, col3 = st.columns([1, 6, 1])

    with col1:
        st.write("")

    with col2:
        image = Image.open("images/semester_planDS.png")
        st.image(image, width=1000)

    with col3:
        st.write("")
