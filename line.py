import tkinter as tk
from tkinter import *
import sqlite3
from sqlite3 import Error
from tkinter import messagebox as ms
from modirentry import ADMIN
from doctorenter import doctor
from monshientry import monshi

system = tk.Tk()
system.geometry('900x500')
system.configure(background='lightblue')
system.title('خدمات درمانی و پزشکی ')
top_frame = Label(system, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
top_frame.pack(side='top')

#-------------------------دیتابیس---------------------------------------------------
try:
    conn = sqlite3.connect('data.db')
    conn.execute('PRAGMA foreign_keys = ON;')

#ادمین ها
    conn.execute('''CREATE TABLE IF NOT EXISTS admins(username TEXT PRIMARY KEY,
    password TEXT)''')
#بیمه
    conn.execute('''CREATE TABLE IF NOT EXISTS Insurance_t(insid PRIMARY KEY ,
      institle TEXT ,
      insphone)''')
#تخصص پزشک
    conn.execute('''CREATE TABLE IF NOT EXISTS Residency_t(
                 residencid PRIMARY KEY , rdesc TEXT,
                 resname TEXT)''')

#پزشک
    conn.execute('''CREATE TABLE IF NOT EXISTS Doctor_t (
                 docid PRIMARY KEY,
                docusername  ,
                docpassword ,

                 residencid INTEGER ,
                 doctname  TEXT,
                 btime ,
                 etime,
                 FOREIGN KEY (residencid) REFERENCES Residency_t(residencid)
                 )
                 ''')
#قرارداد بیمه و پزشک
    conn.execute('''CREATE TABLE IF NOT EXISTS Bond_t(
                bondid PRIMARY KEY ,
                docid INTEGER ,
                insid INTEGER ,  
                bdate , 
                edate ,
                FOREIGN KEY (insid) REFERENCES Insurance_t(insid),
                FOREIGN KEY (docid) REFERENCES Doctor_t(docid))''')
 #پرونده بیمار
    conn.execute('''CREATE TABLE IF NOT EXISTS Filepat_t(
    patid PRIMARY KEY ,
    patname , 
    patjob ,
    pattel , 
    patadr ,
    patrecord ,
    patgender,
    insid INTEGER ,
    FOREIGN KEY (insid) REFERENCES Insurance_t(insid)
      )''')
#ویزیت
    conn.execute('''CREATE TABLE IF NOT EXISTS Visit_t(
    visid PRIMARY KEY ,
    shiftnum ,
    visdate ,
    viscost ,
    visdesc ,
    docid INTEGER ,
    patid INTEGER,
    FOREIGN KEY (docid) REFERENCES Doctor_t(docid),
    FOREIGN KEY (patid) REFERENCES Filepat_t(patid)
        )''')



#دارو
    conn.execute('''CREATE TABLE IF NOT EXISTS Drug_t(
    drugid PRIMARY KEY ,
    drugname TEXT ,
    drugdesc ,
    drugcom)''')


 #نسخه ی دارو ها
    conn.execute('''CREATE TABLE IF NOT EXISTS Noskhe_t(
    pr1num PRIMARY KEY , 
    drugdesc ,
    price ,
    visid INTEGER ,
    drugid INTEGER,
    patid INTEGER,
    FOREIGN KEY (visid) REFERENCES Visit_t(visid),
    FOREIGN KEY (drugid) REFERENCES Drug_t(drugid),
    FOREIGN KEY (patid) REFERENCES Filepat_t(patid)
        )''')
    
#آزمایش
    conn.execute('''CREATE TABLE IF NOT EXISTS Experience_t(
    expid PRIMARY KEY ,
    expname TEXT ,
    expper)''')
    
#نسخه آزمایش ها
    conn.execute('''CREATE TABLE IF NOT EXISTS Noskhe2_t(
    pr2num PRIMARY KEY ,
    expper , 
    visid INTEGER ,
    expid INTEGER ,
    FOREIGN KEY (visid) REFERENCES Visit_t(visid),
    FOREIGN KEY (expid) REFERENCES Experience_t(expid)
        )''')
    
#منشی 
    conn.execute('''CREATE TABLE IF NOT EXISTS Clerk_t(
    clkid PRIMARY KEY ,
    clkpass , 
    clkuser ,
    crknum ,
    crkname TEXT
        )''')   


    
except Error:
    print(Error)


conn.execute("INSERT OR IGNORE INTO admins(username,password) VALUES('owner','1234a')")

# Top Frame
top_frame = Label(system, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
top_frame.pack(side='top')


# Creating Frame
frame = LabelFrame(system,text='ورود و ثبت نام', padx=30, pady=40, bg='white', bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# Creating login button and positioning it


# Label for seperating Buttons
label = Label(frame, bg='white').pack()
login1 = tk.Button(frame, text = "ورود مدیران", width="12", bd = '2',command=ADMIN, font = ('Times', 12, 'bold'), bg='purple3',relief='groove', justify = 'center', pady='2')
login1.pack()

login2 = tk.Button(frame, text ="ورود پزشک", width="12", bd = '2',command=doctor, font = ('Times', 12, 'bold'), bg='cyan3',relief='groove', justify = 'center', pady='2')
login2.pack()


login3 = tk.Button(frame, text = "ورود منشی", width="12", bd = '2',command=monshi,font = ('Times', 12, 'bold'), bg='cyan4',relief='groove', justify = 'center', pady='2')
login3.pack()


# Label for seperating Buttons
label2 = Label(frame, bg='white').pack()
def Quit():
    response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
    if response == 1:
        system.destroy()
    else:
        pass

Quit = tk.Button(system, text="خروج", width="10", command=Quit, bd='3', font=('Times', 12, 'bold'), bg='#133038',
                 fg='white', relief='groove', pady='5')
Quit.place(anchor='sw', rely=1.0, relx=0.0)
system.mainloop()
