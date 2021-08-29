# if
is_hungry =True
Wants_To_Eat=True
if not is_hungry and Wants_To_Eat  ==True:
    print("3ayez 2eh")
elif is_hungry  and  Wants_To_Eat == True           :
    print("Go Eat")
else:
    print("GO Out")


def Max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
       return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
         return num3

X=Max_num(2,88,10)
print(X)

def Match(IntOrStr1 , IntOrStr2):
    if IntOrStr1 == IntOrStr2 :
        print(" The Two String Do Match")
    else:
        print(" The Two String Do not Match")

Match(5,"KL")
