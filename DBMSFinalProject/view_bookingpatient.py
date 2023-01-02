import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_bookingpatient_data


def view_bookingpatient():
    result = view_bookingpatient_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['id', 'srfid', 'bedtype',' hcode', 'spo2', 'pname', 'pphone', 'paddress'])
    with st.expander("View all Bookings"):
        st.dataframe(df)
    # with st.expander("Train details"):
    #     train_df = df['Availability'].value_counts().to_frame()
    #     train_df = train_df.reset_index()
    #     st.dataframe(train_df)
    #     p1 = px.pie(train_df, names='index', values='Availability')
    #     st.plotly_chart(p1)