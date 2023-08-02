# Importing Libraries
from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image
def Registerpatient():

    Reg = tk.Tk()
    Reg.title('افزودن بیمار جدید')
    Reg.geometry('800x800')

    Reg.configure(background='cyan3')
    

    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.45, anchor = CENTER)

    def database(arg=None):
      
        # Getting entries
        patid=patid_entry.get()
        patname=patname_entry.get()
        patjob=patjob_entry.get()
        pattel=pattel_entry.get()
        patadr=patadr_entry.get()
        patrecord=patrecord_entry.get()
        patgender=patgender_entry.get()
        insid=insid_entry.get()



        # Validating Entries
        validation = []

        # Adding information to the list
        validation.append(patid)
        validation.append(patname)
        validation.append(patjob)
        validation.append(pattel)
        validation.append(patadr)
        validation.append(patrecord)
        validation.append(patgender)
        validation.append(insid)

        # Boolean for condition
        condition = True
        
        # Looping and checking conditions

        if condition:
            
        

                # Making connection
                con = sqlite3.connect('data.db', check_same_thread=False, isolation_level=None)
                cur = con.cursor()

                # Inserting Data into Table
                cur.execute('INSERT INTO Filepat_t (patid ,patname,patjob ,pattel,patadr, patrecord ,patgender,insid) VALUES(?,?,?,?,?,?,?,?)',(patid,patname,patjob,pattel,patadr,patrecord,patgender,insid,))
                con.commit()

                # Showing success message
                ms.showinfo('Successful', 'ثبت نام با موفقیت انجام شد.')

                # Closing the window
                Reg.destroy()
            
        else:
            ms.showerror('Oops', 'Please Fill All The Input Fields')

    # creating a label for username and password using Label
    patid = tk.Label(frame, text = 'شناسه بیمار', font=('Arial',8, 'bold'), bg='white')
    patname = tk.Label(frame, text = 'نام بیمار ', font=('Arial',8, 'bold'), bg='white' )
    patjob = tk.Label(frame, text = 'شغل بیمار', font=('Arial',8, 'bold'), bg='white')
    pattel = tk.Label(frame, text = 'تلفن بیمار', font=('Arial',8, 'bold'), bg='white')
    patadr = tk.Label(frame, text = 'محل زندگی بیمار', font=('Arial',8, 'bold'), bg='white')
    patrecord = tk.Label(frame, text = 'سوابق بیمار', font=('Arial',8, 'bold'), bg='white')

    patgender = tk.Label(frame, text = 'جنسیت ', font=('Arial',8, 'bold'), bg='white')
    insid= tk.Label(frame, text = 'شناسه بیمه ', font=('Arial',8, 'bold'), bg='white')


    patid_entry = tk.Entry(frame ,font=('Arial',8,'normal'), bg='lavender')
    patid_entry.bind("<Return>", database)
    patname_entry = tk.Entry(frame ,font=('Arial',8,'normal'), bg='lavender')
    patname_entry.bind("<Return>", database)
    patjob_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='lavender')
    patjob_entry.bind("<Return>",database)
    pattel_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='lavender')
    pattel_entry.bind("<Return>",database)
    patadr_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='lavender')
    patadr_entry.bind("<Return>",database)
    patrecord_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='lavender')
    patrecord_entry.bind("<Return>",database)
    patgender_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='lavender')
    patgender_entry.bind("<Return>",database)
    insid_entry = tk.Entry(frame,font=('Arial',8,'normal'), bg='lavender')
    insid_entry.bind("<Return>",database)

    # Button that will call the submit function  
    submit=tk.Button(frame,text = 'افزودن بیمار', command = database, width="10",bd = '3',  font = ('Times', 8, 'bold'), bg='blue' , fg='white',relief='groove', justify = 'center', pady='5'  )

    # Placing the label and entry
    patid.pack()
    patid_entry.focus_set()
    patid_entry.pack()
    

    patname.pack()
    patname_entry.focus_set()
    patname_entry.pack()

    patjob.pack()
    patjob_entry.focus_set()
    patjob_entry.pack()


    pattel.pack()
    pattel_entry.focus_set()
    pattel_entry.pack()



    patadr.pack()
    patadr_entry.focus_set()
    patadr_entry.pack()



    patrecord.pack()
    patrecord_entry.focus_set()
    patrecord_entry.pack()




    patgender.pack()
    patgender_entry.focus_set()
    patgender_entry.pack()




    insid.pack()
    insid_entry.focus_set()
    insid_entry.pack()




    # Label for seperating Buttons
    label = Label(frame, bg='white').pack()
    
    submit.pack()

    # Quit Button

    Quit = tk.Button(Reg, text = "خروج", width="10", command = Reg.destroy, bd = '3',  font = ('Times', 12, 'bold'), bg='#133038', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=0.9,relx=0.0)
