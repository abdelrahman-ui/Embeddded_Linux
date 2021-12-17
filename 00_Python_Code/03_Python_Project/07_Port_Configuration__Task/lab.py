import tkinter as GUI 
import os
import fileModifier  as fileMod
#from PORT_A import init



#Inailize Array to Carry Widget Variables 
Radio_var=[]

def init():
    global     main_window , Radio_var
    #Port_A_Frame 
    Port_A_Frame =GUI.Frame( main_window , bg="gray" ,width=250  ,height=600)
    Port_A_Frame.place( x=50 , y=150 )
    
    
    #Creating Array of Widget Variables 
    for ls_iterator in range(0,8,1) :
        Radio_var.append(  GUI.IntVar() )
        
    
    # Loop Creating Label (Pin_Num) + Input RadioButton + Output RadioButton
    for iterator in range( 0 , 8 ) : 
        #Label of Pin Number
        Pin_Num = "PIN " + str(iterator)
        pin_num_label = GUI.Label(Port_A_Frame , text=Pin_Num)
        pin_num_label.place( x=10  , y=100*(iterator*.5) )
        #Input Radio Button
        in_radioBtn = GUI.Radiobutton(Port_A_Frame,text='INPUT'  , value=0 , variable= Radio_var[iterator] )
        in_radioBtn.place( x=50  , y=100*(iterator*.5) )
        #Input Rdio Button
        out_radioBtn = GUI.Radiobutton(Port_A_Frame,text='OUTPUT', value=1 , variable= Radio_var[iterator] )
        out_radioBtn.place( x=150 , y=100*(iterator*.5) )
    
    
    #submit button
    button = GUI.Button(Port_A_Frame , text="submit" , command=submitFunc)
    button.place( x=180 , y=400 )
    




def submitFunc():
    global Radio_var 
    results=[]
    #ss = str(var.get())
    #lab = GUI.Label(Port_A_Frame,text=ss)
    #lab.place( x=100 , y=150 )
    for i in range(0,8):
        results.append( Radio_var[i].get() )
    
    #Pass Radio_var Function 
    fileMod.ModifyPortFunction(results)



#create main_window 
main_window=GUI.Tk()
#disable resizability 
main_window.resizable(False , False)
#Set title 
main_window.title("AVR PORT Configuration ")
#Set Geometry of main_window
main_window.geometry("1050x950")

#File path entry
path_entry=GUI.Entry(main_window)
path_entry.place( x=50 , y=50 )

 

init()
#ModifyFile()
#PORT_A.init()
#PORT_A.hello()



#main window loop
main_window.mainloop()



#file.close()