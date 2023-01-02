import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_test_data


def view_test():
    result = view_test_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'name'])
    with st.expander("View test Data"):
        st.dataframe(df)