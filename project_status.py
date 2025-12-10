from tkinter import *
from tkinter import ttk

class ProjectStatus:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Status")
        self.root.geometry("1530x780+0+0")
        self.root.resizable(0, 0)
        self.root.configure(bg="#F5F5F5")  # Light gray background

        # ===== Title Label =====
        title_label = Label(self.root, text="Project Status", font=("Helvetica", 28, "bold"), bg="#2A3E5C", fg="white")
        title_label.pack(side=TOP, fill=X)

        # ===== Search Section =====
        lbl_search = Label(self.root, text="Search by", font=("Helvetica", 18), fg="#2A3E5C", bg="#F5F5F5")
        lbl_search.place(x=390, y=100)

        self.txt_search = Entry(self.root, font=("Helvetica", 18), bg="#EDEDED", fg="gray")
        self.txt_search.place(x=520, y=100, width=330, height=40)
        self.txt_search.insert(0, "Employee ID")  # Set initial placeholder

        # Placeholder text functionality
        self.txt_search.bind("<FocusIn>", self.clear_placeholder)
        self.txt_search.bind("<FocusOut>", self.add_placeholder)

        # Search Button with styling
        btn_search = Button(self.root, text="Search", font=("Helvetica", 16), bg="blue", fg="white",
                            cursor="hand2", activebackground="#006666", activeforeground="white",
                            bd=1, relief="solid")
        btn_search.place(x=870, y=100, width=150, height=40)

        # Clear Button with styling
        btn_clear = Button(self.root, text="Clear", font=("Helvetica", 16), bg="red", fg="white",
                           cursor="hand2", activebackground="#444444", activeforeground="white",
                           bd=1, relief="solid", command=self.clear_search)
        btn_clear.place(x=1035, y=100, width=150, height=40)

        # Styling Treeview
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview.Heading", font=("Helvetica", 15, "bold"), foreground="#2A3E5C")
        style.configure("Treeview", font=("Helvetica", 14), background="#F9F9F9", foreground="black", rowheight=30)
        style.map("Treeview", background=[("selected", "#008080")], foreground=[("selected", "white")])

        # ===== Table Frame =====
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="#F5F5F5")
        self.C_Frame.place(x=20, y=180, width=1490, height=550)

        # Scrollbar setup
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)

        # Treeview for displaying project information
        self.projectTable = ttk.Treeview(self.C_Frame, columns=("ProjectID", "ProjectName", "ManagerID","ManagerName", "EmployeeID", "EmployeeName", "status"),
                                         show='headings', xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.projectTable.xview)
        scrolly.config(command=self.projectTable.yview)

        # Define headings and columns for the Treeview
        self.projectTable.heading("ProjectID", text="Project ID")
        self.projectTable.heading("ProjectName", text="Project Name")
        self.projectTable.heading("ManagerID", text="Manager ID")
        self.projectTable.heading("ManagerName", text="Manager Name")
        self.projectTable.heading("EmployeeID", text="Employee ID")
        self.projectTable.heading("EmployeeName", text="Employee Name")
        self.projectTable.heading("status", text="Status")

        self.projectTable.column('ProjectID', width=100)
        self.projectTable.column('ProjectName', width=170)
        self.projectTable.column('ManagerID', width=100)
        self.projectTable.column('ManagerName', width=170)
        self.projectTable.column('EmployeeID', width=100)
        self.projectTable.column('EmployeeName', width=170)
        self.projectTable.column('status', width=100)

        self.projectTable.pack(fill=BOTH, expand=1)

    # ===== Placeholder Functions =====
    def clear_placeholder(self, event):
        if self.txt_search.get() == "Employee ID":
            self.txt_search.delete(0, 'end')
            self.txt_search.config(fg="black")  # Change text color when active

    def add_placeholder(self, event):
        if not self.txt_search.get():
            self.txt_search.insert(0, "Employee ID")
            self.txt_search.config(fg="gray")  # Change text color back to gray

    # ===== Clear Function =====
    def clear_search(self):
        self.txt_search.delete(0, 'end')
        self.add_placeholder(None)  # Reset placeholder text

# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = ProjectStatus(root)
    root.mainloop()
