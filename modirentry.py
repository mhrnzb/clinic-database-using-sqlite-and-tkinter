
# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3 
from modirprofile import all21
# Creating Input

def ADMIN():
    # Creating a new window
    Login = tk.Tk()
    Login.geometry('500x500')
    Login.title('Login to System !')

    # Background Colors
    Login.configure(background='gray26')

    # Locking the window size
    Login.resizable(width=False, height=False)

    # Top Frame
    top_frame = Label(Login, text='ورود مدیران',font = ('Cosmic', 20, 'bold'), bg='purple3',relief='groove',padx=500, pady=10)
    top_frame.pack(side='top')
    
    # Creating Frame
    frame = LabelFrame(Login, padx=40, pady=30, bg='purple3')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    
    # Creating function for connecting to database and checking username
    def Search(arg = None):
        if username_entry.get() == '': 
            ms.showerror('Oops', 'Enter Username !!')
            
        elif password_entry.get() == '':
            ms.showerror('Oops', 'Enter Password !!')
            
        else:
            global username
            username = username_entry.get()
            global password
            password = password_entry.get()

            # Making connection
            conn = sqlite3.connect('data.db')

            # Creating cursor
            with conn:
                cursor = conn.cursor()

            # Searching for users
            find_user = ('SELECT * FROM admins WHERE username = ? AND password = ?')
            cursor.execute(find_user,(username, password))
            results = cursor.fetchall()

            # if user then new window
            if results:
                all21()
                Login.destroy()

    username = tk.Label(frame, text = ': نام کاربری',font=('Arial',12, 'bold'),bg='purple3', fg='white')
    password = tk.Label(frame, text = ': رمز ورود', font = ('Arial',12,'bold'),bg='purple3', fg='white')

    # creating a entry for username 
    username_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='ivory3')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'), show = '*', justify = 'center', bg='ivory3') 
    password_entry.bind('<Return>', Search)
    
    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'ورود', command = Search, width="10",bd = '3',  font = ('Times', 12, 'bold'), bg='#581845', fg='white',relief='groove', justify = 'center', pady='5')

    # Placing the label and entry   
    username.pack()
    username_entry.focus_set()
    username_entry.pack()
    
    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Login, text = "خروج", width="10", command = Login.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='purple3', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.0)
