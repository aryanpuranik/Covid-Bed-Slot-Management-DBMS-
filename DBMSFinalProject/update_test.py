import datetime

import pandas as pd
import streamlit as st
from database import view_test_data, view_only_test_id, get_test, update_test_data


def update_test():
    result = view_test_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'name'])
    with st.expander("Current Booking Patient Table"):
        st.dataframe(df)
    list_of_bookingpatient = [i[0] for i in view_only_test_id()]
    selected_bookingpatient = st.selectbox("Booking Patient to Edit", list_of_bookingpatient)
    selected_result = get_test(selected_bookingpatient)
    # st.write(selected_result)
    if selected_result:
        id = selected_result[0][0]
        name = selected_result[0][1]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_id = st.text_input("Enter id",id)


        with col2:
            new_name = st.text_input("Enter Name:",name)
            if st.button("Update Info"):
                update_test_data(new_id, new_name, id)
                st.success("Successfully updated:: {} to ::{}".format(id, new_id))

    result2 = view_test_data()
    df2 = pd.DataFrame(result2, columns=['id', 'name'])
    with st.expander("Updated data"):
        st.dataframe(df2)
