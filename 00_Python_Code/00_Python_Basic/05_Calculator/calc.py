# Calculator
num1 = float(input("Enter Frist Value"))
num2 =  float(input("Enter Second Value"))
operator = input("Please Enter The Operator ")
if operator == "+" :
    print(num1 + num2)
elif operator == "-" :
    print(num1 - num2)
elif operator == "*" :
    print(num1 * num2)
elif operator == "/" :
    print(num1 / num2)
elif operator == "%" :
    print(num1 % num2)
elif operator == "//":
    print(num1 // num2)
else :
    print(" Wrong Operator Please Try Again ")

