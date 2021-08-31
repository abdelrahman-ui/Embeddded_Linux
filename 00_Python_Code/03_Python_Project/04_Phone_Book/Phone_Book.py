'''
Write a Python Program using text files
to create and maintain a Phone Book.
The Phone Book will display the
following Menu and will support
the corresponding functionality

*** Phone Book Menu ***
Enter 1,2,3 or 4:
Enter 1 To Display Your Contacts Records
Enter 2 To Add a New Contact Record a new contact
Enter 3 To search your contacts
Enter 4 To Quit
**********************

author: Abdelrahman_Magdy
'''
File_Handler=open("Phone_Book.txt","a+")
File_Handler.close()
''' Function To Show The Meanu Of Phone Book '''
def Show_Option():
    print("*** Phone Book Menu ***Enter 1,2,3 or 4 \n Author : Abdelrahman Magdy")
    print("    Enter 1 To Display Your Contacts Records\n    Enter 2 To Add a New Contact Record a new contact\n    Enter 3 To search your contacts\n    Enter 4 To Quit")
    cohice = int(input("Enter Your Choice :--> "))
    if cohice == 1 :
        File_Handler=open("Phone_Book.txt","r+")
        file_contant=File_Handler.read()
        if len(file_contant)==0:
            print(" The Phone Book Is Empty ")
        else :
            print(file_contant)
        File_Handler.close
        Enter=int(input(" Press On Enter To Continue ..... "))
        Show_Option()
    elif cohice == 2 :
        Add_Contant()
        Enter = int(input(" Press On Enter To Continue ..... "))
        Show_Option()
    elif cohice == 3:
        Search_Contant()
        Enter = int(input(" Press On Enter To Continue ..... "))
        Show_Option()
    elif cohice == 4:
        print("Thanks for using Phone Book Program presented by Abdelrahman Magdy ")
    else:
        print("Wrong choice, Please Enter [1 to 4]\n")
        Enter = input("Press Enter to continue ...")
        Show_Option()


def Add_Contant():
    FristName =input(" Enter The Contant Frist Name :  ")
    LastName = input(" Enter The Contant Last Name  :  ")
    PhoneNum = int(input("Enter The Contant Number "))
    contant=([FristName , LastName  , PhoneNum ])
    print("\n")
    File_Handler=open("Phone_Book.txt","a")
    Global_ContantNum=1
    File_Handler.write(ContantNum ,contant)
    Global_ContantNum +=1
    print(contant[0:1] ("has been added successfully!")

def Search_Contant():
     FristName = input("Enter The Frist Name For Search --->  ")
     SecondName= input("Enter The Frist Name For Search --->  ")

    File_Handler = open("Phone_Book.txt", "r")
    File_Contant=File_Handler.readline()
    Found = 0
    for line in File_Contant :
        if FristName in line & SecondName in line :
            print("Your Required Contact Record is:", end=" ")
            print(line)
            Found=1
            break
    if Found == 0 :
       print("There's no contact Record in Phone Book with name = ")

Show_Option()


