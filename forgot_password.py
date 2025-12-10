from tkinter import *
from PIL import Image, ImageTk

class ForgotPass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x780+0+0')
        self.root.resizable(0, 0)
        self.root.title("Registration Page")

        # Load and display the background image
        bg = Image.open('pictures/bg_forgot_password.jpg').resize((1530, 780))
        self.bg = ImageTk.PhotoImage(bg)
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0)

       

        # Create a white frame section on the right side
        self.frame = Frame(self.bg_label, width=420, height=546, bg='white')
        self.frame.place(x=900, y=130)

        # Load and display the registration icon
        regi_icon = Image.open('pictures/reset_psss icon.png').resize((110, 110))
        self.regi_icon = ImageTk.PhotoImage(regi_icon)
        self.regi_label = Label(self.frame, image=self.regi_icon, bg='white')
        self.regi_label.place(x=160, y=50)

       
        # Add heading for "Reset Password"
        self.heading = Label(self.frame, text='Reset Password', font=('Segoe UI Variable', 25, 'bold'), bg='white', fg='slateblue1')
        self.heading.place(x=80, y=171)





        # Username entry
        self.username_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.username_entry.place(x=44, y=255)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', self.on_enter_username)
        self.username_entry.bind('<FocusOut>', self.on_leave_username)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=280)


        # Password entry
        self.password_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.password_entry.place(x=44, y=315)
        self.password_entry.insert(0, 'New Password')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=340)

      # Confirm_Password entry
        self.confpassword_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.confpassword_entry.place(x=44, y=375)
        self.confpassword_entry.insert(0, 'Confirm Password')
        self.confpassword_entry.bind('<FocusIn>', self.on_enter_confpassword)
        self.confpassword_entry.bind('<FocusOut>', self.on_leave_confpassword)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=400)
        
        # Submit button
        self.signup_button = Button(self.frame, font=('Open Sans', 14, 'bold'), width=28, pady=4, text='Submit', bg='slateblue1', cursor="hand2", fg='white', border=0)
        self.signup_button.place(x=40, y=440)





    # Functions to handle focus events for username entry
    def on_enter_username(self, event):
        self.username_entry.delete(0, 'end')

    def on_leave_username(self, event):
        name = self.username_entry.get()
        if name == '':
            self.username_entry.insert(0, "Username")

    # Functions to handle focus events for new password entry
    def on_enter_password(self, event):
        self.password_entry.delete(0, 'end')

    def on_leave_password(self, event):
        name = self.password_entry.get()
        if name == '':
            self.password_entry.insert(0, "New Password")

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
    app = ForgotPass(root)
    root.mainloop()
