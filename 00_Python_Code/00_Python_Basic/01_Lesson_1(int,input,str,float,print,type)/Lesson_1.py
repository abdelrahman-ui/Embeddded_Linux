#include math lib
from math import *

# \n = dowen line
x="Hello \n World"

# \t = tape or 4 space
x="Hello \t World"

# upper() = Make All World Capital & isupper() = Ask is that Capital
print(x.upper().isupper())

# lower() = Make All World Small& islower()= Ask is that Small
print(x.lower().islower())

# len = Number of Element in  Variable
print(len(x))

# [] = spacific Element in variable
print(x[0])

Frist_Name= "Abdo"
Last_Name= "Magdy"
# Print The Frist element of Abdo --> A ,Second element of Magdy --> a
print(Frist_Name[0],Last_Name[1])

# Sreach The order of spacific element
print(Frist_Name.index("o"))

# Replace Ab To 3B
print(Frist_Name.replace("Ab","3B"))

x="Ahmed"
# Y is String
y="5"
#  Type = Give The Type Of Var
f=type(x)
z=type(y)
print(f)
print(z)

# Change The Var Type To int
y=int(y)
z=type(y)
print(z)

x="Abdo"
y=15
# Give Variable To Print
print("Name",x)
print("age ",y)

#
print("Modulus ---> " ,10%3)
print("Float Devision --> ",10 // 3)

x=-5
# The abslute Value of x
print(abs(x))

print(type(x))
# Change Type To String
print(type(str(x)))

# Get The Max Num
print(max(4,5,10,44,50))
# Get The Mini Num
print(min(1,5,10,44,50))

print(round(3.2))
print(round(3.8))

#The Power 2**4 = pow
print(pow(2,4))
print(2**4)
#The Root
print(sqrt(4))

#Get Input From User input is string
x=input("Enter Value Of X -->  ")
print(" Value Of x = ", x)
# Type Of Any Input Is String So If You must Transfer it by int
print(type(x))
x=int(x)
print(type(x))

# Calculator
num1 = input("Enter Value Of num1 :  ")
num2 = input("Enter Value Of num2 :  ")
# Transform As Interger
num1=int(num1)
# Transform As Float
num2=float(num2)

sum =num1+num2
print("sum = ",sum )

