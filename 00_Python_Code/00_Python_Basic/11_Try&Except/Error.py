# To Avoid Error --> Try & Except

try:
    x=int (input("Enter a Number : -->   "))
    print(x)
    print("success")
    result = 10 / 0
    print(result)
except ValueError as Error_2:
    print("Invalid Error ")
    print(Error_2)
except ZeroDivisionError as Error 1:
    print(" you Can not div by Zero ")
    print(Error)

