import datetime

import pandas as pd
import streamlit as st
from database import view_user_data, view_only_user_id, get_user, update_user_data


def update_user():
    result = view_user_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'srfid', 'email', 'dob'])
    with st.expander("Current Booking Patient Table"):
        st.dataframe(df)
    list_of_user = [i[0] for i in view_only_user_id()]
    selected_user = st.selectbox("Booking Patient to Edit", list_of_user)
    selected_result = get_user(selected_user)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        srfid = selected_result[0][1]
        email = selected_result[0][2]
        dob = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_id = st.text_input("Enter hospital id")
            new_email = st.text_input("Enter Email:")


        with col2:
            new_srfid = st.text_input("Enter srfid")
            new_dob = st.text_input("Enter Date of Birth:")
        if st.button("Update Info"):
            update_user_data(new_id, new_srfid, new_email, new_dob, id)
            st.success("Successfully updated:: {} to ::{}".format(id, new_id))

    result2 = view_user_data()
    df2 = pd.DataFrame(result2, columns=['id', 'srfid', 'email', 'dob'])
    with st.expander("Updated data"):
        st.dataframe(df2)
