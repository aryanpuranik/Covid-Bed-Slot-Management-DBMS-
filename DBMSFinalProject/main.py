import streamlit as st
import mysql.connector
import pandas as pd 


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
)

c = mydb.cursor()

from sql_func import sql_func

from create_bookingpatient import create_bookingpatient
from create_hospitaldata import create_hospitaldata
from create_hospitaluser import create_hospitaluser
from create_test import create_test
# from create_trig import create_trig
from create_user import create_user


from view_bookingpatient import view_bookingpatient
from view_hospitaldata import view_hospitaldata
from view_hospitaluser import view_hospitaluser
from view_test import view_test
# from view_trig import view_trig
from view_user import view_user


from update_bookingpatient import update_bookingpatient
from update_hospitaldata import update_hospitaldata
from update_hospitaluser import update_hospitaluser
from update_test import update_test
# # from update_trig import update_trig
from update_user import update_user




from delete_bookingpatient import delete_bookingpatient
from delete_hospitaldata import delete_hospitaldata
from delete_hospitaluser import delete_hospitaluser
from delete_test import delete_test
# # from delete_trig import delete_trig
from delete_user import delete_user



from database import create_bookingpatient_table
from database import create_hospitaldata_table
from database import create_hospitaluser_table
from database import create_test_table
from database import create_trig_table
from database import create_user_table
# from delete import delete
# from read import read
# from update import update



def main():
    st.title("Covid Bed Slot Management")
    menu = ["Add", "View", "Edit", "Remove","SQL Query"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_bookingpatient_table()
    create_hospitaldata_table()
    create_hospitaluser_table()
    create_test_table()
    create_trig_table()
    create_user_table()
    menu1 = ["Booking Patient", "Hospital Data", "Staff Login", "User Login" , "user"]
    choice1 = st.sidebar.selectbox("Entity", menu1)


    if choice =="Add":
        
        if choice1 == "Booking Patient":
            st.subheader("Enter Patient Details:")
            create_bookingpatient()

        elif choice1 == "Hospital Data":
            st.subheader("Enter Hospital Data:")
            create_hospitaldata()

        elif choice1 == "Staff Login":
            st.subheader("Enter Staff Details")
            create_hospitaluser()

        elif choice1 == "User Login":
            st.subheader("Enter User Login details")
            create_test()

        # elif choice1 == "trig":
        #     st.subheader("Delete created tasks")
        #     create_trig()

        elif choice1 == "user":
            st.subheader("Enter user details")
            create_user()

        else:
            st.subheader("About tasks")




    if choice =="View":
        if choice1 == "Booking Patient":
            st.subheader("Patient Details:")
            view_bookingpatient()

        elif choice1 == "Hospital Data":
            st.subheader("Hospital Data:")
            view_hospitaldata()

        elif choice1 == "Staff Login":
            st.subheader("About staff ")
            view_hospitaluser()

        elif choice1 == "User Login":
            st.subheader("User Login details")
            view_test()

        #  elif choice1 == "trig":
        #     st.subheader("Delete created tasks")
        #     view_trig()

        elif choice1 == "user":
            st.subheader("User details")
            view_user()

        else:
            st.subheader("About tasks")



    if choice =="Edit":
        
        if choice1 == "Booking Patient":
            st.subheader("Enter Patient Details:")
            update_bookingpatient()

        elif choice1 == "Hospital Data":
            st.subheader("Enter Hospital Data:")
            update_hospitaldata()

        elif choice1 == "Staff Login":
            st.subheader("Enter staff Details")
            update_hospitaluser()

        elif choice1 == "User Login":
            st.subheader("Enter User Login details")
            update_test()

        # elif choice1 == "trig":
        #     st.subheader("Delete created tasks")
        #     update_trig()

        elif choice1 == "user":
            st.subheader("Enter user details")
            update_user()

        # else:
        #     st.subheader("About tasks")





    if choice =="Remove":
        if choice1 == "Booking Patient":
            st.subheader("Patient Details:")
            delete_bookingpatient()

        elif choice1 == "Hospital Data":
            st.subheader("Hospital Data:")
            delete_hospitaldata()

        elif choice1 == "Staff Login":
            st.subheader("About staff")
            delete_hospitaluser()

        elif choice1 == "User Login":
            st.subheader("User Login details")
            delete_test()

        #elif choice1 == "trig":
        #   st.subheader("Delete created tasks")
        #   delete_trig()

        elif choice1 == "user":
            st.subheader("User details")
            delete_user()

        else:
            st.subheader("About tasks")


    if choice == "SQL Query":
        st.subheader("Type in your Query")
        ans = sql_func()
        if (ans != 0):
            df = pd.DataFrame(ans)
            st.dataframe(df)
        else:
            st.subheader("No query given")




if __name__ == '__main__':
    main()
