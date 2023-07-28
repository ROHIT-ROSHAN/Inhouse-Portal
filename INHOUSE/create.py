import streamlit as st
from database import add_data1,add_data2,add_data3,add_data4,add_data5,add_data6


def create(num):
    if num==1:
        col1, col2 = st.columns(2)
        with col1:
            emp_id = st.text_input("EMP ID")
            first_name = st.text_input("FIRST Name")
            last_name = st.text_input("Last Name")
            dept_id=st.text_input("dept id")
        
        with col2:
            role_id = st.text_input("Role ID")
            manager_id = st.text_input("MANAGER ID")
            doj=st.text_input("Date-Of-Join")
    
        if st.button("Add Employee"):
            add_data1(emp_id,first_name,last_name,role_id,manager_id,dept_id,doj)
            st.success("Successfully added Employee: {}".format(last_name))
     
    if num==2:
        col1, col2 = st.columns(2)

        with col1:
            role_id = st.text_input("Role id")
            salary = st.text_input("Salary")
            
        
        with col2:
            title = st.text_input("Title")
            
        
    
        if st.button("Add Role"):
            add_data2(role_id,salary,title)
            st.success("Successfully added Role: {}".format(title))
    
    if num==3:
        
        col1, col2 = st.columns(2)

        with col1:
            dept_id = st.text_input("Dept id")
            department_name = st.text_input("Dept Name")
            
        
        with col2:
            location = st.text_input("Location")
            
        
    
        if st.button("Add Department"):
            add_data3(dept_id,department_name,location)
            st.success("Successfully added Role: {}".format(department_name))
                  

    if num==4:
        col1, col2 = st.columns(2)

        with col1:
            id = st.text_input("Manager id")
                      
        
        with col2:
            department_id = st.text_input("Department id")
            
        
    
        if st.button("Add Manager"):
            add_data4(id,department_id)
            st.success("Successfully added Manager: {}".format(id))

    if num==5:
        col1, col2 = st.columns(2)

        with col1:
            project_id = st.text_input("Project id")
            
            
        
        with col2:
            employee_id = st.text_input("Employee id")
            
        
    
        if st.button("Add Project Manger"):
            add_data5(project_id,employee_id)
            st.success("Successfully added Manager: {}".format(employee_id))
    
    if num==6:

        col1, col2 = st.columns(2)

        with col1:
            project_id = st.text_input("Project id")
            no_of_employee = st.text_input("No of employee")
            
        
        with col2:
            role_id = st.text_input("Role id")
            id = st.text_input("Project Manager id")
            
        
    
        if st.button("Add Department"):
            add_data6(project_id,no_of_employee,role_id,id)
            st.success("Successfully added project: {}".format(project_id))