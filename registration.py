from tkinter import *
from PIL import Image, ImageTk

class Registration:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x780+0+0')
        self.root.resizable(0, 0)
        self.root.title("Registration Page")

        # Load and display the background image
        bg = Image.open('pictures/bg_registration.jpg').resize((1530, 780))
        self.bg = ImageTk.PhotoImage(bg)
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0)

       

        # Create a white frame section on the right side
        self.frame = Frame(self.bg_label, width=420, height=600, bg='white')
        self.frame.place(x=900, y=100)

        # Load and display the registration icon
        regi_icon = Image.open('pictures/registration icon.png').resize((110, 110))
        self.regi_icon = ImageTk.PhotoImage(regi_icon)
        self.regi_label = Label(self.frame, image=self.regi_icon, bg='white')
        self.regi_label.place(x=160, y=30)

       
        # Add heading for "User Login"
        self.heading = Label(self.frame, text='User Registration', font=('Segoe UI Variable', 25, 'bold'), bg='white', fg='slateblue1')
        self.heading.place(x=70, y=140)



        # Email entry
        self.email_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.email_entry.place(x=44, y=220)
        self.email_entry.insert(0, 'Email')
        self.email_entry.bind('<FocusIn>', self.on_enter_email)
        self.email_entry.bind('<FocusOut>', self.on_leave_email)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=245)


        # Username entry
        self.username_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.username_entry.place(x=44, y=280)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', self.on_enter_username)
        self.username_entry.bind('<FocusOut>', self.on_leave_username)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=305)


        # Password entry
        self.password_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.password_entry.place(x=44, y=340)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=365)

      # Confirm_Password entry
        self.confpassword_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.confpassword_entry.place(x=44, y=400)
        self.confpassword_entry.insert(0, 'Confirm Password')
        self.confpassword_entry.bind('<FocusIn>', self.on_enter_confpassword)
        self.confpassword_entry.bind('<FocusOut>', self.on_leave_confpassword)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=425)




        
        # Sign-up button
        self.signup_button = Button(self.frame, font=('Open Sans', 14, 'bold'), width=28, pady=4, text='Sign up', bg='slateblue1', cursor="hand2", fg='white', border=0)
        self.signup_button.place(x=40, y=470)

        # Sign-in prompt
        label_x = Label(self.frame, text="Already have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 11,'bold'))
        label_x.place(x=80, y=520)

        # Sign-in button
        sign_in = Button(self.frame, text='Sign in', bd=0, bg='white', cursor='hand2', fg='slateblue1', font=('Open Sans', 12,))
        sign_in.place(x=280, y=520)


    # Functions to handle focus events for email entry
    def on_enter_email(self, event):
        self.email_entry.delete(0, 'end')

    def on_leave_email(self, event):
        name = self.email_entry.get()
        if name == '':
            self.email_entry.insert(0, "Email")


    # Functions to handle focus events for username entry
    def on_enter_username(self, event):
        self.username_entry.delete(0, 'end')

    def on_leave_username(self, event):
        name = self.username_entry.get()
        if name == '':
            self.username_entry.insert(0, "Username")

    # Functions to handle focus events for password entry
    def on_enter_password(self, event):
        self.password_entry.delete(0, 'end')

    def on_leave_password(self, event):
        name = self.password_entry.get()
        if name == '':
            self.password_entry.insert(0, "Password")

    # Functions to handle focus events for Confirm password entry
    def on_enter_confpassword(self, event):
        self.confpassword_entry.delete(0, 'end')

    def on_leave_confpassword(self, event):
        name = self.confpassword_entry.get()
        if name == '':
            self.confpassword_entry.insert(0, "Confirm Password")


# Create the main window and run the app
if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
