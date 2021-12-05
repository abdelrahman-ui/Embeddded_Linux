from tkinter import *
import time

root_w = Tk()
root_w.title("Abdo_Frist_Gui")
root_w.resizable(False,False)
# the background colour
root_w.configure(background ="black")
root_w.geometry("700x500")

off=0

def clock():
    hour =time.strftime("%I")
    min =time.strftime("%M")
    sec =time.strftime("%S")
    day=time.strftime("%A")
    am_pm =time.strftime("%p")
    time_zone =time.strftime("%Z")
    my_label.config(text= hour + ":"+ min + ":" + sec +" " + am_pm)
    my_label.after(1000, clock)
    my_label2.config(text= "- "+time_zone +" Day is :"+ day)

def massage():
    global entery , my_label4
    my_label4.config(text="Alarm is counting .....")
    Alarm()

def Alram_off():
    off+=1

def Alarm():
    global entery, my_label4 ,Alarm ,off
    Alarm = entery.get()
    current_time=time.strftime("%H:%M")
    while Alarm != current_time :
        # update current time
        current_time = time.strftime("%H:%M")
    if Alarm == current_time :
        my_label4.config(text=" Alarm sound is playing.....")
        if off <= 1 :
            print("Toggle LED & Playing Sound")
            time.sleep(1)
            off=0


my_label=Label(root_w,text="",font=("Helvetica",48),fg="green",bg="black")
my_label.place(x=180,y=20)

my_label2=Label(root_w,text="",font=("Helvetica",14),fg="green",bg="black")
my_label2.place(x=180,y=100)

my_label3=Label(root_w,text="Enter the time for Alaram ( hh : mm ) : ",font=("Helvetica",11),fg="green",bg="black")
my_label3.place(x=100,y=200)

entery=Entry(root_w,width=20)
entery.place(x=400,y=200)

my_label4=Label(root_w,text=" - No Alarm Configration .. ",font=("Helvetica",13),fg="red",bg="black")
my_label4.place(x=220,y=250)


Btn=Button(root_w,text="Start counting ",command=massage ,font=("Helvetica",13))
Btn.place(x=260,y=300)

Btn2=Button(root_w,text="Stop Alarm ",command=Alram_off,font=("Helvetica",13))
Btn2.place(x=270,y=360)

clock()

root_w.mainloop()

