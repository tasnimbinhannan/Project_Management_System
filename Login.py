from tkinter import *
from PIL import Image, ImageTk #pip install pillow

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x780+0+0')
        self.root.resizable(0, 0)
        self.root.title("Login Page")

        # Load and display the background image
        bg = Image.open('pictures/bg_login.jpg').resize((1530, 780))
        self.bg = ImageTk.PhotoImage(bg)
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0)

       

        # Create a white frame section on the right side
        self.frame = Frame(self.bg_label, width=420, height=546, bg='white')
        self.frame.place(x=900, y=130)

        # Load and display the login icon
        signin_icon = Image.open('pictures/login icon.png').resize((120, 120))
        self.signin_icon = ImageTk.PhotoImage(signin_icon)
        self.sign_label = Label(self.frame, image=self.signin_icon, bg='white')
        self.sign_label.place(x=150, y=60)

       
        # Add heading for "User Login"
        self.heading = Label(self.frame, text='User Login', font=('Segoe UI Variable', 25, 'bold'), bg='white', fg='slateblue1')
        self.heading.place(x=123, y=183)

        # Username entry
        self.username_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.username_entry.place(x=44, y=260)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', self.on_enter_username)
        self.username_entry.bind('<FocusOut>', self.on_leave_username)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=285)


        # Password entry
        self.password_entry = Entry(self.frame, width=31, font=('Microsoft Yahei UI Light', 12,'bold'), bd=0, fg='gray')
        self.password_entry.place(x=44, y=320)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)
        Frame(self.frame, width=350, height=2, bg='black').place(x=38, y=345)

   

        #Forgot password button
        forgot_pass = Button(self.frame, text='Forgot Password?', bd=0, bg='white', cursor='hand2', fg='slateblue1', font=('Microsoft Yahei UI Light', 11,'bold'))
        forgot_pass.place(x=240, y=350)


        
        # Sign-in button
        self.signin_button = Button(self.frame, font=('Open Sans', 14, 'bold'), width=28, pady=4, text='Sign in', bg='slateblue1', cursor="hand2", fg='white', border=0)
        self.signin_button.place(x=40, y=410)

        # Sign-up prompt
        label_x = Label(self.frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 11,'bold'))
        label_x.place(x=84, y=460)

        # Sign-up button
        sign_up = Button(self.frame, text='Sign up', bd=0, bg='white', cursor='hand2', fg='slateblue1', font=('Open Sans', 12,))
        sign_up.place(x=272, y=460)



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

# Create the main window and run the app
if __name__ == "__main__":
    root = Tk()
    app = LoginPage(root)
    root.mainloop()
