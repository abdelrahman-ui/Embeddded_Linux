# To Save Data On Hard_Disk Not Ram --> So PUT In File
# Liberay We Be Use is Built in --> We don't need to import it

# To open file --> open("File_path","Mode")
#   Mode -->
# "r" --> Read Only & "w" ---> Write Only  & "a" --> Append Only
# "r+": Read & write Mode
# "w+": Write Read Mode same r+
# "a+": Append Read Mode

# Creat File Handeler To deal WithThe File --> Like Pointer
# if you open file not exist return error same read but write will creat file
File_Handlr = open("Try.txt","r")
# To Know The File Can Be Read Or Not   Will Return True Or False
print(File_Handlr.readable())
#  To read by bit
print("Frist read --->",File_Handlr.read(3))
# Start From The Last Position
print("Second read --->",File_Handlr.read(4))
# To read alll the  file read(empty) From The Last Position
print("Frist read --->",File_Handlr.read())
# Close File
File_Handlr.close()
# To Write on file Must Change The Mod3e Frist & Close Befor Change Mode
File_Handlr = open("Try.txt","w")
# here will delet all file and over write on it
# Not Writ On The Same Time Becuse it on the hard disk not Ram
File_Handlr .write("This is the a new string ")
# If the file not exist --> Will Creat Anthor new One on write not read on the same directory
File_Handlr = open("Try_2.txt","w")
File_Handlr.write("Hi --> abdo ")
# Close File
File_Handlr.close()

# To Append ---> Will No Format before write
# when file not exist creat file
File_Handlr = open("Try.txt","a")
File_Handlr .write("\n This is the a Append string ")

#flush --> Write the io buffer on the file with out close
# Close File
File_Handlr.close()
File_Handlr = open("Try.txt","r+")
# To read line From The Last Position
File_Handlr.readline()
print("read line --->",File_Handlr.readline())
print("read  Spacific line 3 --->",File_Handlr.readline()[3])

# To Read Line By Line
print("****************** To Read By Line ******************")
File_Handlr = open("Try.txt","r+")
for line in File_Handlr :
    print(line)

print("****************** Try And Catch ******************")
# Try and Catch if you have error do some thing does't give error
try :
    # Befor the error any thing will excute
    print("what is the file -->")
    File_Handlr = open("Wrong_File.txt", "r+")
    # after error will not excut
    print("File open successfuly ")
except:
    # if there is an error do that
    print("no file by this name ")

# -----> Seek
print("****************** Seek ******************")
# Move file handler to spasific bit
File_Handlr = open("Try.txt","r+")
File_Handlr.seek(3)
print("read After Seek --->",File_Handlr.readline())



# Write By List
Worker_File=open("orkers","a")
List_Worker_Name=["Abdo" , "Abdullah","Fady","Sara","Mariam"]
Worker_File.writelines(List_Worker_Name)
Worker_File.close()

#/========/ Task /========/
# Write python code that generate an initialization function for DDRA REG in Atmega32
# The System Will Ask User to enter the mode for each pin , then generate a function called :
# void DDRA_init(void) that do the code




#/========/ Task /========/
# Phone Book
# Show  Contant
# Show All Contant
# Add Contant
# Update Contant
# Delet Contant
# Delet All
# Exit
