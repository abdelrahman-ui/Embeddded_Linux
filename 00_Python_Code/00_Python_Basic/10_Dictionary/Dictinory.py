# Key And Value --> Key Must Be Uniqe Or Will Over Write To The Last One
# Dictionaries in {}
#       - Unorder             --> Accessed By Key Not Index Like List
#       - Changable Element   -->
#       - Each Item Has A Key -->
#       - Key Must Be Uniqe
#

Convert_Month = {
    "jan"   : "january",
    "feb"   : "feb",
    "mar"   : "march",
     1      : True,
    "Mar" : ["march","march is third" , 3]
 }
print(Convert_Month["mar"])
# When I'm Use Wrong Key Can Till You Massage If You Not
print(Convert_Month.get("feb","Value Not Here"))
print(Convert_Month.get("fdb","Value Not Here"))
print(Convert_Month.get("Mar","Value Not Here"))

Sallary ={
    "Abdoo" : 2000 ,
    "Magdy" : 4000 ,
    "Dina" : 5000 ,
    "Omar"  : 6000
}
# Changable The Same  Element
Sallary["Abdoo"]=5000
print(Sallary["Abdoo"])
Sallary["Abdoo"]=2000

# lenght
print("Salley index Long -->",len(Sallary))

# With Loop
for Key_Index in Sallary :
    print(Sallary[Key_Index])
# Check if Key Exists
if  "Abdoo" in Sallary:
    print(" It;s Here")

# Function --> pop , clear ,keys, values

# Remove Element Be Key
Sallary.pop("Omar")
print(Sallary)

#Return List Of Key
print("The List Of Key ---> ",Sallary.keys())

#Return List Of Value
print("The List Of Value ---> ",Sallary.values())

# Clear All
Sallary.clear()



# By Dictionary Write Python Code Mange a DataBase For Employees .
# Ecah Employees has a uniqe ID and have Following Data :
# Name ,Salary , age
# 1 -Add New Employee
# 2- Print Employee Data
# 3- Remove Employee From System

Employee_Info={}
def Add_Employee(key):
    Employee_Name =input("Enter New Employee's Name -->")
    Employee_Sallery=int(input("Enter New Employee's Sallary -->"))
    Employee_Age = int(input("Enter New Employee's Age -->"))
    global Employee_Info
    Employee_Info[key]={"Name" : Employee_Name ,"Sallary": Employee_Sallery ,"Age" :Employee_Age}

def Print_Employee(key):
    print(Employee_Info[key])

def Remove_Employee(key):
    Sallary.pop(key)



User_Index =0
while (User_Index !=4):
    User_Index = int(input("Enter Your Option ---->  "))
    if User_Index == 1:
        Uniqe_Key=input("Enter Yor Uniqe Key To Creat---> ")
        Add_Employee(Uniqe_Key)
    elif User_Index == 2 :
        print("The List Of Key ---> ", Employee_Info.keys())
        Uniqe_Key = input("Enter Yor Uniqe Key To Print ---> ")
        Print_Employee(Uniqe_Key)
    elif User_Index == 3:
        Uniqe_Key = input("Enter Yor Uniqe Key To Print ---> ")
        Remove_Employee(Uniqe_Key)
    elif  User_Index == 4:
        print(" Thankes ")
    else:
        print("Error")


