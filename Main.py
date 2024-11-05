#https://github.com/Brekkii
input("Welcome, please enter key: ")
User_Key = "Development"

if input == "Development":
 print("Welcome to XYZ")
elif input == "":
 print("Incorrect user key")

Static_Number_Eins = ['']
Invalid_Variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
input("Please choose a number: ")
if input == '':
 print("You have chosen" + input)
elif input == Invalid_Variables:
 print("You have input a variable that is not yet supported.")

Inital_Variables = ['+', '-', '/', '*']
input("Please select a Variable: " + Inital_Variables)

if input == '+':
 print("You have chosen +, please input next number: ")
elif input == '-':
 print("You have chosen -, please input next number: ")
elif input == '/':
 print("You have chosen /, please input next number: ")
elif input == '*':
 print("You have chosen *, please input next number: ")

Static_Number_zwei = ['']
input("Please input next number: ")

if input == Invalid_Variables:
 print("You have input a variable that is not yet supported.")
elif input == '':
 print("You have chosen " + input)
