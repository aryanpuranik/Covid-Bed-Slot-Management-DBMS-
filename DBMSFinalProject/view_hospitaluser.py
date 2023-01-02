import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_hospitaluser_data


def view_hospitaluser():
    result = view_hospitaluser_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'hcode', 'email', 'password'])
    with st.expander("View Hospital User data"):
        st.dataframe(df)