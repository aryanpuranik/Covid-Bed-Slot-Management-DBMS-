import pandas as pd
import streamlit as st
from database import view_user_data
from database import view_only_user_id
from database import delete_user_data

def delete_user():
    result = view_user_data()
    df = pd.DataFrame(result, columns=['id', 'srfid', 'email', 'dob'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_user = [i[0] for i in view_only_user_id()]
    selected_user = st.selectbox("Task to Delete", list_of_user)
    st.warning("Do you want to delete ::{}".format(selected_user))
    if st.button("Delete User Details"):
        delete_user_data(selected_user)
        st.success("User Details have been deleted successfully")
    new_result = view_user_data()
    df2 = pd.DataFrame(new_result, columns=['id', 'srfid', 'email', 'dob'])
    with st.expander("Updated data"):
        st.dataframe(df2)