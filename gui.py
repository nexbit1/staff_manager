from tkinter import *
from tkinter import ttk
import mysql.connector

sql_password = ""
#create a database in mysql
database_name = ""


class staff:
    def __init__(self, root):
        self.root = root
        self.root.title('GROCERY STORE')
        self.root.geometry("1300x700+0+0")

        title=Label(self.root, text='GROCERY STORE',bd=10,relief=GROOVE , font=("times new roman", 40, "bold"), bg="#CEE5D0",fg="#2B7A0B")
        title.pack(side=TOP, fill=X)

        self.STAFF_ID_VAR = StringVar()
        self.FIRST_NAME_VAR = StringVar()
        self.LAST_NAME_VAR = StringVar()
        self.SALARY_VAR = StringVar()
        self.JOINING_DATE = StringVar()
        self.DEPARTMENT = StringVar()
        self.CONTACT_NUM = StringVar()


        self.search_department = StringVar()






#MANAGE FRAME
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#E9EFC0")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_Frame, text='MANAGE STAFF',bg="#CEE5D0",fg="#2B7A0B", font=("times new roman",30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

#staff_id
        lbl_STAFF_ID = Label(Manage_Frame, text='STAFF ID', bg="#CEE5D0",fg="#2B7A0B", font=("times new roman",20, "bold"))
        lbl_STAFF_ID.grid(row=1, column=0,pady=10, padx=20, sticky='w')
        txt_STAFF_ID = Entry(Manage_Frame,textvariable=self.STAFF_ID_VAR, font=("times new roman",20, "bold"), bd=5, relief=GROOVE)
        txt_STAFF_ID.grid(row=1, column=1,pady=10, padx=20, sticky='w')
#first_name
        lbl_FIRST_NAME = Label(Manage_Frame, text='FIRST NAME', bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lbl_FIRST_NAME.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        txt_FIRST_NAME = Entry(Manage_Frame, textvariable=self.FIRST_NAME_VAR ,font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_FIRST_NAME.grid(row=2, column=1, pady=10, padx=20, sticky='w')
#last_name
        lb1_LAST_NAME = Label(Manage_Frame, text='LAST NAME', bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lb1_LAST_NAME.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        txt_LAST_NAME = Entry(Manage_Frame, textvariable=self.LAST_NAME_VAR, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_LAST_NAME.grid(row=3, column=1, pady=10, padx=20, sticky='w')
#salary
        lb1_SALARY = Label(Manage_Frame, text='SALARY', bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lb1_SALARY.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        txt_SALARY = Entry(Manage_Frame, textvariable=self.SALARY_VAR,font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_SALARY.grid(row=4, column=1, pady=10, padx=20, sticky='w')
#joining date
        lb1_JOINING_DATE = Label(Manage_Frame, text="JOINING DATE", bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lb1_JOINING_DATE.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        txt_JOINING_DATE = Entry(Manage_Frame, textvariable=self.JOINING_DATE,font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_JOINING_DATE.grid(row=5, column=1, pady=10, padx=20, sticky='w')
#department
        lb1_DEPARTMENT = Label(Manage_Frame, text='DEPARTMENT', bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lb1_DEPARTMENT.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        # txt_DEPARTMENT = Entry(Manage_Frame, font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        # txt_DEPARTMENT.grid(row=6, column=1, pady=10, padx=20, sticky='w')

        combo_DEPARTMENT = ttk.Combobox(Manage_Frame, textvariable=self.DEPARTMENT, font=("times new roman", 20, "bold"))
        combo_DEPARTMENT['values'] = ('dairy', 'vegetables', 'fruits')
        combo_DEPARTMENT.grid(row=6, column=1, pady=10, padx=20, sticky='w')
#contact_num
        lb1_CONTACT_NUM = Label(Manage_Frame, text='CONTACT NO.', bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lb1_CONTACT_NUM.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        txt_CONTACT_NUM = Entry(Manage_Frame, textvariable=self.CONTACT_NUM,font=("times new roman", 20, "bold"), bd=5, relief=GROOVE)
        txt_CONTACT_NUM.grid(row=7, column=1, pady=10, padx=20, sticky='w')
#button
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="#E9EFC0")
        btn_Frame.place(x=10, y=500, width=430)

        delete_btn = Button(btn_Frame, text="DELETE", command=self.delete, width=10).grid(row=0, column=0, padx=50, pady=10)
        update_btn = Button(btn_Frame,command=self.update,text="UPDATE", width=10).grid(row=0, column=1, padx=10, pady=10)


        #TABULAR VIEW DETAIL FRAME
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#E9EFC0")
        Detail_Frame.place(x=500, y=100, width=770, height=580)


        lbl_search = Label(Detail_Frame, text='SEARCH DEPARTMENT', bg="#CEE5D0", fg="#2B7A0B",
                             font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=18, sticky='w')

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_department, font=("times new roman", 20, "bold"))
        combo_search['values'] = ('dairy', 'vegetables', 'fruits')
        combo_search.grid(row=0, column=1, pady=10, padx=18, sticky='w')
        search_btn = Button(Detail_Frame,command=self.fetch_department_data,text="SEARCH", width=7).grid(row=0, column=2, padx=8, pady=10)
        viewall_btn = Button(Detail_Frame,command=self.fetch_data, text="VIEW ALL", width=7).grid(row=0, column=3, padx=10, pady=10)

#table
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='#E9EFC0')
        Table_Frame.place(x=10, y=70, width=740, height=480)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.staff_table = ttk.Treeview(Table_Frame, columns=('STAFF_ID', 'FIRST_NAME', 'LAST_NAME', 'SALARY', 'JOINING_DATE', 'DEPARTMENT', 'CONTACT_NUM'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)
        self.staff_table.heading("STAFF_ID", text="STAFF_ID")
        self.staff_table.heading("FIRST_NAME", text="FIRST_NAME")
        self.staff_table.heading("LAST_NAME", text="LAST_NAME")
        self.staff_table.heading("SALARY", text="SALARY")
        self.staff_table.heading("JOINING_DATE", text="JOINING_DATE")
        self.staff_table.heading("DEPARTMENT", text="DEPARTMENT")
        self.staff_table.heading("CONTACT_NUM", text="CONTACT_NUM")
        self.staff_table['show'] = 'headings'
        self.staff_table.column("STAFF_ID", width=100)
        self.staff_table.column("FIRST_NAME", width=150)
        self.staff_table.column("LAST_NAME", width=150)
        self.staff_table.column("SALARY", width=100)
        self.staff_table.column("JOINING_DATE", width=100)
        self.staff_table.column("DEPARTMENT", width=100)
        self.staff_table.column("CONTACT_NUM", width=150)

        self.staff_table.bind("<ButtonRelease-1>", self.get_data)

        self.staff_table.pack(fill=BOTH, expand = 1)
        self.fetch_data()


    def fetch_data(self):
        con = mysql.connector.connect(
            host="localhost", user="root", password=f"{sql_password}", database=f"{database_name}")
        cursor = con.cursor()
        query = "SELECT * FROM STAFF"
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert("",END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.STAFF_ID_VAR.set("")
        self.FIRST_NAME_VAR.set("")
        self.LAST_NAME_VAR.set("")
        self.SALARY_VAR.set("")
        self.JOINING_DATE.set("")
        self.DEPARTMENT.set("")
        self.CONTACT_NUM.set("")

    def get_data(self, event):
        data = self.staff_table.focus()
        content = self.staff_table.item(data)
        row = content['values']
        self.STAFF_ID_VAR.set(row[0])
        self.FIRST_NAME_VAR.set(row[1])
        self.LAST_NAME_VAR.set(row[2])
        self.SALARY_VAR.set(row[3])
        self.JOINING_DATE.set(row[4])
        self.DEPARTMENT.set(row[5])
        self.CONTACT_NUM.set(row[6])

    def delete(self):
        con = mysql.connector.connect(
            host="localhost", user="root", password=f"{sql_password}", database=f"{database_name}")
        cursor = con.cursor()
        query = "DELETE FROM STAFF WHERE STAFF_ID=%s"
        data = (self.STAFF_ID_VAR,)
        cursor.execute(query,data)
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def update(self):
        con = mysql.connector.connect(
            host="localhost", user="root", password=f"{sql_password}", database=f"{database_name}")
        cursor = con.cursor()
        data = (self.FIRST_NAME_VAR.get(), self.LAST_NAME_VAR.get(), self.SALARY_VAR.get(), self.JOINING_DATE.get(), self.DEPARTMENT.get(), self.CONTACT_NUM.get(), self.STAFF_ID_VAR.get())
        query = "UPDATE STAFF SET FIRST_NAME=%s,LAST_NAME=%s,SALARY=%s,JOINING_DATE=%s, DEPARTMENT=%s, CONTACT_NUM=%s WHERE STAFF_ID=%s,"
        cursor.execute(query, data)
        con.commit()
        self.fetch_data()
        self.clear()


    def fetch_department_data(self):
        con = mysql.connector.connect(
            host="localhost", user="root", password=f"{sql_password}", database=f"{database_name}")
        cursor = con.cursor()
        query = "SELECT * FROM STAFF WHERE DEPARTMENT=%s"
        data = (self.search_department.get(),)
        cursor.execute(query, data)
        rows = cursor.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert("", END, values=row)
            con.commit()
        con.close()




root = Tk()
ob = staff(root)
root.mainloop()