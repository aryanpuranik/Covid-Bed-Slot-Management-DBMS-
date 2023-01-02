import pandas as pd
import streamlit as st
from database import view_hospitaluser_data
from database import view_only_hospitaluser_id
from database import delete_hospitaluser_data

def delete_hospitaluser():
    result = view_hospitaluser_data()
    df = pd.DataFrame(result, columns=['id', 'hcode', 'email', 'password'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_hospitaluser = [i[0] for i in view_only_hospitaluser_id()]
    selected_hospitaluser = st.selectbox("Task to Delete", list_of_hospitaluser)
    st.warning("Do you want to delete ::{}".format(selected_hospitaluser))
    if st.button("Delete Hospital User"):
        delete_hospitaluser_data(selected_hospitaluser)
        st.success("Hospital User has been deleted successfully")
    new_result = view_hospitaluser_data()
    df2 = pd.DataFrame(new_result, columns=['id', 'hcode', 'email', 'password'])
    with st.expander("Updated data"):
        st.dataframe(df2)