from tkinter import *
from tkinter import ttk  # Import ttk for Combobox & scrollbar

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Page")
        self.root.geometry('1530x780+0+0')
        self.root.resizable(0, 0)
        self.root.config(bg='midnight blue')

        # Title label
        self.title = Label(self.root, text='Manage Employee Details', font=('goudy old style', 20, 'bold'), bg='slateblue1', fg='white')
        self.title.place(x=10, y=15, width=1510, height=50)

        # Create a leftFrame section on the Left side
        self.leftFrame = Frame(self.root, width=468, height=500, bg='midnight blue')
        self.leftFrame.place(x=10, y=120)

        # Employee Name
        self.empID = Label(self.leftFrame, text='Employee ID', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.empID.place(x=20, y=20)
        self.empID_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.empID_entry.place(x=210, y=20, height=32)

        # Employee ID
        self.empName = Label(self.leftFrame, text='Employee Name', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.empName.place(x=20, y=105)
        self.empName_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.empName_entry.place(x=210, y=105, height=32)

        # Phone Number
        self.phone = Label(self.leftFrame, text='Phone', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.phone.place(x=20, y=190)
        self.phone_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.phone_entry.place(x=210, y=190, height=32)

        # Gender Combobox
        self.gender = Label(self.leftFrame, text='Gender', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.gender.place(x=20, y=275)
        self.gender_entry = ttk.Combobox(self.leftFrame, values=["Male", "Female"], font=('goudy old style', 14), width=22, style="TCombobox")
        self.gender_entry.set("Male")  # Default value
        self.gender_entry.place(x=210, y=275, height=32)

        # Salary
        self.salary = Label(self.leftFrame, text='Salary', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.salary.place(x=20, y=360)
        self.salary_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.salary_entry.place(x=210, y=360, height=32)

        # Project ID
        self.projectID = Label(self.leftFrame, text='Project ID', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.projectID.place(x=20, y=445)
        self.projectID_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.projectID_entry.place(x=210, y=445, height=32)

        # ButtonFrame
        self.ButtonFrame = Frame(self.root, width=1388, height=45, bg='midnight blue')
        self.ButtonFrame.place(x=71, y=700)

        # New Employee button
        self.newEmp_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='New Employee', bg='slateblue1', fg='white', cursor="hand2", border=2)
        self.newEmp_button.place(x=20, y=3,height=40)

        # Add Employee button
        self.addEmp_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Add Employee', bg='slateblue1', fg='white', cursor="hand2", border=2)
        self.addEmp_button.place(x=302, y=3,height=40)

        # Update Employee button
        self.updateEmp_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Update Employee', bg='slateblue1', fg='white',cursor="hand2", border=1)
        self.updateEmp_button.place(x=583, y=3,height=40)

        # Delete Employee button
        self.deleteEmp_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Delete Employee', bg='slateblue1', fg='white', cursor="hand2", border=2)
        self.deleteEmp_button.place(x=864, y=3,height=40)

        # Delete All button
        self.deleteAll_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Delete All', bg='slateblue1', fg='white', cursor="hand2", border=2)
        self.deleteAll_button.place(x=1146, y=3,height=40)

        # Search Frame
        self.searchFrame = Frame(self.root, width=900, height=40, bg='white')
        self.searchFrame.place(x=600, y=133)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TCombobox", fieldbackground="light yellow", background="light yellow", foreground="black")

        # Combobox for searching
        search_options = ['Employee ID', 'Employee Name', 'Phone', 'Gender', 'Salary', 'Project ID']
        self.search_by = ttk.Combobox(self.searchFrame, values=search_options, font=('goudy old style', 14), width=16, style="TCombobox")
        self.search_by.set("Search by")
        self.search_by.place(x=20, y=6, height=28)

        self.search_entry = Entry(self.searchFrame, width=16, font=('goudy old style', 14), bg='light yellow', fg='black',bd=2)
        self.search_entry.place(x=265, y=6, height=28)

        self.search_button = Button(self.searchFrame, font=('Open Sans', 14, 'bold'), width=13, pady=1, text='Search', bg='slateblue1', cursor="hand2", fg='white', border=2)
        self.search_button.place(x=498, y=5, height=30)

        self.showAll_button = Button(self.searchFrame, font=('Open Sans', 14, 'bold'), width=13, pady=1, text='Show All', bg='slateblue1', cursor="hand2", fg='white', border=2)
        self.showAll_button.place(x=715, y=5, height=30)

        # Right Frame
        self.C_Frame = Frame(self.root, relief=RIDGE)
        self.C_Frame.place(x=600, y=180, width=900, height=430)

        # Scrollbar setup
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)

        # Configure Treeview style
        style.configure("Custom.Treeview.Heading", font=('goudy old style',12, 'bold'), foreground='midnight blue')
        style.configure("Custom.Treeview", font=('goudy old style', 12), rowheight=25, foreground='Black', background="light cyan")

        # Treeview setup with scroll commands
        self.empTable = ttk.Treeview(self.C_Frame, columns=('empID', 'empName', 'phone', 'gender', 'salary', 'ProjectID'),
                                     xscrollcommand=scrollx.set, yscrollcommand=scrolly.set, style="Custom.Treeview")

        # Pack scrollbars and set them to the Treeview
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.empTable.xview)
        scrolly.config(command=self.empTable.yview)

        # Treeview columns and headers
        self.empTable.heading('empID', text='Employee ID')
        self.empTable.heading('empName', text='Employee Name')
        self.empTable.heading('phone', text='Phone')
        self.empTable.heading('gender', text='Gender')
        self.empTable.heading('salary', text='Salary')
        self.empTable.heading('ProjectID', text='Project ID')
        self.empTable['show'] = 'headings'

        self.empTable.column('empID', width=100)
        self.empTable.column('empName', width=140)
        self.empTable.column('phone', width=100)
        self.empTable.column('gender', width=80)
        self.empTable.column('salary', width=80)
        self.empTable.column('ProjectID', width=100)

        self.empTable.pack(fill=BOTH, expand=1)


# Create the main window and run the app
if __name__ == "__main__":
    root = Tk()
    app = Employee(root)
    root.mainloop()