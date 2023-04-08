'''try:
    n = int(input("Enter NUMBER NOT STRING OR FLOAT :) "))
    print(n**2)
except ValueError:
    print("please enter NUMBER!! :)")'''

'''try:
    name=str(input("Enter name: "))
    age=int(input("Enter your age: "))
    if age<18:
        print(f"sorry,{name} you are not big enough to be confirmed")
    else:
        print(f"congratulations {name} you have been confirmed")
except ValueError:
    print(f"{name},please enter your age as a NUMBER")'''

'''try:
    num1=int(input("please enter number1: "))
    num2=int(input("please enter number2: "))
    ans=num1/num2
    print(ans)
except ZeroDivisionError:
    print("Number2 is 0 please change it")'''

'''with open("text.txt","w") as fileHandler:
    fileHandler.write("hello")
try:
    with open("text1.txt","r") as fileHandler:
        print(fileHandler.read())
except Exception:
    print("File not found")'''

'''try:
    name=input()
    name.capitalize()
except TypeError:
    print("please enter name as a STRING")'''
