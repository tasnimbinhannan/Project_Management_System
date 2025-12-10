from tkinter import *
from tkinter import ttk  # Import ttk for Combobox & scrollbar

class Project:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Page")
        self.root.geometry('1530x780+0+0')
        self.root.resizable(0, 0)
        self.root.config(bg='midnight blue')

        # Title label
        self.title = Label(self.root, text='Manage Project Details', font=('goudy old style', 20, 'bold'), bg='slateblue1', fg='white')
        self.title.place(x=10, y=15, width=1510, height=50)

        # Create a leftFrame section on the Left side
        self.leftFrame = Frame(self.root, width=478, height=500, bg='midnight blue')
        self.leftFrame.place(x=10, y=120)

        # Project ID
        self.ProjectID = Label(self.leftFrame, text='Project ID', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.ProjectID.place(x=20, y=30)
        self.ProjectID_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.ProjectID_entry.place(x=220, y=30, height=32)

        # Project Name
        self.ProjectName = Label(self.leftFrame, text='Project Name', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.ProjectName.place(x=20, y=130)
        self.ProjectName_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.ProjectName_entry.place(x=220, y=130, height=32)

        # Duration 
        self.duration = Label(self.leftFrame, text='Duration', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.duration.place(x=20, y=230)
        self.duration_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.duration_entry.place(x=220, y=230, height=32)

        # Status
        self.status = Label(self.leftFrame, text='Status', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.status.place(x=20, y=330)
        self.status_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.status_entry.place(x=220, y=330, height=32)

        #  Manager ID
        self.ManagerID = Label(self.leftFrame, text='Manager ID', font=('goudy old style', 18, 'bold'), bd=0, bg='midnight blue', fg='white')
        self.ManagerID.place(x=20, y=430)
        self.ManagerID_entry = Entry(self.leftFrame, width=23, font=('goudy old style', 14), bg='light yellow', fg='black')
        self.ManagerID_entry.place(x=220, y=430, height=32)

        # BOTTOM Frame
        self.ButtonFrame = Frame(self.root, width=1388, height=45, bg='midnight blue')
        self.ButtonFrame.place(x=71, y=690)

        # New Project button
        self.newProject_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='New Project', bg='slateblue1', cursor="hand2", fg='white', border=2)
        self.newProject_button.place(x=20, y=3, height=40)

        # Add Project button
        self.addProject_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Add Project', bg='slateblue1', cursor="hand2", fg='white', border=2)
        self.addProject_button.place(x=302, y=3, height=40)

        # Update Project button
        self.updateProject_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Update Project', bg='slateblue1', cursor="hand2", fg='white', border=1)
        self.updateProject_button.place(x=583, y=3, height=40)

        # Delete Project button
        self.deleteProject_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Delete Project', bg='slateblue1', cursor="hand2", fg='white', border=2)
        self.deleteProject_button.place(x=864, y=3, height=40)

        # Delete All button
        self.deleteAll_button = Button(self.ButtonFrame, font=('Open Sans', 14, 'bold'), width=15, pady=1, text='Delete All', bg='slateblue1', cursor="hand2", fg='white', border=2)
        self.deleteAll_button.place(x=1146, y=3, height=40)

        # Search Frame
        self.searchFrame = Frame(self.root, width=900, height=40, bg='white')
        self.searchFrame.place(x=600, y=133)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("TCombobox", fieldbackground="light yellow", background="light yellow", foreground="black")

        # Combobox for searching
        search_options = ['Project Name', 'Project ID', 'Duration', 'Status', 'Project Manager']
        self.search_by = ttk.Combobox(self.searchFrame, values=search_options, font=('goudy old style', 14), width=16, style="TCombobox")
        self.search_by.set("Search by")
        self.search_by.place(x=20, y=6, height=28)

        self.search_entry = Entry(self.searchFrame, width=16, font=('goudy old style', 14), bg='light yellow', fg='black', bd=2)
        self.search_entry.place(x=265, y=6, height=28)

        self.search_button = Button(self.searchFrame, font=('Open Sans', 14, 'bold'), width=13, pady=1, text='Search', bg='slateblue1', fg='white', cursor="hand2", border=2)
        self.search_button.place(x=498, y=5, height=30)

        self.showAll_button = Button(self.searchFrame, font=('Open Sans', 14, 'bold'), width=13, pady=1, text='Show All', bg='slateblue1', fg='white', cursor="hand2", border=2)
        self.showAll_button.place(x=715, y=5, height=30)

        # Right Frame
        self.C_Frame = Frame(self.root, relief=RIDGE)
        self.C_Frame.place(x=600, y=180, width=900, height=430)

        # Scrollbar setup
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)

        # Configure Treeview style
        style.configure("Custom.Treeview.Heading", font=('goudy old style', 12, 'bold'), foreground='midnight blue')
        style.configure("Custom.Treeview", font=('goudy old style', 12), rowheight=25, foreground='Black', background="light cyan")

        # Treeview setup with scroll commands
        self.projectTable = ttk.Treeview(self.C_Frame, columns=('ProjectID', 'ProjectName', 'duration', 'status', 'ManagerID'), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set, style="Custom.Treeview")

        # Pack scrollbars and set them to the Treeview
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.projectTable.xview)
        scrolly.config(command=self.projectTable.yview)

        # Treeview columns and headers
        self.projectTable.heading('ProjectID', text='Project ID')
        self.projectTable.heading('ProjectName', text='Project Name')
        self.projectTable.heading('duration', text='Duration')
        self.projectTable.heading('status', text='Status')
        self.projectTable.heading('ManagerID', text='Manager ID')
        self.projectTable['show'] = 'headings'

        self.projectTable.column('ProjectID', width=120)
        self.projectTable.column('ProjectName', width=200)
        self.projectTable.column('duration', width=130)
        self.projectTable.column('status', width=130)
        self.projectTable.column('ManagerID', width=120)

        # Pack Treeview
        self.projectTable.pack(fill=BOTH, expand=1)

if __name__ == "__main__":
    root = Tk()
    obj = Project(root)
    root.mainloop()
