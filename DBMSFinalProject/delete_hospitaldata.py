import pandas as pd
import streamlit as st
from database import view_hospitaldata_data
from database import view_only_hospitaldata_id
from database import delete_hospitaldata_data

def delete_hospitaldata():
    result = view_hospitaldata_data()
    df = pd.DataFrame(result, columns=['id', 'hcode', 'hname', 'normalbed', 'hicubed','icubed', 'vbed','add_date'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_hospitaldata = [i[0] for i in view_only_hospitaldata_id()]
    selected_hospitaldata = st.selectbox("Task to Delete", list_of_hospitaldata)
    st.warning("Do you want to delete ::{}".format(selected_hospitaldata))
    if st.button("Delete Hospital Data"):
        delete_hospitaldata_data(selected_hospitaldata)
        st.success("Hospital Data has been deleted successfully")
    new_result = view_hospitaldata_data()
    df2 = pd.DataFrame(new_result, columns=['id', 'hcode', 'hname', 'normalbed', 'hicubed','icubed', 'vbed','add_date'])
    with st.expander("Updated data"):
        st.dataframe(df2)