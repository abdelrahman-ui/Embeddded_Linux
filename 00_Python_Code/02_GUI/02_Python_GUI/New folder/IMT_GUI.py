# GUI :( Graphic User Interface ) The Window Appear To User To Interface With it

# Every Thing is widget
# widget in python :objectname = widgetfunction(windowtoshow,option)

# 1---> Buttton        : Can Clic on it
# 2---> Entry          : To Take Input From User
# 3---> Lable          : As a topic not doing any action
# 4---> Radio Buttons  : Many option but can take only one option
# 5---> Check Buttons  : Many option Can select too many of option or all
# 6---> Label Frame    : As Container have too many label
# 7---> TopLevel       : Like exit without save give you window too tell you would you like to save change
# 8---> Text Area      : Empty to put in it text and edit on it
# 10---> Spin Box      : Box give you some option can select an option
# 11---> Scale         : Like Zoom slider
# 12---> Menu          : Like File View run
# 13---> Frame         : Fram With Out Label
# 14---> Massage       : Like Label But I can Make Multi line
# 15---> Canvas        : Draw or display image
# 16---> OptionMenu    : Drop Dowen Meanu like spin


# The Lib is --> GUI From Tkinter
import tkinter as GUI

# Button Action
def Btn_Action():
    print("Btn_Prassed")


# Creat Empty Window tk return main window the empty window
main_Window = GUI.Tk()

# to name the window
main_Window.title("Abdo_Frist_Gui")

# To put the size of window (size and shift) all by picsel
main_Window.geometry("400x400+600+200")

# Can't expent in window size in x or y
main_Window.resizable(False,False)

# the background colour
main_Window.configure(background ="green")

print(" i have not reached the end of the program ")
# Creat Button Must Before main window only creat without display
# Every thing in window is a widget -->ObjectName = GUI.widgetfunction(WindowMame ,text="ok",command=Fun of click)
Btn_OK=GUI.Button(main_Window,text="OK",command=Btn_Action(),width=10 , height=5)
# To Displaying ( pack or grid) not both
# pack --> Display in defulat by python arrang widgets automatically and display it
# grid --> You are responsible for organizing your widgets like a table colum and rows
# Place --> Using picxel x= and y=
#Btn_OK.pack()
# If you change 0 and 0 will not change position --> any block empaty defualt size is zero
#Btn_OK.grid(row = 50 , column = 20)
#to change defulat size For colume and row  so you must configure both
#main_Window.grid_columnconfigure(0,minsize=20)
#main_Window.grid_rowconfigure(0,minsize=20)

# With Loop
#for Btn in range(0,3):
   # Creat Btn
   # Mybtn = GUI.Button(main_Window,text="OK")
   # Display Button
   # Mybtn.pack()


def Radio_Action():
    global Selected_Radio_Btn
    #Make a variable to not call function meny time 
    select_var=Selected_Radio_Btn.get()
    if select_var == 1 :
        print("Frist")
    elif select_var == 2 :
        print("Second")
    else:
        print("No one Pressed ")
# Place by pixel Creart
#sheft_x=0
#sheft_y=0
#for btn in range(0,4):
 #   Btn_OK = GUI.Button(main_Window, text="OK", command=Btn_Action(), width=2, height=1)
 #  Btn_OK.place(x=sheft_x,y=sheft_y)
 #   sheft_x+=20
 #  sheft_y+=10
# To Appear
'''
Btn2_button=GUI.Button(main_Window,text="Button")
# Sppear Button on Row =  Column =
Btn2_button.grid(row=0,column=1)
main_Window.grid_columnconfigure(0,minsize=50)
main_Window.grid_columnconfigure(0,minsize=50)

Btn2_button=GUI.Button(main_Window,text="Button")
Btn2_button.grid(row=1,column=2)
main_Window.grid_columnconfigure(0,minsize=50)
main_Window.grid_columnconfigure(0,minsize=50)

Btn2_button=GUI.Button(main_Window,text="Button")
Btn2_button.grid(row=1,column=0)
main_Window.grid_columnconfigure(0,minsize=50)
main_Window.grid_columnconfigure(0,minsize=50)

Btn2_button=GUI.Button(main_Window,text="Button")
Btn2_button.grid(row=2,column=1)
main_Window.grid_columnconfigure(0,minsize=50)
main_Window.grid_columnconfigure(0,minsize=50)

#Creat Entry
Entry=GUI.Entry(main_Window,width=20)
#Display Entery
Entry.place(x=20,y=20)
#To return the string from entry
user_enter=Entry.get()

#Creat Label
Label=GUI.Label(main_Window,text="Enter Your Name",bg="red")
#Display
Label.place(x=30,y=10)

'''
#Global Var you must give him it's type IntVar() or StringVar()
Selected_Radio_Btn=GUI.IntVar()
# If the frist radio btn pressed the varible will = 1
# If the Second radio btn pressed the varible will = 2
# If noone pressed the value will be the defult one  0
Radio_Btn_1=GUI.Radiobutton(main_Window,text="Btn_1",value=1,variable=Selected_Radio_Btn,command=Radio_Action)
Radio_Btn_2=GUI.Radiobutton(main_Window,text="Btn_2",value=2,variable=Selected_Radio_Btn,command=Radio_Action)
Radio_Btn_1.place(x=30,y=10)
Radio_Btn_2.place(x=100,y=10)

# To Apear Window Ans still inside  the GUI until action Of close
main_Window.mainloop()
#that will excute after close the tk
print(" i have reached the end of the program ")




#================ for linux ================#
# sudo apt update
# sudo apt-get install python3-tk
# sudo apt install pip3
# pip3 install tkinter
# pip install tk