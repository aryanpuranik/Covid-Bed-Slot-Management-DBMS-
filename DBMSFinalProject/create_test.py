import streamlit as st
from database import add_test_table


def create_test():
    col1, col2 = st.columns(2)
    with col1:
        id = st.text_input("Enter id")


    with col2:
        name = st.text_input("Enter Name:")

    if st.button("Tap to Enter Hospital User Detials "):
        add_test_table(id ,name)
        st.success("Successfully added Hospital User Details: {}".format(name))
