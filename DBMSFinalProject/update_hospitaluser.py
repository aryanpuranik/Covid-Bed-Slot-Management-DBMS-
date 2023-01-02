import datetime

import pandas as pd
import streamlit as st
from database import view_hospitaluser_data, view_only_hospitaluser_id, get_hospitaluser, update_hospitaluser_data


def update_hospitaluser():
    result = view_hospitaluser_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'hcode', 'email', 'password'])
    with st.expander("Current Booking Patient Table"):
        st.dataframe(df)
    list_of_hospitaluser = [i[0] for i in view_only_hospitaluser_id()]
    selected_hospitaluser = st.selectbox("Booking Patient to Edit", list_of_hospitaluser)
    selected_result = get_hospitaluser(selected_hospitaluser)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        hcode = selected_result[0][1]
        email = selected_result[0][2]
        password = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_id = st.text_input("Enter hospital id",id)
            new_hcode = st.selectbox("Hospital Code:",["MAT123","BBH01"],key = 'hcode')
            new_email = st.text_input("Enter Email:",email)


        with col2:
            new_password = st.text_input("Enter Password:",password)
        if st.button("Update Info"):
            update_hospitaluser_data(new_id, new_hcode, new_email,new_password, id)
            st.success("Successfully updated:: {} to ::{}".format(id, new_id))

    result2 = view_hospitaluser_data()
    df2 = pd.DataFrame(result2, columns=['id', 'hcode', 'email', 'password'])
    with st.expander("Updated data"):
        st.dataframe(df2)
