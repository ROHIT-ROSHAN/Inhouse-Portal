# Importing pakages
import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )
# c = mydb.cursor()

# c.execute("USE railway_reservation_355")


def main():
    st.title("IN HOUSE PORTAL")
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add":
        
        option = st.selectbox(    'Add Data Into Database', ('Employee', 'Role', 'Department','Manager','Project Manager','Project'))

        if option=="Employee":
        
            create(1)

        if option=="Role":
        
            create(2) 

        if option=="Department":
        
            create(3)
        if option=="Manager":
        
            create(4)
        if option=="Project Manager":
        
            create(5)
        if option=="Project":
        
            create(6)                     


    elif choice == "View":
        st.subheader("View All Databases")
        read()

    elif choice == "Edit":
        st.subheader("Update Database")
        update()

    elif choice == "Remove":
        st.subheader("Delete  Database")
        delete()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()