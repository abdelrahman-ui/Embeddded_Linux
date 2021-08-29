# Function Can Take Arrgument And Return

def ADD(NUM1,NUM2):
    return NUM1+NUM2

print(ADD(NUM2=5,NUM1=1))

def Say_Hi(Copy_Index ,Copy_Set):
    x=input("User Name --> ")
    print("HI ", x)
    print("Your Index = " ,Copy_Index )
    print("Your high = ", Copy_Set)
# Call Fun
Say_Hi(0,155)

#Return --> The Last In Function

def Cube(Num):
    cube=Num*Num*Num
    return cube

print("Cube-->",Cube(3))

def sum(num1 , num2):
    sum = num1 +num2
    return sum
print("sum --->" , sum(2,3))


# Function
def Welcome(Copy_Name):
    print("Welcome",Copy_Name)

# Call Fun
Welcome("ABDO")

#With Out Return Return None
x=Welcome("AVD")
print(x)


# Global Variable --> With Out Use Return globale only in the conition but out by defult it is global
result = 0
def ADD(NUM1,NUM2):
    global result
    result= NUM1+NUM2

ADD(5,5)
print(result)

#Power Of Function
def Power_Fun(Base_Num,Pow_Nun):
    result = 1
    for index in range(Pow_Nun)
        result *=Base_Num
    return result

