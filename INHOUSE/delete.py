import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_names, delete_data,show_project,delete_project


def delete():
    
    result1 = view_all_data(1)
    result2 = view_all_data(2)
    result3 = view_all_data(3)
    result4 = view_all_data(4)
    result5 = view_all_data(5)
    result6 = view_all_data(6)
    result7 = view_all_data(7)
    # st.write(result)
    
    df2= pd.DataFrame(result1, columns=['DEPT_ID','DEPARTMENT_NAME','LOCATION'])
    df1 = pd.DataFrame(result2, columns=['EMP_ID','FIRST_NAME','LAST_NAME','ROLE_ID','MANAGER_ID','dept_id','Date-of-join'])
   # df3 = pd.DataFrame(result3, columns=['Department_Id','Department_Name','First_Name','Last_Name','Location'])
    #df4 = pd.DataFrame(result4, columns=['No of employee','Title','Project Manager First_name','Project Manager Last_name'])
    #df5 = pd.DataFrame(result5, columns=['PROJECT_ID','EMPLOYEE_ID'])
    #df6 = pd.DataFrame(result6, columns=['ROLE_ID','SALARY','TITLE'])
    #df7 = pd.DataFrame(result, columns=['EMP_ID',';FIRST_NAME','LAST_NAME','ROLE_ID','MANAGER_ID'])
    with st.expander("View all Employees"):
        st.dataframe(df1)
    list_of_trains = [i[0] for i in view_only_train_names(2)]
    selected_train = st.selectbox("Emp to Delete", list_of_trains)
    st.warning("Do you want to delete ::{}".format(selected_train))
    if st.button("Delete Employee"):
        delete_data(selected_train)
        st.success("Employee has been deleted successfully")
    
    with st.expander("View all Department"):
        st.dataframe(df1)
    list_of_trains = [i[0] for i in view_only_train_names(2)]
    selected_train = st.selectbox("Department to Delete", list_of_trains)
    st.warning("Do you want to delete ::{}".format(selected_train))
    if st.button("Delete Department"):
        delete_data(selected_train)
        st.success("Deparment has been deleted successfully")

    with st.expander("View all Project"):
        st.dataframe(df1)
    list_of_trains = [i[0] for i in show_project()]
    selected_train = st.selectbox("Project to Delete", list_of_trains)
    st.warning("Do you want to delete ::{}".format(selected_train))
    if st.button("Delete Project"):
        delete_project(selected_train)
        st.success("Project has been deleted successfully")
