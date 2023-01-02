import datetime

import pandas as pd
import streamlit as st
from database import view_bookingpatient_data, view_only_bookingpatient_id, get_bookingpatient, update_bookingpatient_data


def update_bookingpatient():
    result = view_bookingpatient_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id','srfid', 'bedtype', 'hcode', 'spo2', 'pname', 'pphone', 'paddress'])
    with st.expander("Current Booking Patient Table"):
        st.dataframe(df)
    list_of_bookingpatient = [i[0] for i in view_only_bookingpatient_id()]
    selected_bookingpatient = st.selectbox("Booking Patient to Edit", list_of_bookingpatient)
    selected_result = get_bookingpatient(selected_bookingpatient)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        srfid = selected_result[0][1]
        bedtype = selected_result[0][2]
        hcode = selected_result[0][3]
        spo2 = selected_result[0][4]
        pname = selected_result[0][5]
        pphone = selected_result[0][6]
        paddress = selected_result[0][7]



        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            
            new_pname = st.text_input("Patient Name:",pname)
            new_id = st.text_input("Enter id:",id)
            new_srfid= st.text_input("Enter srfid:",srfid)
            new_pphone = st.text_input("Patient Phone Number:",pphone)
            new_paddress = st.text_input("Patient Address:",paddress)

        with col2:
            new_bedtype = st.selectbox("Bedtype", ["Normal Bed", "ICU Bed", "HICU Bed","VENTILATOR Bed"],key='bedtype')
            new_hcode = st.text_input("Hospital Code:",hcode)
            new_spo2 = st.text_input("Oxygen Level:",spo2)
        if st.button("Update Info"):
            update_bookingpatient_data(new_id, new_srfid, new_bedtype, new_hcode, new_spo2,new_pname,new_pphone,new_paddress, id)
            st.success("Successfully updated:: {} to ::{}".format(id, new_id))

    result2 = view_bookingpatient_data()
    df2 = pd.DataFrame(result2, columns=['id', 'srfid', 'bedtype',' hcode', 'spo2', 'pname', 'pphone', 'paddress'])
    with st.expander("Updated data"):
        st.dataframe(df2)
