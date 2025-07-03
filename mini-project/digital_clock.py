#Digital Clock 

from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    m = time.strftime("%p")
    
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    
    box_hour.config(text=hour)
    box_min.config(text=minute)
    box_sec.config(text=second)
    box_m.config(text=m)

    box_date.config(text=date)
    box_month.config(text=month)
    box_year.config(text=year)
    box_day.config(text=day)
    
    box_hour.after(200,date_time)

clock = Tk()
clock.title('****Digital Clock****')
clock.geometry('1000x500')
clock.config(bg='grey')

box_label_time = Label(clock,text = "Time",font = ('Times New Roman',26),bg='silver',fg="black")
box_label_time.place(x=10,y=0,height=30,width=120)
#******* Time *******
box_hour =  Label(clock,text = "00",font = ('Times New Roman',50,"bold"),bg='white' , fg="black")
box_hour.place(x=120,y=45,height=110,width=100)
lab_hour =  Label(clock,text = "Hour",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_hour.place(x=120,y=180,height=35,width=100)

box_min =  Label(clock,text = "00",font = ('Times New Roman',50,"bold"),bg='white' , fg="black")
box_min.place(x=340,y=45,height=110,width=100)
lab_min =  Label(clock,text = "Minute",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_min.place(x=340,y=180,height=35,width=100)

box_sec =  Label(clock,text = "00",font = ('Times New Roman',50,"bold"),bg='white' , fg="black")
box_sec.place(x=560,y=45,height=110,width=100)
lab_sec =  Label(clock,text = "Second",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_sec.place(x=560,y=180,height=35,width=100)

box_m =  Label(clock,text = "00",font = ('Times New Roman',44,"bold"),bg='white' , fg="black")
box_m.place(x=780,y=45,height=110,width=100)
lab_m =  Label(clock,text = "AM/PM",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_m.place(x=780,y=180,height=35,width=100)

box_label_date = Label(clock,text = "Date",font = ('Times New Roman',26),bg='silver',fg="black")
box_label_date.place(x=10,y=235,height=30,width=120)
#******* Date *******
box_date =  Label(clock,text = "00",font = ('Times New Roman',50,"bold"),bg='white' , fg="black")
box_date.place(x=120,y=280,height=110,width=100)
lab_date =  Label(clock,text = "Date",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_date.place(x=120,y=415,height=35,width=100)

box_month =  Label(clock,text = "00",font = ('Times New Roman',50,"bold"),bg='white' , fg="black")
box_month.place(x=340,y=280,height=110,width=100)
lab_month =  Label(clock,text = "Month",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_month.place(x=340,y=415,height=35,width=100)

box_year =  Label(clock,text = "00",font = ('Times New Roman',50,"bold"),bg='white' , fg="black")
box_year.place(x=560,y=280,height=110,width=100)
lab_year =  Label(clock,text = "Year",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_year.place(x=560,y=415,height=35,width=100)

box_day =  Label(clock,text = "00",font = ('Times New Roman',38,"bold"),bg='white' , fg="black")
box_day.place(x=780,y=280,height=110,width=100)
lab_day =  Label(clock,text = "Day",font = ('Times New Roman',20,"bold"),bg='white' , fg="black")
lab_day.place(x=780,y=415,height=35,width=100)

date_time()

clock.mainloop()
