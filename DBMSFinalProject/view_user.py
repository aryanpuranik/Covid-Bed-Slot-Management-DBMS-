import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_user_data


def view_user():
    result = view_user_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'srfid', 'email', 'dob'])
    with st.expander("View User details"):
        st.dataframe(df)