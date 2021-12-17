
#import sys
#sys.path.append("D:\Embedded\Embedded Linux\2-Python\python_Tasks\Port_Configuration__Task\lab")

import tkinter as GUI 
#from lab import*
from lab import main_window
#import  lab



def init():
    global    main_window
    #Port_A_Frame 
    Port_A_Frame =GUI.Frame(  main_window , bg="red" ,width=250  ,height=600)
    Port_A_Frame.place( x=50 , y=150 )
    
    '''
    #Inailize Array to Carry Widget Variables 
    Radio_var=[]
    #Creating Array of Widget Variables 
    for ls_iterator in range(0,8,1) :
        Radio_var.append(  GUI.IntVar() )
    
    
    # Loop Creating Label (Pin_Num) + Input RadioButton + Output RadioButton
    for iterator in range( 0 , 8 ) : 
        #Label of Pin Number
        Pin_Num = "PIN " + str(iterator)
        pin_num_label = GUI.Label(Port_A_Frame , text=Pin_Num)
        pin_num_label.place( x=10  , y=100*(iterator*.5) )
        #Input Rdio Button
        in_radioBtn = GUI.Radiobutton(Port_A_Frame,text='INPUT'  , value=0 , variable= Radio_var[iterator] )
        in_radioBtn.place( x=50  , y=100*(iterator*.5) )
        #Input Rdio Button
        out_radioBtn = GUI.Radiobutton(Port_A_Frame,text='OUTPUT', value=1 , variable= Radio_var[iterator] )
        out_radioBtn.place( x=150 , y=100*(iterator*.5) )
    
    
    #submit button
    button = GUI.Button(Port_A_Frame , text="submit" , command=goToGet)
    button.place( x=180 , y=400 )

'''

def hello():
    print("Hello")
