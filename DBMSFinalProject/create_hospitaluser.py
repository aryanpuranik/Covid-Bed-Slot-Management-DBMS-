
import streamlit as st
from database import add_hospitaluser_table


def create_hospitaluser():
    col1, col2 = st.columns(2)
    with col1:
        id = st.text_input("Enter hospital id")
        hcode = st.selectbox("Hospital Code:",["MAT123","BBH01"],key = 'hcode')
        email = st.text_input("Enter Email:")


    with col2:
        password = st.text_input("Enter Password:")

    if st.button("Tap to Enter Hospital User Detials "):
        add_hospitaluser_table(id, hcode, email, password)
        st.success("Successfully added Hospital User Details: {}".format(hcode))
