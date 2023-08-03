from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter import messagebox as ms
from registerpatient import Registerpatient

conn = sqlite3.connect('data.db')
def all():
    window = Tk()
    window.geometry('1000x700')
    window.configure(background='#7676EE')
    window.title('پنل کاربری منشی')
    window.resizable(width=False, height=False)
    top_frame = Label(window, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
    top_frame.pack(side='top')

    top_frame = Label(window, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
    top_frame.pack(side='top')
    top_frame = Label(window, text='پروفایل منشی',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='spring green',relief='groove',padx=500, pady=10)
    top_frame.pack(side='top')
#------------------------------------------------------------------------------------------------    
    #این تابع برای مشاهده ی لیست پزشکان درمانگاه
    showAllDoctorsPageBTN= Button(window)
    def show_all_doctors():

        window2 = Tk()


        
        window2.geometry('800x700')
        window2.configure(background='DarkSlateGray2')
        window2.title('مشاهده گزارش پزشکان درمانگاه')
        window2.resizable(width=False, height=False) 

        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='مشاهده پزشکان درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
            
            
                 
        doctors=Label(window2)
        doctors.pack()
        doctors.place (x=0, y=200)
   
        with conn:
            cursorObj = conn.cursor() 
            all_doctors=cursorObj.execute('SELECT docid , residencid , doctname ,  btime , etime  FROM Doctor_t ')
            rows = cursorObj.fetchall()
            for i in rows:
                doctors.configure(text=" {}".format(rows) , bg='white')
            window2.mainloop()
        
    showAllDoctorsPageBTN.configure(text="مشاهده پزشکان درمانگاه",font=("Brandon Grotesque",15 ),bg="white",fg="black" ,height= 2, width=18, command=show_all_doctors)
    showAllDoctorsPageBTN.pack()
    showAllDoctorsPageBTN.place (x=290 , y= 180)
# #-------------------------------------------------------------------------------------------------------------------------------------------------------------

# #این تابع برای مشاهده ی لیست ویزیت هایی می باشد که در درمانگاه انجام شده است 
    showAllVisitPageBTN= Button(window)
    def show_all_visit():
        window2 = Tk()
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='مشاهده ویزیت های انجام شده در درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        visits=Label(window2)
        visits.pack()
        visits.place (x=0, y=0)

        
        window2.geometry('800x700')
        window2.configure(background='DarkSlateGray2')
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

# #------------------------------------------------------------------------------------------------------------------------------------------------------------
# #این تابع برای این است که منشی بتواند اسامی تمام بیماران درمانگاه را مشاهده کند 
    showAllPatientPageBTN = Button(window)
    def show_all_patient():
        window2 = Tk()
        patient=Label(window2)
        patient.pack()
        patient.place (x=0, y=0)
        window2.geometry('800x700')
        top_frame = Label(window2, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window2, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window2, text='مشاهده بیماران درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        window2.configure(background='DarkSlateGray2')
        window2.title('گزارش مشاهده بیماران درمانگاه')
        window2.resizable(width=False, height=False) 
        patient=Label(window2)
        patient.pack()
        patient.place (x=0, y=200)    
           
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
# #-------------------------------------------------------------------------------------------------------------
# #مشاهده ی پرونده ی یک بیمار حاص 

    showfilepatinfoMain= Button(window)

    def show_file_pat():
        window3 = Tk()
        patient=Label(window3)
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='نمایش پرونده بیمار',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='SpringGreen2',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        patient.pack()
        patient.place (x=0, y=0)

        showfilepatinfo= Button(window3)
        text=Label(window3,text=" لطفا شناسه بیمار مورد نظر را در فیلد وارد کنید" , font=("Brandon Grotesque",16 ) , foreground="black" , background="SteelBlue2")
        text.pack()
        text.place (x=70, y=200)
    
        window3.geometry('500x700')
        window3.configure(background='SteelBlue2')
        window3.title('گزارش مشاهده بیماران درمانگاه')
        window3.resizable(width=False, height=False)    
        filepat_entry= Entry(window3)
        filepat_entry.pack()
        filepat_entry.place(x=190 , y=240)
    
        
        def show_file_pat_main():
            showpatid = filepat_entry.get()

            patientname=Label(window3)
            patientname.pack()
            patientname.place (x=330, y=330)

            patientjob=Label(window3)
            patientjob.pack()
            patientjob.place (x=330, y=370)

            patientid=Label(window3)
            patientid.pack()
            patientid.place (x=330, y=410)

            patienttel=Label(window3)
            patienttel.pack()
            patienttel.place (x=330, y=450)

            patientadr=Label(window3)
            patientadr.pack()
            patientadr.place (x=330, y=490)

            
            patientrecord=Label(window3)
            patientrecord.pack()
            patientrecord.place (x=330, y=530)


                        
            patientgender=Label(window3)
            patientgender.pack()
            patientgender.place (x=330, y=570)

            patientinsid=Label(window3)
            patientinsid.pack()
            patientinsid.place (x=330, y=610)





            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT patname FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientname.configure(text=" {}".format(rows) , bg='white')

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT patjob FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientjob.configure(text=" {}".format(rows) , bg='white')

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT patid FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientid.configure(text=" {}".format(rows) , bg='white')


            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT pattel FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patienttel.configure(text=" {}".format(rows) , bg='white')


            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT patadr FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientadr.configure(text=" {}".format(rows) , bg='white')

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT patrecord FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientrecord.configure(text=" {}".format(rows) , bg='white')

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT patgender FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientgender.configure(text=" {}".format(rows) , bg='white')

            with conn:
                
                cursorObj = conn.cursor()
                query = "SELECT insid FROM Filepat_t where patid= ?"
                cursorObj.execute(query, (showpatid,))
            rows = cursorObj.fetchall()
            conn.commit()
            patientinsid.configure(text=" {}".format(rows) , bg='white')


            text=Label(window3,text="نام کامل بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text.pack()
            text.place (x=430, y=330)


            text1=Label(window3,text="شغل بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text1.pack()
            text1.place (x=430, y=370)
        
            text2=Label(window3,text="شناسه بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text2.pack()
            text2.place (x=430, y=410)


            text3=Label(window3,text="تلفن بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text3.pack()
            text3.place (x=430, y=450)
        

            text4=Label(window3,text="آدرس بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text4.pack()
            text4.place (x=430, y=490)
        

            text4=Label(window3,text="سوابق بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text4.pack()
            text4.place (x=430, y=530)


        
        
            text5=Label(window3,text="جنسیت بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text5.pack()
            text5.place (x=430, y=570)


            text5=Label(window3,text="شناسه بیمه بیمار" , font=("Brandon Grotesque",10 ) , foreground="black" , background="SteelBlue2")
            text5.pack()
            text5.place (x=430, y=610)





        showfilepatinfo= Button(window3)
        showfilepatinfo.configure(text=" نمایش اطلاعات بیمار ",font=("Brandon Grotesque",10 ),fg="black",bg='cyan' , command=show_file_pat_main)
        showfilepatinfo.pack()
        showfilepatinfo.place (x=200 , y=275)
        window3.mainloop()
    
    showfilepatinfoMain.configure(text=" نمایش پرونده بیمار مورد نظر ",font=("Brandon Grotesque",15 ),bg='white',height= 2, width=18  , command=show_file_pat)
    showfilepatinfoMain.pack()
    showfilepatinfoMain.place (x=510 , y= 250)












# #-------------------------------------------------------------------------------------------------
# #مشاهده شماره پرونده ی بیمار و هزینه ی ویزیت خ 
    showvisitinfoMain= Button(window)

    def show_file_pat_visit_and_date():
        window3 = Tk()
        window3.geometry('500x700')
        window3.configure(background='DarkSlateGray2')
        window3.title('گزارش مشاهده هزینه ویزیت بیمار')
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='مشاهده هزینه ویزیت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        window3.resizable(width=False, height=False)    
            
        patient=Label(window3)
        patient.pack()
        patient.place (x=0, y=0)

        text=Label(window3,text=" لطفا شناسه بیمار مورد نظر را در فیلد وارد کنید" , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text.pack()
        text.place (x=70, y=200)

        filepat_entry= Entry(window3,bg='white')
        filepat_entry.pack()
        filepat_entry.place(x=190 , y=240)
        showvisitinfo= Button(window3)
    
        def show_file_pat_visit_and_date_main():
            showvisdate = filepat_entry.get()

            infoname=Label(window3)
            infoname.pack()
            infoname.place (x=10, y=350)
            with conn:
                cursorObj = conn.cursor()
                query = "SELECT patid , viscost   FROM Visit_t WHERE visid = ?"
                cursorObj.execute(query, (showvisdate,))

            rows = cursorObj.fetchall()
            conn.commit()
            infoname.configure(text=" {}".format(rows) , bg='white')

        showvisitinfo= Button(window3)
        showvisitinfo.configure(text=" نمایش ",font=("Brandon Grotesque",10 ),fg="black", bg='light coral' , command=show_file_pat_visit_and_date_main)
        showvisitinfo.pack()
        showvisitinfo.place (x=230 , y=275)

        window3.mainloop()
    
    showvisitinfoMain.configure(text="هزینه ویزیت بیمار مورد نظر",font=("Brandon Grotesque",15 ),bg='white',height= 2, width=18 , command=show_file_pat_visit_and_date)
    showvisitinfoMain.pack()
    showvisitinfoMain.place (x=290 , y= 320)


# #----------------------------------------------------------------------------------------------------------
# # این دکمه برای این هست که منشی بتونه اطلاعات یه بیمار رو در دیتابیس وارد کنه 
# #وقتی که منشی روی دکمه ی مورد نظر کلیک کنه ، وارد صفحه ی ثبت بیمار جدید می شود 
    registerNewPatient= Button(window)
    registerNewPatient.configure(text="افزودن بیمار جدید ",font=("Brandon Grotesque",15 ),bg='white',height= 2, width=18 , command=Registerpatient)
    registerNewPatient.pack()
    registerNewPatient.place (x=510 , y= 320)

#-------------------------------------------------------------------------------------------------------
#حذف پرونده ی بیمار
    showvisitinfoMain= Button(window)

    def show_file_pat_visit_and_date():
        window3 = Tk()
        window3.geometry('500x700')
        window3.configure(background='DarkSlateGray2')
        window3.title('گزارش مشاهده هزینه ویزیت بیمار')
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='حذف پرونده ی بیمار',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        window3.resizable(width=False, height=False)    
            
        patient=Label(window3)
        patient.pack()
        patient.place (x=0, y=0)

        text=Label(window3,text=" لطفا جهت حذف ، شناسه بیمار مورد نظر را در فیلد وارد کنید" , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text.pack()
        text.place (x=70, y=200)

        filepat_entry= Entry(window3,bg='white')
        filepat_entry.pack()
        filepat_entry.place(x=190 , y=240)
        showvisitinfo= Button(window3)
    
        def show_file_pat_visit_and_date_main():
            showvisdate = filepat_entry.get()

            infoname=Label(window3)
            infoname.pack()
            infoname.place (x=10, y=350)
            with conn:
                cursorObj = conn.cursor()
                query = "DELETE FROM Filepat_t  WHERE patid= ?"
                cursorObj.execute(query, (showvisdate,))

            rows = cursorObj.fetchall()
            conn.commit()


        showvisitinfo= Button(window3)
        showvisitinfo.configure(text="حذف بیمار ",font=("Brandon Grotesque",10 ),fg="black", bg='light coral' , command=show_file_pat_visit_and_date_main)
        showvisitinfo.pack()
        showvisitinfo.place (x=230 , y=275)

        window3.mainloop()
    
    showvisitinfoMain.configure(text=" حذف پرونده بیمار",font=("Brandon Grotesque",15 ),bg='white',height= 2, width=18 , command=show_file_pat_visit_and_date)
    showvisitinfoMain.pack()
    showvisitinfoMain.place (x=290 , y= 390)



#---------------------------------------------------------------------------------------------------------
#افزودن تایم ویزیت 
    addvisitinfoMain= Button(window)

    def show_file_pat_visit_and_date():
        window3 = Tk()
        window3.geometry('500x700')
        window3.configure(background='DarkSlateGray2')
        window3.title('گزارش مشاهده هزینه ویزیت بیمار')
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='افزودن زمان نوبت',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        window3.resizable(width=False, height=False)    
            
        patient=Label(window3)
        patient.pack()
        patient.place (x=0, y=0)

        text1=Label(window3,text="لطفا شناسه ای برای ویزیت وارد کنید " , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text1.pack()
        text1.place (x=100, y=200)

        text2=Label(window3,text="لطفا شماره ی نوبت را برای ویزیت وارد کنید " , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text2.pack()
        text2.place (x=70, y=260)

        text2=Label(window3,text="لطفا تاریخی را برای ویزیت وارد کنید " , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text2.pack()
        text2.place (x=100, y=310)


        filepat_entry1= Entry(window3,bg='white')
        filepat_entry1.pack()
        filepat_entry1.place(x=190 , y=240)

        filepat_entry2= Entry(window3,bg='white')
        filepat_entry2.pack()
        filepat_entry2.place(x=190 , y=290)

        filepat_entry3= Entry(window3,bg='white')
        filepat_entry3.pack()
        filepat_entry3.place(x=190 , y=350)

        showvisitinfo= Button(window3)
    
        def show_file_pat_visit_and_date_main():
            showvisdate1 = filepat_entry1.get()
            showvisdate2 = filepat_entry2.get()
            showvisdate3 = filepat_entry2.get()

            infoname=Label(window3)
            infoname.pack()
            infoname.place (x=10, y=350)
            with conn:
                cursorObj = conn.cursor()
                query = "INSERT INTO Visit_t (visid , shiftnum ,visdate) VALUES (?,?,?) "
                cursorObj.execute(query, (showvisdate1 ,showvisdate2 ,showvisdate3 ))

            rows = cursorObj.fetchall()
            conn.commit()
            infoname.configure(text=" {}".format(rows) , bg='white')

        showvisitinfo= Button(window3)
        showvisitinfo.configure(text="افزودن",font=("Brandon Grotesque",10 ),fg="black", bg='light coral' , command=show_file_pat_visit_and_date_main)
        showvisitinfo.pack()
        showvisitinfo.place (x=230 , y=380)

        window3.mainloop()
    
    addvisitinfoMain.configure(text="افزودن زمان نوبت",font=("Brandon Grotesque",15 ),bg='white',height= 2, width=18 , command=show_file_pat_visit_and_date)
    addvisitinfoMain.pack()
    addvisitinfoMain.place (x=510 , y= 390)
#-----------------------------------------------------------------------------------------------------------
#حذف نوبت
    showdeleteMain= Button(window)

    def delete_shift():
        window3 = Tk()
        window3.geometry('500x700')
        window3.configure(background='DarkSlateGray2')
        window3.title('گزارش مشاهده هزینه ویزیت بیمار')
        top_frame = Label(window3, text='مدیریت خدمات درمانی و پزشکی',font = ('B Koodak', 16, 'bold'),bd='5',fg='black' ,bg='#7F7FFF',relief='groove',padx=900, pady=10)
        top_frame.pack(side='top')

        top_frame = Label(window3, text='سامانه مدیریت درمانگاه',font = ('Cosmic', 13, 'bold'),bd='5',fg='white' ,bg='gray26',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        top_frame = Label(window3, text='حذف نوبت بیمار',font = ('Cosmic', 13, 'bold'),bd='5',fg='black' ,bg='cyan3',relief='groove',padx=500, pady=10)
        top_frame.pack(side='top')
        window3.resizable(width=False, height=False)    
            
        patient=Label(window3)
        patient.pack()
        patient.place (x=0, y=0)

        text=Label(window3,text=" لطفا جهت حذف ، شناسه ویزیت  را در فیلد وارد کنید" , font=("Brandon Grotesque",16 ) , foreground="black" , background="DarkSlateGray2")
        text.pack()
        text.place (x=70, y=200)

        filepat_entry= Entry(window3,bg='white')
        filepat_entry.pack()
        filepat_entry.place(x=190 , y=240)
        showvisitinfo= Button(window3)
    
        def delete_shift_main():
            showvisdate = filepat_entry.get()
            with conn:
                cursorObj = conn.cursor()
                query = "DELETE FROM Visit_t  WHERE visid= ?"
                cursorObj.execute(query, (showvisdate,))

            rows = cursorObj.fetchall()
            conn.commit()


        showvisitinfo= Button(window3)
        showvisitinfo.configure(text="حذف نوبت ",font=("Brandon Grotesque",10 ),fg="black", bg='light coral' , command=delete_shift_main)
        showvisitinfo.pack()
        showvisitinfo.place (x=230 , y=275)

        window3.mainloop()
    
    showdeleteMain.configure(text=" حذف نوبت بیمار",font=("Brandon Grotesque",15 ),bg='white',height= 2, width=18 , command=delete_shift)
    showdeleteMain.pack()
    showdeleteMain.place (x=290 , y= 460)

#-------------------------------------------------------------------------------------------------

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
