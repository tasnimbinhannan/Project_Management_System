from tkinter import *
from PIL import Image, ImageTk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1530x780+0+0")
        self.root.resizable(0, 0)
        self.root.config(bg='midnight blue')

        # Load and display the background image
        try:
            bg = Image.open('pictures/bg_dash.jpg').resize((1530, 780))
            self.bg = ImageTk.PhotoImage(bg)
            self.bg_label = Label(self.root, image=self.bg)
            self.bg_label.place(x=0, y=0)
        except Exception as e:
            print(f"Error loading background image: {e}")

        # Title label
        self.title = Label(self.root, text='Project Management System', font=('goudy old style', 20, 'bold'), bg='midnight blue', fg='white')
        self.title.place(x=10, y=15, width=1510, height=50)

        # ===== Menu Frame =====
        self.M_Frame = LabelFrame(self.root, bg="midnight blue")
        self.M_Frame.place(x=10, y=80, width=1510, height=70)

        # ===== Buttons =====
        self.btn_Employee = Button(self.M_Frame, text="Employee", font=("Arial", 20, "bold"), bg="red", fg="light yellow", cursor="hand2")
        self.btn_Employee.place(x=20, y=5, width=280, height=55)

        self.btn_Project = Button(self.M_Frame, text="Project", font=("Arial", 20, "bold"), bg="green", fg="light yellow", cursor="hand2")
        self.btn_Project.place(x=410, y=5, width=280, height=55)

        self.btn_Project_Status = Button(self.M_Frame, text="Project Status", font=("Arial", 20, "bold"), bg="blue", fg="light yellow", cursor="hand2")
        self.btn_Project_Status.place(x=810, y=5, width=280, height=55)

        self.btn_Logout = Button(self.M_Frame, text="Logout", font=("Arial", 20, "bold"), bg="#1F487E", fg="light yellow", cursor="hand2")
        self.btn_Logout.place(x=1205, y=5, width=280, height=55)

        # ===== Summary Labels =====
        self.lbl_Employee = Label(self.root, text="Total Employee\n[ 0 ]", font=("Arial", 25), bd=10, relief=RIDGE, bg="midnight blue", fg="light yellow")
        self.lbl_Employee.place(x=530, y=650, width=300, height=110)
        
        self.lbl_total_project = Label(self.root, text="Total Project\n[ 0 ]", font=("Arial", 25), bd=10, relief=RIDGE, bg="midnight blue", fg="light yellow")
        self.lbl_total_project.place(x=850, y=650, width=300, height=110)
        
        self.lbl_ongoing_project = Label(self.root, text="Ongoing Project\n[ 0 ]", font=("Arial", 25), bd=10, relief=RIDGE, bg="midnight blue", fg="white")
        self.lbl_ongoing_project.place(x=1170, y=650, width=300, height=110)

if __name__ == "__main__":
    root = Tk()
    obj = Dashboard(root)
    root.mainloop()
