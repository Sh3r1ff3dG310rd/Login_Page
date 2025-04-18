#CLAY NOTTINGHAM FIRST LOGIN PAGE

#Imported tkinter and installed pillow package
from tkinter import *
from PIL import ImageTk

#FUNCTIONALITY

#Hide eye icon
def hide():
    Eye.config(file = 'eye.png')
    enterPassword.config(show = '*')
    eyeButton.config(command = show)

#Show eye icon
def show():
    Eye.config(file = 'eye2.png')
    enterPassword.config(show = '')
    eyeButton.config(command = hide)

#Enter username
def username_enter(event):
    if enterUsername.get() == 'Username':
        enterUsername.delete(0, END)

#Enter password
def password_enter(event):
    if enterPassword.get() == 'Password':
        enterPassword.delete(0, END)

#GUI

#Created login window
login_page = Tk()
login_page.geometry('1055x660+50+50')
login_page.resizable(0, 0)
login_page.title('Login')
bgImage = ImageTk.PhotoImage(file = 'mountains.png')
bgLabel = Label(login_page, image = bgImage)
bgLabel.place(x = 0, y = 0)

#Login heading
loginHeading=Label(login_page,text = 'USER LOGIN', font = ('Consolas', 23, 'bold'), bg = 'white', fg = 'DodgerBlue4')
loginHeading.place(x = 580, y = 120)

#Enter username
enterUsername = Entry(login_page, width = 25, font = ('Consolas', 11, 'bold'), bd = 0, fg = 'DodgerBlue4')
enterUsername.place(x = 580, y = 200)
enterUsername.insert(0, 'Username')
enterUsername.bind('<FocusIn>',username_enter)
Frame(login_page, width = 300, height = 2, bg = 'DodgerBlue4').place(x = 580, y = 222)

#Enter password
enterPassword = Entry(login_page, width = 25, font = ('Consolas', 11, 'bold'), bd = 0, fg = 'DodgerBlue4')
enterPassword.place(x = 580, y = 260)
enterPassword.insert(0, 'Password')
enterPassword.bind('<FocusIn>', password_enter)
Frame(login_page, width = 300, height = 2, bg = 'DodgerBlue4').place(x = 580, y = 282)

#Hide password
Eye = PhotoImage(file = 'eye2.png')
eyeButton = Button(login_page, image = Eye, bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', command = hide)
eyeButton.place(x = 857, y = 255)

#Forgot password
forgotButton = Button(login_page, text = 'Forgot Password?', bd = 0, bg = 'white', activebackground = 'white', cursor = 'hand2', font = ('Consolas', 11, 'bold'), fg = 'DodgerBlue4')
forgotButton.place(x = 757, y = 295)

#Login Button
loginButton = Button(login_page, text = 'Login', font = ('Consolas', 16, 'bold'), fg = 'white', bg = 'DodgerBlue4', activeforeground = 'white', activebackground = 'DodgerBlue4', cursor = 'hand2', bd = 0, width = 19)
loginButton.place(x = 615, y = 350)

#Or
orLabel = Label(login_page, text = '------------- OR -------------', font = ('Consolas', 14), bg = 'white', fg = 'DodgerBlue4')
orLabel.place(x = 583, y = 400)

#Facebook logo
fb_logo = PhotoImage(file = 'fb.png')
fbButton = Button(login_page, image = fb_logo, bg = 'white', activeforeground = 'white', activebackground = 'white', cursor = 'hand2')
fbButton.place(x = 590, y = 440)

#Google logo
google_logo = PhotoImage(file = 'google.png')
gButton = Button(login_page, image = google_logo, bg = 'white', cursor = 'hand2')
gButton.place(x = 720, y = 440)

#Github logo
gh_logo = PhotoImage(file = 'GH.png')
ghButton = Button(login_page, image = gh_logo, bg = 'white', cursor = 'hand2')
ghButton.place(x = 855, y = 440)

#Sign up for new account
signupLabel=Label(login_page, text = 'No account? Sign up for one!', font = ('Consolas', 9, 'bold'), fg = 'DodgerBlue4', bg = 'white')
signupLabel.place(x = 590, y = 500)

#Create account
newAccountButton=Button(login_page, text = 'Create New Account', font=('Consolas', 9, 'bold underline'), fg = 'white', bg = 'DodgerBlue4', activeforeground = 'white', activebackground = 'medium orchid', cursor = 'hand2', bd = 0)
newAccountButton.place(x = 590, y = 525)

login_page.mainloop()
