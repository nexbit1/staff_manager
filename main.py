import mysql.connector
sql_password = ""
#create a database in mysql
database_name = ""

con = mysql.connector.connect(
    host="localhost", user="root", password=f"{sql_password}", database=f"{database_name}")
if con.is_connected():
    print('Connection succesfully')

def add_member():
    staff_id = int(input('Check Staff ID if exists: '))
    if check_member(staff_id):
        print("Member exists in Database")
    else:
        print("new staff, add details")
        STAFF_ID = staff_id
        FIRST_NAME = input('first name: ')
        LAST_NAME = input('last name: ')
        SALARY = float(input('salary: '))
        JOINING_DATE = int(input('joining date (dd/mm/yyyy): '))
        DEPARTMENT = input('department: ')
        add_department(DEPARTMENT)
        CONTACT_NUM = input('contact number: ')
        data = (STAFF_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT, CONTACT_NUM)
        cursor = con.cursor()
        query = f"INSERT INTO STAFF VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        con.commit()
        print("Succesfully added")

    menu()

def delete_member():
    staff_id = int(input('Enter staff ID: '))

    if not check_member(staff_id):
        print("Member not in database")
    else:
        query = "DELETE FROM STAFF WHERE STAFF_ID=%s"
        cursor = con.cursor()
        data = (staff_id, )
        cursor.execute(query, data)
        con.commit()
        print('Member Removed')

    menu()


def check_member(staff_id):
    query = "SELECT * FROM STAFF WHERE STAFF_ID=%s"
    cursor = con.cursor(buffered=True)
    data = (staff_id, )
    cursor.execute(query, data)
    if cursor.rowcount == 1:
        return True
    else:
        return False

def display_members():
    query = "SELECT * FROM STAFF"
    cursor = con.cursor()
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i)

    menu()

def check_department(department):
    query = "SELECT * FROM DEPARTMENT WHERE DEPARTMENT_NAME=%s"
    cursor = con.cursor(buffered=True)
    data = (department, )
    cursor.execute(query, data)
    if cursor.rowcount == 1:
        return True
    else:
        return False

def add_department(department_name):
    data = (department_name, )

    if check_department(department_name):
        print('Department Already in database')
    else:
        cursor = con.cursor()
        query = "INSERT INTO DEPARTMENT VALUES(%s)"
        cursor.execute(query, data)
        con.commit()
        print(" New department Succesfully added")

def display_department_members():
    query = "SELECT * FROM DEPARTMENT"
    cursor = con.cursor()
    cursor.execute(query)
    for i in cursor.fetchall():
        print(i[0])
    department_name = input("Choose department name: ")
    query1 = "SELECT * FROM STAFF WHERE DEPARTMENT=%s"
    data = (department_name, )
    c = con.cursor()
    c.execute(query1, data)
    print(f"All members from {department_name} department.")
    for i in c.fetchall():
        print(i)


def menu():
    print("Press ")
    print("1 to Add member")
    print("2 to Remove member ")
    print("3 to Display members")
    print("4 to choose specific department members")
    print("5 to Exit")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        add_member()
    elif ch == 2:
        delete_member()
    elif ch == 3:
        display_members()
    elif ch == 4:
        display_department_members()
    elif ch == 5:
        exit(0)
    else:
        print("Invalid Choice")
        menu()

menu()