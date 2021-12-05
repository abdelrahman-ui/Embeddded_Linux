'''

Write a python code that generate the
mentioned GUI used for configuring AVR
ARM GPIO and generate a c file for the
code

'''




def Mode_Action():
    global Mode_Action
    # Make a variable to not call function meny time
    Select_var = Selected_Radio_Btn.get()
    if Select_var == 0 :
        Input_Config()
    elif Select_var == 1:
        Output_Config()
    else:
        print("Check The Mode")



# The Lib is --> GUI From Tkinter
import tkinter as GUI

# Creat Empty Window
main_Window = GUI.Tk()

# to name the window
main_Window.title("ARM_PINS_Config")

# To put the size of window (size and shift) all by picsel
main_Window.geometry("500x500+600+200")

# Can't expent in window size in x or y
main_Window.resizable(False,False)

#Global Var you must give him it's type IntVar() or StringVar()
Mode_Action=GUI.IntVar()
Config=GUI.IntVar()


# Putton For Config Pin as input or outpuy
Radio_Btn_1=GUI.Radiobutton(main_Window,text="Input",value=0,variable=Mode_Action,command=Mode_Action)
Radio_Btn_2=GUI.Radiobutton(main_Window,text="Output",value=1,variable=Mode_Action,command=Mode_Action)

Analog_Radio_Btn=GUI.Radiobutton(main_Window,text="Analog",value=0,variable=Config,command=Mode_Action)
Floating_Radio_Btn=GUI.Radiobutton(main_Window,text="Floating",value=1,variable=Config,command=Mode_Action)
PULL_DOWN_Radio_Btn=GUI.Radiobutton(main_Window,text="PULL_DOWN",value=2,variable=Config,command=Mode_Action)
PULL_UP_Radio_Btn=GUI.Radiobutton(main_Window,text="PULL_UP",value=3,variable=Config,command=Mode_Action)


Pushpull_Radio_Btn=GUI.Radiobutton(main_Window,text="Pushpull ",value=0,variable=Config,command=Mode_Action)
OpenDrain_Radio_Btn=GUI.Radiobutton(main_Window,text="OpenDrain",value=1,variable=Config,command=Mode_Action)
ALF_PushPull_Radio_Btn=GUI.Radiobutton(main_Window,text="ALF PushPull",value=2,variable=Config,command=Mode_Action)
ALF_OpenDrain_Radio_Btn=GUI.Radiobutton(main_Window,text="ALF OpenDrain",value=3,variable=Config,command=Mode_Action)

#Display Radio_Btn
Radio_Btn_1.place(x=30,y=10)
Analog_Radio_Btn.place(x=30,y=30)
Floating_Radio_Btn.place(x=30,y=50)
PULL_DOWN_Radio_Btn.place(x=30,y=70)
PULL_UP_Radio_Btn.place(x=30,y=90)


Radio_Btn_2.place(x=200,y=10)
Pushpull_Radio_Btn.place(x=200,y=30)
OpenDrain_Radio_Btn.place(x=200,y=50)
ALF_PushPull_Radio_Btn.place(x=200,y=70)
ALF_OpenDrain_Radio_Btn.place(x=200,y=90)

# To Apear Window Ans still inside  the GUI until action Of close
main_Window.mainloop()