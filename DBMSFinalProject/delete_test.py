import pandas as pd
import streamlit as st
from database import view_test_data
from database import view_only_test_id
from database import delete_test_data

def delete_test():
    result = view_test_data()
    df = pd.DataFrame(result, columns=['id', 'name'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_test = [i[0] for i in view_only_test_id()]
    selected_test = st.selectbox("Task to Delete", list_of_test)
    st.warning("Do you want to delete ::{}".format(selected_test))
    if st.button("Delete Test Data"):
        delete_test_data(selected_test)
        st.success("Test Data has been deleted successfully")
    new_result = view_test_data()
    df2 = pd.DataFrame(new_result, columns=['id', 'name'])
    with st.expander("Updated data"):
        st.dataframe(df2)