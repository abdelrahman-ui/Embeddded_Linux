#Lists is a collection of ordered and changable variables
#Square Brackets
#Allow Duplicate Member
#Members Can Have Diierent Types


List_1=["Abdo", 23 , "Magdy" , 55 , "Dina", 18 ]
print("- Name is  :\t ",List_1[0] ,"     - My Age : " , List_1[1] ,"\n- Dad Name :\t ",List_1[2],"\t- His Age :", List_1[3] )
print("print from last ", List_1[-2])
#Rang From To
print(List_1[0:3])
#To The End
print(List_1[1:])
#len list --> == Element of List
print(len(List_1))
#Replace
List_1[4]="Omer"
print("Replace->",List_1[4])

# For  With List



# Function With List
FristNameList=["Abdo" , 23 , "Omar", 22 , "Dina" , 18 , "Ahmed ",7 , "Mahmoud", 22]
print("Show Frist List Element \n ", FristNameList)
SecondNameList=["Magdy" , 64 , "Tarek" , 63]
print("Show Second List Element \n ", SecondNameList)


print("/******************************__ Add Element to List__******************************/")

# Extend : connection list Put Second In Frist = FristNameList += SecondNameList
FristNameList.extend(SecondNameList)
print("PRINT ALL LISTS \n", FristNameList)

# Insert Element put position and element -- > Add Any Where
FristNameList.insert(0,"Sherif")
print("PRINT AFTER + LISTS \n", FristNameList)

#Append == Add Element At Last
FristNameList.append("A4RAF")


print("/******************************__ Remove List__******************************/")

#Remove Element --> only Frist Element If it is repeated
FristNameList.remove("Sherif")
print("PRINT AFTER Remove \n", FristNameList)

print("/******************************__ Pop   List__******************************/")

#Pop Last Element And Still Save At In Var if you need
The_Poped = FristNameList.pop()
print("PRINT AFTER Popping  \n", FristNameList)
print("The Poped = ", The_Poped)

print("/******************************__ Count Repeat  List__******************************/")

#Count Repeat value
List_1=["Abdo", 23 , "Magdy" , 55 , "Dina", 18 ,"Abdo", 23,"Abdo", 23  ]
print("The Num of ( Abdo ) of List --> ", List_1.count("Abdo"))

print("/******************************__ Sortting  List__******************************/")
# Sortting ( Ascending & Descending )
List_Name=["Abdo", "Magdy" , "Dina"]
List_Name.sort()
print("After Sortting --> ",List_Name)
List_Num=[1 ,52,65,5854]
List_Num.sort()
print("After Sortting --> ",List_Num)

print("/******************************__ Copy  List__******************************/")

#Copy List shallow Copy --> if  i change in one List other one will not sense
Newlist=List_Num
print("=",Newlist)
COPY_LIST= List_Num.copy()
print("After Copy ---> " , COPY_LIST )
List_Num.pop()
print("After popping -->",List_Num)
print("After popping -->",COPY_LIST)
# Will Sense Change
print("=",Newlist)

print("/******************************__ Sreach  List__******************************/")

#Sreach in List if element in list
print("Is here give The index of it---> ",FristNameList.index("Abdo"))
if "Abdo" in FristNameList :
    print("Abdo in My List")
else:
    print("Abdo not in My List")



#Mex List Sortting
#MexList=["Abdo", 23 , "Magdy" , 55 , "Dina", 18 ,"Abdo", 23,"Abdo", 23 ]
#MexList.sort()
#print("After Sortting Mex List --> ",MexList)

print("/******************************__ Clear  List__******************************/")
#Clear All List
FristNameList.clear()

# Nested List --> Lists Inside Of A List
print("/******************************__ Nested List__******************************/")
Nasted_List_1 = [["Abdo", "Magdy", "Dina","Omar"],[2000,3000,4000,5000]]
# To Acsses [List][Element in list]
print(Nasted_List_1[0][2])
# String Are List By The Way
Nasted_List_2= ["Abdo", "Magdy", "Dina","Omar"]
print(Nasted_List_2[0][2])
Num_List = [
    [1,2,3,5],
    [5,1,2,5],
    [54,5,8,22]
]
print("/******************************__ Nested Loop__******************************/")

for row in Num_List:
    print(row)
    for colum in row :
        print(colum)

print("/******************************__ Task List__******************************/")

# Task Sreach About Sallery From Name
#Frist Way
List_Name=["Abdo", "Magdy", "Dina","Omar"]
List_Sallery=[2000,3000,4000,5000]

User_Input=input(" Enter The Name Of User -->  ")
if User_Input in List_Name :
    User_Sallery=List_Name.index(User_Input)
    print("Sallery of --->" , User_Input ," = ", List_Sallery[User_Sallery])
else:
    print("Name Not Founnd")
#Second Way
List_Name_Sallery = ["Abdo" ,2000,"Magdy",3000, "Dina",4000,"Omar",5000]
User_Input=input(" Enter The Name Of User --> ")
if User_Input in List_Name :
    User_Index=List_Name_Sallery.index(User_Input)
    print("Sallery of --->" ,List_Name_Sallery[User_Index]," = ", List_Name_Sallery[User_Index+1])
else:
    print("Name Not Founnd")


print("/******************************__ Task List__******************************/")

# Write A Python cODE That Code To Do List For The User .
# The The System Shall Give The User The Option To Do
# 1- Add To Do  Item
# 2- Print The To Do List
# 3- Print The Done List
# 4- Enter "End" To Exit
# Please Enter Your Choice

# Global Var

ToDo_List=[]
Done_List=[]

def Add_Item(item):
    global ToDo_List
    ToDo_List.append(item)

def Print_List(List_Name):
     for index in range(len(List_Name)):
        print(index,"- ",List_Name[index])

def MoveFromTo(Item):
        global ToDo_Lis
        global Done_List
        Done_List.append(item)
        ToDo_List.remove(item)

item=0
UserOption =0

while(UserOption !=5) :
    UserOption = int(input("Please Enter Your Option Based On The Table : "))
    if UserOption == 1 :
        item=input("Enter Item--> ")
        Add_Item(item)
    elif UserOption == 2:
        Print_List(ToDo_List)
    elif UserOption == 3:
        Print_List(Done_List)
    elif UserOption == 4:
        item = input("Enter Item--> ")
        MoveFromTo(item)
    else:
        print(" Error ")
print("/******************************__ Thanks__******************************/")


print("/******************************__ Task List__******************************/")
# What Will Happen To List If I ChanGe Var Inserted iN iT
x_1 ,x_2 ,x_3= 4 , 5 , 6
list = [x_1,x_2,x_3]
print("Befor Change -->",list)
# When I Change Var The Var Change But In List It Take Only Copy
x_1 , x_2 ,x_3  = 14 , 15 ,16
print("After Change -->",list)
