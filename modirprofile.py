from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox as ms
#making a window instance

conn = sqlite3.connect('data.db')

def all21():

    window = Tk()
    #creating a title for window
    #making a button inside the window 
    window.geometry('1000x700')
    window.configure(background='deep sky blue')
    window.title('پنل کاربری مدیر درمانگاه')
    window.resizable(width=False, height=False)
    top_frame = Label(window, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
    top_frame.pack(side='top')

    top_frame = Label(window, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
    top_frame.pack(side='top')
    top_frame = Label(window, text='پروفایل مدیر',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
    top_frame.pack(side='top')
#---------------------------------------
#مشاهده نام و آی دی و ساعت کاری پزشکان 
    showAllDoctorsPageBTNinfo= Button(window)


    def show_doctors_info():

        window2 = Tk()
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='مشاهده ساعت کاری پزشکان ' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='LightPink1',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')

        doctors=Label(window2)
        doctors.pack()
        doctors.place (x=0, y=200)

        
        window2.geometry('800x700')
        window2.configure(background='cyan2')
        window2.title('مشاهده نام و ساعت کاری پزشکان')
        window2.resizable(width=False, height=False)    
            
        with conn:
            cursorObj = conn.cursor() 
            all_doctors=cursorObj.execute('SELECT docid , doctname ,  btime , etime  FROM Doctor_t ')
            rows = cursorObj.fetchall()
            for i in rows: 
                doctors.configure(text=" {}".format(rows) , bg='white')
            window2.mainloop()
        
    showAllDoctorsPageBTNinfo.configure(text="مشاهده ساعت کاری پزشکان",font=("Brandon Grotesque",15 ),bg="white",fg="black",height= 2, width=18 , command=show_doctors_info)
    showAllDoctorsPageBTNinfo.pack()
    showAllDoctorsPageBTNinfo.place (x=290 , y= 180)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#این تابع برای مشاهده ی لیست ویزیت هایی می باشد که در درمانگاه انجام شده است 
    showAllVisitPageBTN= Button(window)
    def show_all_visit():
        window2 = Tk()
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='مشاهده گزارش ویزیت های درمانگاه' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='LightPink1',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')



        
        window2.geometry('800x700')
        window2.configure(background='cyan2')
        window2.title('گزارش مشاهده ویزیت های درمانگاه')
        window2.resizable(width=False, height=False)    
            
        visits=Label(window2)
        visits.pack()
        visits.place (x=0, y=200)
            
        with conn:
            cursorObj = conn.cursor() 
            all_visit=cursorObj.execute('SELECT visid , shiftnum ,visdate ,viscost ,visdesc ,docid ,patid  FROM Visit_t ')
            rows = cursorObj.fetchall()
            for i in rows:
                visits.configure(text=" {}".format(rows) , bg='white')
            window2.mainloop()
        
    showAllVisitPageBTN.configure(text="مشاهده ویزیت های درمانگاه",font=("Brandon Grotesque",15 ),bg="white",fg="black",height= 2, width=18 , command=show_all_visit)
    showAllVisitPageBTN.pack()
    showAllVisitPageBTN.place (x=510 , y= 180)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#این تابع برای این است که منشی بتواند اسامی تمام بیماران درمانگاه را مشاهده کند 
    showAllPatientPageBTN= Button(window)
    def show_all_patient():
        window2 = Tk()
        patient=Label(window2)
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        patient.pack()
        patient.place (x=0, y=200)
        top_frame = Label(window2, text='مشاهده گزارش بیماران درمانگاه' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='LightPink1',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')

        
        window2.geometry('800x700')
        window2.configure(background='cyan2')
        window2.title('گزارش مشاهده بیماران درمانگاه')
        window2.resizable(width=False, height=False)    
            
            
            
        with conn:
            cursorObj = conn.cursor() 
            all_patients=cursorObj.execute('SELECT patid , patname ,  patjob , pattel , patadr , patrecord ,patgender,insid FROM Filepat_t')
            rows = cursorObj.fetchall()
            for i in rows:
                patient.configure(text=" {}".format(rows) , bg='white')
            window2.mainloop()
        
    showAllPatientPageBTN.configure(text="مشاهده بیماران درمانگاه",font=("Brandon Grotesque",15 ),bg="white",fg="black",height= 2, width=18 , command=show_all_patient)
    showAllPatientPageBTN.pack()
    showAllPatientPageBTN.place (x=290 , y= 250)


    #------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------------------------------
#نمایش لیست بیمه هایی که درمانگاه با آنها قرارداد دارد
    showBimeBTN= Button(window)

    def show_all_bime():
        window2 = Tk()  
        window2.geometry('500x700')
        window2.configure(background='cyan2')
        window2.title('گزارش مشاهده بیمه های طرف قرارداد درمانگاه')
        window2.resizable(width=False, height=False)    
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='مشاهده گزارش بیمه های طرف قرارداد درمانگاه' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='LightPink1',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
   
        bime=Label(window2)
        bime.pack()
        bime.place (x=0, y=200) 
            
        with conn:
            cursorObj = conn.cursor() 
            all_Bime=cursorObj.execute('SELECT institle FROM Insurance_t')
            rows = cursorObj.fetchall()
            for i in rows:
                bime.configure(text=" {}".format(rows) , bg='white')
            window2.mainloop()
        
    showBimeBTN.configure(text="مشاهده بیمه های طرف قرارداد",font=("Brandon Grotesque",15 ),bg="white",fg="black", height= 2, width=18 , command=show_all_bime)
    showBimeBTN.pack()
    showBimeBTN.place (x=510 , y= 250)
#----------------------------------------------------------------------------------------
#مشاهده ی درآمد درمانگاه در تاریخی خاص

    showIncomeMain= Button(window)
    def show_Income():
        window3 = Tk()
        patient=Label(window3)
        patient.pack()
        patient.place (x=0, y=0)
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='درآمد درمانگاه در روزی مشخص' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')

        showfilepatinfo= Button(window3)
        text=Label(window3,text=" لطفا تاریخ مورد نظر را در فیلد وارد کنید" , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text.pack()
        text.place (x=70, y=200)
    
        window3.geometry('500x700')
        window3.configure(background='DarkSlateGray2')
        window3.title('گزارش مشاهده درآمد درمانگاه')
        window3.resizable(width=False, height=False)    
        showvisdate_entry= Entry(window3)
        showvisdate_entry.pack()
        showvisdate_entry.place(x=190 , y=240)
        

        def show_Income_main():
            showvisdate = showvisdate_entry.get()
            infoname=Label(window3)
            infoname.pack()
            infoname.place (x=5, y=400)

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT SUM(viscost) FROM Visit_t where visdate= ?"
                cursorObj.execute(query, (showvisdate,))

            rows = cursorObj.fetchall()
            conn.commit()

            infoname.configure(text=" {}".format(rows) , bg='white')

        showfilepatinfo= Button(window3)
        showfilepatinfo.configure(text=" نمایش درآمد",font=("Brandon Grotesque",10 ),fg="black", bg='orange' , command=show_Income_main)
        showfilepatinfo.pack()
        showfilepatinfo.place (x=200 , y=275)

    showIncomeMain.configure(text="درآمد درمانگاه تاریخ مشخص",font=("Brandon Grotesque",15 ),height= 2, width=18,bg='white' , command=show_Income)
    showIncomeMain.pack()
    showIncomeMain.place (x=290 , y= 320)


#----------------------------------------------------------------------------------------------------
#تعداد بیماران درمانگاه 
    showpateintCount= Button(window)


    def show_doctors_info():

        window2 = Tk()
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='تعداد بیماران درمانگاه' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='LightPink1',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')

        doctors=Label(window2)
        doctors.pack()
        doctors.place (x=0, y=200)

        
        window2.geometry('500x700')
        window2.configure(background='cyan2')
        window2.title('مشاهده گزارش تعداد بیماران درمانگاه')
        window2.resizable(width=False, height=False)    
            
        with conn:
            cursorObj = conn.cursor() 
            all_doctors=cursorObj.execute('SELECT COUNT(*) FROM Filepat_t ')
            rows = cursorObj.fetchall()
            for i in rows: 
                doctors.configure(text=" {}".format(rows) , bg='white')
            window2.mainloop()
        
    showpateintCount.configure(text="مشاهده تعداد بیماران درمانگاه",font=("Brandon Grotesque",15 ),bg="white",fg="black",height= 2, width=18 , command=show_doctors_info)
    showpateintCount.pack()
    showpateintCount.place (x=510 , y= 320)

#-----------------------------------------------------------------------------------------------------
#درآمد پزشک در بین دو تاریخ خاص

    showIncomeMain= Button(window)
    def show_Income_specific():
        window3 = Tk()
        patient=Label(window3)
        patient.pack()
        patient.place (x=0, y=0)
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='درآمد درمانگاه در بازه زمانی مشخص' ,font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')

        showfilepatinfo= Button(window3)
        text=Label(window3,text=" لطفا تاریخ مورد نظر را در فیلد وارد کنید" , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text.pack()
        text.place (x=70, y=200)
    
        window3.geometry('500x700')
        window3.configure(background='DarkSlateGray2')
        window3.title('گزارش مشاهده درآمد درمانگاه')
        window3.resizable(width=False, height=False)    
        showvisdate_entry1= Entry(window3)
        showvisdate_entry1.pack()
        showvisdate_entry1.place(x=190 , y=240)
        
        showvisdate_entry2= Entry(window3)
        showvisdate_entry2.pack()
        showvisdate_entry2.place(x=190 , y=270)

        def show_Income_specific_main():
            showvisdate1 = showvisdate_entry1.get()
            showvisdate2 = showvisdate_entry1.get()
            infoname=Label(window3)
            infoname.pack()
            infoname.place (x=5, y=400)

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT SUM(viscost) FROM Visit_t where visdate  BETWEEN ? AND ? "
                cursorObj.execute(query, (showvisdate1,showvisdate2))

            rows = cursorObj.fetchall()
            conn.commit()

            infoname.configure(text=" {}".format(rows) , bg='white')

        showfilepatinfo= Button(window3)
        showfilepatinfo.configure(text=" نمایش درآمد",font=("Brandon Grotesque",10 ),fg="black", bg='orange' , command=show_Income_specific_main)
        showfilepatinfo.pack()
        showfilepatinfo.place (x=200 , y=295)

    showIncomeMain.configure(text="درآمد درمانگاه بین 2 تاریخ",font=("Brandon Grotesque",15 ),height= 2, width=18,bg='white' , command=show_Income_specific)
    showIncomeMain.pack()
    showIncomeMain.place (x=290 , y= 390)
    
#-------------------------------------------------------------------
    def Quit1():
        response = ms.askokcancel('Exit!', 'Do you really want to exit ?')
        if response == 1:
            window.destroy()
        else:
            pass
    
    Quit= Button(window)
    Quit.configure(text="خروج",font=("Brandon Grotesque",12 ),width="10",fg='white', relief='groove', pady='5',bg='#133038', command= Quit1)
    Quit.pack()
    Quit.place (anchor='sw', rely=1.0, relx=0.0)


    window.mainloop()
