
import streamlit as st
from database import add_user_table


def create_user():
    col1, col2 = st.columns(2)
    with col1:
        id = st.text_input("Enter hospital id")
        email = st.text_input("Enter Email:")


    with col2:
        srfid = st.text_input("Enter srfid")
        dob = st.date_input("Enter Date of Birth:")

    if st.button("Tap to Enter User Detials "):
        add_user_table(id, srfid ,email,dob)
        st.success("Successfully added User Details: {}".format(id))
