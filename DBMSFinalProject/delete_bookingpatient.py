import pandas as pd
import streamlit as st
from database import view_bookingpatient_data
from database import view_only_bookingpatient_id
from database import delete_bookingpatient_data

def delete_bookingpatient():
    result = view_bookingpatient_data()
    df = pd.DataFrame(result, columns=['id', 'srfid', 'bedtype',' hcode', 'spo2', 'pname', 'pphone', 'paddress'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_bookingpatient = [i[0] for i in view_only_bookingpatient_id()]
    selected_bookingpatient = st.selectbox("Task to Delete", list_of_bookingpatient)
    st.warning("Do you want to delete ::{}".format(selected_bookingpatient))
    if st.button("Delete Booking"):
        delete_bookingpatient_data(selected_bookingpatient)
        st.success("Booking has been deleted successfully")
    new_result = view_bookingpatient_data()
    df2 = pd.DataFrame(new_result, columns=['id', 'srfid', 'bedtype',' hcode', 'spo2', 'pname', 'pphone', 'paddress'])
    with st.expander("Updated data"):
        st.dataframe(df2)