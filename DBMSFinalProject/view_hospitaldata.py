import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_hospitaldata_data,procedure_call


def view_hospitaldata():
    result = view_hospitaldata_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'hcode', 'hname', 'normalbed', 'hicubed','icubed', 'vbed','add_date'])
    with st.expander("View Hospital User data"):
        st.dataframe(df)

        
    st.subheader("Name of the hospital:")
    id = st.number_input("Enter user id:")
    table = procedure_call(id)
    df = pd.DataFrame(table,columns=['hname','id'])
    st.dataframe(df)