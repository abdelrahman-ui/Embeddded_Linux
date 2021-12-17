#import re (reguler expresion library)
import re 

##File Handling
#file_handler=open("..\Resources\PORT_config.txt","r")
##The New File , Create A New File If Not Exist 
#hand=open("..\Destination\PORT_config.txt","w")

#File Handling
file_handler=open("Resources\PORT_config.txt","r")
#The New File , Create A New File If Not Exist 
hand=open("Destination\PORT_config.txt","w")


mypattern=r"#define\s*PORTA_PIN\d_DIR\s*\d"


def  ModifyPortFunction(config_ls):
    #global Variables
    global  mypattern
    #Initialize Variables 
    Counter = 0 
    myFoundedList = []
    #Reading Each Line    
    for line in file_handler:
        #if found the Pattern in the line  
        mysearch = re.findall( mypattern , line )
        #if mysearch list is not empty  then append mysearch to myFoundedList
        if  mysearch != [] :
            #Append To myFoundedList 
            myFoundedList.append( mysearch )
            #change the index       
            myFoundedList[Counter]="#define PORTA_PIN"+str(Counter)+"_DIR\t\t\t\t"+str(config_ls[Counter]) +r"/*Modified By The Tool*/"+"\n"
            #Write The Modified Line (myFoundedList[Counter])
            hand.write(myFoundedList[Counter]) 
            #Increment The Counter
            Counter += 1
            
        else :
            #Write The Normal Line
            hand.write(line) 
            
        hand.flush()  
     

#Important Notice
#
#  for iterator in file_handler :
#      for 
#      line.split():
#      word=file_handler.readline()
#      ls_word.append(word)
#             
      
    

    
        



    



   

    
    

    

