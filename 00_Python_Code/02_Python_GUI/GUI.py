# GUI :( Graphic User Interface ) The Window Appear To User To Interface With it
# widget in python :

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


# The Lib is --> Tkinter
import tkinter as GUI

# Button Action
def Btn_Action():
    print("Ok")
# Creat Empty Window
main_Window = GUI.Tk()

# to name the window
main_Window.title("Abdo_Frist_Gui")

# To put the size of window size and shift all by picsel
main_Window.geometry("400x400+600+200")

# Can't expent in window size in x or y
main_Window.resizable(False,False)

# the background colour
main_Window.configure(background ="green")

print(" i have not reached the end of the program ")
# Creat Button Must Before main window
# Every thing in window is a widget -->ObjectName = GUI.widgetfunction(WindowMame ,text="ok",command=Fun of click)
Btn_OK=GUI.Button(main_Window , text="OK",command=Btn_Action())
# To Displaying
# pack --> Display in defulat by python arrang widgets automatically and display it
# grid --> You are responsible for organizing your widgets like a table colum and rows
Btn_OK.pack()


# To Apear Window Ans still inside  the gui until action
main_Window.mainloop()
#that will excute after close the tk
print(" i have reached the end of the program ")






#================ for linux ================#
# sudo apt update
# sudo apt-get install python3-tk
# sudo apt install pip3
# pip3 install tkinter
# pip install tk