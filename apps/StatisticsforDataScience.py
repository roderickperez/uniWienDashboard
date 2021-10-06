import streamlit as st


def app():
    st.title("Statistics for Data Science")

    select = st.sidebar.radio("Select: ", ("Lecture Notes", "Homeworks"))

    if select == "Lecture Notes":

        lectures = [1, 2]

        st.sidebar.selectbox("Lecture", lectures)

        st.write("Lecture Notes")

        st.write("Date: ")

    else:

        homework = [1, 2]

        st.sidebar.selectbox("Homework", homework)

        st.write("Homework")

        st.write("Date: ")

    # st.write("This is the `home page` of this multi-page app.")
