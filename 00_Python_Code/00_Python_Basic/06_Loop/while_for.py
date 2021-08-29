i=1
while i<=10 :
    i += 1
    if i == 6:
    #continue --> Skip Cycle
        continue
    elif i==9:
    #break --> Out
        break
    print(i)


print("Loop has endded")

#For_loop
for index in "ABDO":
    print(index)
# With List
buddies = ["picachu","grandizer", "subzero ","Winner" ]

for bubby in buddies:
    print(bubby)

# With Range
for index in range(5):
    print(index )
#Range From To
for index in range(0,7):
    print(index )
#Range With Step
for index in range( 0 , 10 , 2 ):
    print(index )

for index in range(len(buddies)):
    print(buddies[index])

for index in range(9):
    if index % 2 :
        print(index,"--> an even Num")
    else:
        print(index, "--> an odd Num")

buddies = ["picachu","grandizer", "subzero ","Winner" ]
for index in range(len(buddies)):
    if buddies[index] =="grandizer " or buddies[index] == "picachu":
        print(index,"is Your Frind")

    else:
        print(index, "--> is not Your Frindr " )


#Continu And Break
for index in range( 0 , 10 , 2 ):
    if index ==4:
        continue # Skip Cycle
    if index == 8:
        break   # Out Of Loop
    print(index )

#For_Smae Line
for index in "ABDO":
    print(index , end=" ")


#Reverse input By User
x=input("Enter Word To Be Reversed")
mirror=""
for index in x :
    mirror =  index + mirror

print(mirror)

# By -
x="123456"
for i in  x :
    print("yoyoyoy-->",x[(i*-1)])




# From -1 To Zero
x="fds"
print(x)
for char in range (len(x)-1,-1,-1):
     print(x[char] ,end="")






