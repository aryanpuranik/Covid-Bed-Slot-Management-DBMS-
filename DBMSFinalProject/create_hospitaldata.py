import streamlit as st
from database import add_hospitaldata_table


def create_hospitaldata():
    col1, col2 = st.columns(2)
    with col1:
        hname = st.text_input("Hospital Name:")
        id = st.text_input("Enter hospital id")
        hcode = st.text_input("Hospital Code:")

    with col2:
        normalbed = st.text_input("Number of Normal Beds:")
        hicubed = st.text_input("Number of  HICU Beds:")
        icubed = st.text_input("Number of ICU Beds:")
        vbed = st.text_input("Number of Ventilator Beds:")

    if st.button("Add Details"):
        add_hospitaldata_table(id, hcode, hname, normalbed, hicubed, icubed, vbed)
        st.success("Successfully added Hospital Data: {}".format(hcode))
