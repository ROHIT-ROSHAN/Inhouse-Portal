import datetime
import pandas as pd
import streamlit as st
from database import view_all_data, view_only_train_names, get_train, edit_train_data,edit_employee,get_employee,get_manager,edit_manager,get_pm,edit_pm


def update():
    result1 = view_all_data(1)
    result2 = view_all_data(2)
    result3 = view_all_data(3)
    result4 = view_all_data(4)
    # result5 = view_all_data(5)
    # result6 = view_all_data(6)
    # result7 = view_all_data(7)
    # st.write(result)
    df1= pd.DataFrame(result1, columns=['DEPT_ID','DEPARTMENT_NAME','LOCATION'])
    df2 = pd.DataFrame(result2, columns=['EMP_ID','FIRST_NAME','LAST_NAME','ROLE_ID','MANAGER_ID','Dept_id','Date-of-join'])
    df3 = pd.DataFrame(result3, columns=['EMP_ID','Department_Id','Department_Name','First_Name','Last_Name','Location'])
    df4 = pd.DataFrame(result4, columns=['No of employee','Title','Project Manager First_name','Project Manager Last_name','Emp_id'])
    # df5 = pd.DataFrame(result5, columns=['PROJECT_ID','EMPLOYEE_ID'])
    # df6 = pd.DataFrame(result6, columns=['ROLE_ID','SALARY','TITLE'])
    


    #department
    with st.expander("View all Departments"):
        st.dataframe(df1)
    
    list_of_employees = [i[1] for i in view_only_train_names(1)]
    selected_train = st.selectbox("Deparment To edit", list_of_employees)
    selected_result = get_train(selected_train)
    
    if selected_result:
        dept_id = selected_result[0][0]
        department_name = selected_result[0][1]
        department_location = selected_result[0][2]
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            id = st.text_input("Dept ID", dept_id)
            name = st.text_input("Department Name:",department_name)
            
        with col2:
            location = st.text_input("Department Location",department_location)
            
        if st.button("Update Department"):
            edit_train_data(id,name,location,dept_id,department_name,department_location)
            st.success("Successfully updated:: {} to ::{}".format(department_name, name))

    #Employee
    with st.expander("View all  Employees"):
        st.dataframe(df2)
    
    list_of_employees = [i[1] for i in view_only_train_names(2)]
    selected_train = st.selectbox("Employee to  Edit", list_of_employees)
    selected_result = get_employee(selected_train)
   
    if selected_result:
        dept_id = selected_result[0][0]
        dept_name = selected_result[0][1]
        first_name = selected_result[0][2]
        last_name = selected_result[0][3]
        location=selected_result[0][4]
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            id = st.text_input("EMP ID:", dept_id)
            emp_dept_name = st.text_input("first  Name:",dept_name)
            emp_first_name = st.text_input("last:",first_name)
            
        with col2:
            emp_last_name = st.text_input("Role id",last_name)
            new_location=st.text_input("Manager id",location)
            
        if st.button("Update Employee"):
            edit_employee(id,emp_dept_name,emp_first_name,emp_last_name,new_location,dept_id,dept_name,first_name,last_name,location)
            st.success("Successfully updated:: {} ".format(id))


    #manager
    with st.expander("View all  Manager"):
        st.dataframe(df3)
    
    list_of_employees = [i[0] for i in view_only_train_names(3)]
    selected_train = st.selectbox("Choose Manager EMP_ID To edit", list_of_employees)
    selected_result = get_manager(selected_train)
    
    if selected_result:
        #emp_id= selected_result[0][0]
        dept_id = selected_result[0][1]
        #dept_name = selected_result[0][2]
        firstname = selected_result[0][3]
        lastname = selected_result[0][4]
        #location=selected_result[0][5]
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            id = st.text_input("Dept ID:", dept_id)
            
          
        with col2:
            first_name = st.text_input("First Name:",firstname)
            last_name = st.text_input("last Name:",lastname)
            
            
            
        if st.button("Update Manager"):
            edit_manager(id,first_name,last_name,dept_id,firstname,lastname)
            st.success("Successfully updated:: {} ".format(id))        

    with st.expander("View all Project"):
        st.dataframe(df4)

    list_of_employees = [i[1] for i in view_only_train_names(4)]
    selected_train = st.selectbox("Project manager detail To edit", list_of_employees)
    selected_result = get_pm(selected_train)  
    
    if selected_result:
        emp_id= selected_result[0][0]
        dept_id = selected_result[0][1]
        
        # Layout of Create
        col1, col2 = st.columns(2)
        with col1:
            id = st.text_input("No of employee:", emp_id)
            
          
        with col2:
            first_name = st.text_input("Title:",dept_id)
            
            
            
            
        if st.button("Update Project Manager"):
            edit_pm(id,first_name,emp_id,dept_id)
            st.success("Successfully updated:: {} ".format(id))          