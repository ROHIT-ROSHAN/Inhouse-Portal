# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inhouse"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employee(EMP_ID INT,FIRST_NAME VARCHAR(30),LAST_NAME VARCHAR(30),ROLE_ID INT,MANAGER_ID INT)')

def add_data1(emp_id,first_name,last_name,role_id,manager_id,dept_id,doj):
    c.execute('INSERT INTO employees(EMP_ID,FIRST_NAME,LAST_NAME,ROLE_ID,MANAGER_ID,dept_id,`Date-of-Join` ) VALUES (%s,%s,%s,%s,%s,%s,%s)',(emp_id,first_name,last_name,role_id,manager_id,dept_id,doj))
    mydb.commit()

def add_data2(role_id,salary,title):
    c.execute('INSERT INTO role(role_id,salary,title) VALUES (%s,%s,%s)',(role_id,salary,title))
    mydb.commit()

def add_data3(dept_id,department_name,location):
    c.execute('INSERT INTO departments(dept_id,department_name,location ) VALUES (%s,%s,%s)',(dept_id,department_name,location))
    mydb.commit()

def add_data4(id,department_id):
    c.execute('INSERT INTO manager(manager_id,department_id ) VALUES (%s,%s)',(id,department_id))
    mydb.commit()

def add_data5(project_id,employee_id):
    c.execute('INSERT INTO project_manager(project_id,employee_id ) VALUES (%s,%s)',(project_id,employee_id))
    mydb.commit()

def add_data6(project_id,no_of_employee,role_id,id):
    c.execute('INSERT INTO project(project_id,no_of_employee,role_id,project_manager_id) VALUES (%s,%s,%s,%s)',(project_id,no_of_employee,role_id,id))
    mydb.commit()        


def view_all_data(num):
    if num==1:
        c.execute('SELECT * FROM departments')
        data = c.fetchall()
        return data
    if num==2:
        c.execute('SELECT * FROM Employees ')
        data = c.fetchall()
        return data
    if num==3:
        c.execute('SELECT E.emp_id, M.Department_ID,D.DEPARTMENT_NAME,E.First_Name,E.Last_Name,D.Location FROM Departments AS D JOIN manager AS M ON D.Dept_ID = M.Department_ID JOIN Employees AS E ON M.manager_id = E.Emp_ID')
        data = c.fetchall()
        return data
    if num==4:
        c.execute('SELECT P.no_of_employee,P.Title,E.First_name,E.Last_name,E.emp_id from project as P join Employees as E on P.project_manager_id=E.emp_id')
        data = c.fetchall()
        return data
    if num==5:
        c.execute('SELECT E.First_name ,E.last_name from Employees as E join Project as P on P.project_manager_id=E.emp_id')
        data = c.fetchall()
        return data
    if num==6:
        c.execute('SELECT * FROM role')
        data = c.fetchall()
        return data

def view_pie():
    c.execute("select e.dept_id,d.department_name from employees as e , departments as d where e.dept_id=d.dept_id")                   
    data=c.fetchall()
    return data

def view_only_train_names(num):
    if num==1:
        c.execute('SELECT * from Departments')
        data = c.fetchall()
        return data
    
    if num==2:
        c.execute('SELECT * from Employees')
        data = c.fetchall()
        return data

    if num==3:
        c.execute('SELECT E.emp_id, M.Department_ID,D.DEPARTMENT_NAME,E.First_Name,E.Last_Name,D.Location FROM Departments AS D JOIN manager AS M ON D.Dept_ID = M.Department_ID JOIN Employees AS E ON M.manager_id = E.Emp_ID')
        data = c.fetchall()
        return data    
    
    if num==4:
        c.execute('SELECT P.no_of_employee,P.Title,E.First_name,E.Last_name,E.emp_id from project as P join Employees as E on P.project_manager_id=E.emp_id')

        data = c.fetchall()
        return data 

    if num==5:
        c.execute('SELECT * from Departments')
        data = c.fetchall()
        return data   

    if num==6:
        c.execute('SELECT * from Departments')
        data = c.fetchall()
        return data        

def get_train(department_name):
    
    c.execute('SELECT * FROM departments WHERE department_name="{}"'.format(department_name))
    data = c.fetchall()
    return data

def get_employee(department_name):
    #'SELECT M.Department_ID,D.DEPARTMENT_NAME,E.First_Name,E.Last_Name,D.Location FROM Departments AS D JOIN manager AS M ON D.Dept_ID = M.Department_ID JOIN Employees AS E ON M.manager_id = E.Emp_ID'
    c.execute('SELECT * from employees where first_name="{}"'.format(department_name))
    data = c.fetchall()
    return data    

def get_manager(department_name):

    c.execute('SELECT E.emp_id, M.Department_ID,D.DEPARTMENT_NAME,E.First_Name,E.Last_Name,D.Location FROM Departments AS D JOIN manager AS M ON D.Dept_ID = M.Department_ID JOIN Employees AS E ON M.manager_id = E.Emp_ID and E.emp_id="{}" '.format(department_name))
    data = c.fetchall()
    return data
def get_pm(department_name):
    c.execute('SELECT P.no_of_employee,P.Title,E.First_name,E.Last_name,E.emp_id from project as P join Employees as E on P.project_manager_id=E.emp_id and P.Title="{}"'.format(department_name))
    data = c.fetchall()
    return data
def edit_train_data(id,name,location,dept_id,department_name,department_location):
    
        c.execute("UPDATE departments SET dept_id=%s,department_Name=%s, location=%s   WHERE dept_id=%s and department_Name=%s and  location=%s", (id,name,location,dept_id,department_name,department_location))
        mydb.commit()
        data = c.fetchmany()
        return data
        
def edit_employee(id,emp_dept_name,emp_first_name,emp_last_name,new_location,dept_id,dept_name,first_name,last_name,location):

    
        c.execute("UPDATE employees SET emp_id=%s,first_Name=%s, last_name=%s ,role_id=%s,manager_id=%s  WHERE emp_id=%s AND first_Name=%s AND last_name=%s AND role_id=%s AND manager_id=%s",(id,emp_dept_name,emp_first_name,emp_last_name,new_location,dept_id,dept_name,first_name,last_name,location))
        mydb.commit()
        data = c.fetchmany()
        return data        
    
def edit_manager(id,first_name,last_name,dept_id,firstname,lastname):
        c.execute("UPDATE employees  SET dept_id=%s,first_Name=%s, last_name=%s   WHERE dept_id=%s AND first_Name=%s AND last_name=%s ",(id,first_name,last_name,dept_id,firstname,lastname))
        mydb.commit()
        data = c.fetchmany()
        return data  
    
def edit_pm(id,first_name,emp_id,dept_id):
    c.execute("UPDATE project  SET no_of_employee=%s,title=%s WHERE no_of_employee=%s and title=%s ",(id,first_name,emp_id,dept_id))
    mydb.commit()
    data = c.fetchmany()
    return data 

def delete_data(train_name):
    c.execute('DELETE FROM employees WHERE emp_id="{}"'.format(train_name))
    mydb.commit()

def show_project():
    c.execute('Select * from project')
    data = c.fetchall()
    return data

def delete_project(train_name):
    
    c.execute('DELETE FROM project WHERE project_id="{}"'.format(train_name))
    
    mydb.commit()    