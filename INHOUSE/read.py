import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data ,view_pie
import streamlit as st
import matplotlib.pyplot as plt


def read():
    result1 = view_all_data(1)
    result2 = view_all_data(2)
    result3 = view_all_data(3)
    result4 = view_all_data(4)
    result5 = view_all_data(5)
    result6 = view_all_data(6)
    result7 = view_all_data(7)
    # st.write(result)
    df1= pd.DataFrame(result1, columns=['DEPT_ID','DEPARTMENT_NAME','LOCATION'])
    df2 = pd.DataFrame(result2, columns=['EMP_ID','FIRST_NAME','LAST_NAME','ROLE_ID','MANAGER_ID','Dept_id','Date-of-Join'])
    df3 = pd.DataFrame(result3, columns=['Employee_id','Department_Id','Department_Name','First_Name','Last_Name','Location'])
    df4 = pd.DataFrame(result4, columns=['No of employee','Title','Project Manager First_name','Project Manager Last_name','Employee-id'])
    df5 = pd.DataFrame(result5, columns=['PROJECT_ID','EMPLOYEE_ID'])
    df6 = pd.DataFrame(result6, columns=['ROLE_ID','SALARY','TITLE'])
    #df7 = pd.DataFrame(result, columns=['EMP_ID',';FIRST_NAME','LAST_NAME','ROLE_ID','MANAGER_ID'])
    with st.expander("View all Department"):
        st.dataframe(df1)

    with st.expander("View all Employee"):
        st.dataframe(df2)
    with st.expander("View all Manager"):
        st.dataframe(df3)
    with st.expander("View all Project"):
        st.dataframe(df4)
    with st.expander("View all Project_Manager"):
        st.dataframe(df5)
    with st.expander("View all Role"):
        st.dataframe(df6)    

    result=view_pie()
    df=pd.DataFrame(result,columns=["Count","Department_Count"])
    task_df=df["Department_Count"].value_counts().to_frame()
    task_df = task_df.reset_index()
    st.dataframe(task_df)
    p1 = px.pie(task_df, names='index', values='Department_Count')
    st.plotly_chart(p1)
    