import datetime

import pandas as pd
import streamlit as st
from database import view_hospitaldata_data, view_only_hospitaldata_id, get_hospitaldata, update_hospitaldata_data


def update_hospitaldata():
    result = view_hospitaldata_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'hcode', 'hname', 'normalbed', 'hicubed','icubed', 'vbed','hospital_name'])
    
    with st.expander("Current Booking Patient Table"):
        st.dataframe(df)
    list_of_bookingpatient = [i[0] for i in view_only_hospitaldata_id()]
    selected_bookingpatient = st.selectbox("Booking Patient to Edit", list_of_bookingpatient)
    selected_result = get_hospitaldata(selected_bookingpatient)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        hcode = selected_result[0][1]
        hname = selected_result[0][2]
        normalbed = selected_result[0][3]
        hicubed = selected_result[0][4]
        icubed = selected_result[0][5]
        vbed = selected_result[0][6]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_hname = st.text_input("Hospital Name:",hname)
            new_id = st.text_input("Enter hospital id",id)
            new_hcode = st.text_input("Hospital Code:",hcode)

        with col2:
            new_normalbed = st.text_input("Number of Normal Beds:",normalbed)
            new_hicubed = st.text_input("Number of  hicu Beds:",hicubed)
            new_icubed = st.text_input("Number of ICE Beds:",icubed)
            new_vbed = st.text_input("Number of Ventilator Beds:",vbed)
            if st.button("Update Info"):
                update_hospitaldata_data(new_id, new_hcode, new_hname, new_normalbed, new_hicubed, new_icubed, new_vbed , id,)
                st.success("Successfully updated:: {} to ::{}".format(id, new_id))

    result2 = view_hospitaldata_data()
    df2 = pd.DataFrame(result2, columns=['id', 'hcode', 'hname', 'normalbed', 'hicubed','icubed', 'vbed','hospital_name'])
    with st.expander("Updated data"):
        st.dataframe(df2)
