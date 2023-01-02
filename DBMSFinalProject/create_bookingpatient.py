import streamlit as st
from database import add_bookingpatient_table


def create_bookingpatient():
    col1, col2 = st.columns(2)
    with col1:
        
        pname = st.text_input("Patient Name:")
        id = st.text_input("Enter id:")
        srfid= st.text_input("Enter srfid:")
        pphone = st.text_input("Patient Phone Number:")
        paddress = st.text_input("Patient Address:")

    with col2:
        bedtype = st.selectbox("Bedtype", ["Normal Bed", "ICU Bed", "HICU Bed","VENTILATOR Bed"],key='bedtype')
        hcode = st.text_input("Hospital Code:")
        spo2 = st.text_input("Oxygen Level:")

    if st.button("Book Now"):
        add_bookingpatient_table(id, srfid, bedtype, hcode, spo2, pname, pphone, paddress)
        st.success("Booked Succesfully!: {}".format(hcode))
