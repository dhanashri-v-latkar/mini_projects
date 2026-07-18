from calculator import *
from utils import get_number

while True :

    print("\n===Smart Calculator===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Cube")
    print("7. Power")
    print("8. Square Root")
    print("9. Percentage")
    print("10. Exit")

    choice  = input("enter your choice: ")

    if choice == "1":
        a = get_number("enter first number: ")
        b = get_number("enter second number : ")
        print("answer = " ,add(a,b))
    
    elif choice == "2":
        a = get_number("enter first number: ")
        b = get_number("enter second number : ")
        print("answer = " ,sub(a,b))
    
    elif choice == "3":
        a = get_number("enter first number: ")
        b = get_number("enter second number : ")
        print("answer = " ,mul(a,b))

    elif choice == "4":
        a = get_number("enter first number: ")
        b = get_number("enter second number : ")
        print("answer = " ,div(a,b))

    elif choice == "5":
        a = get_number("enter  number: ")
        print("answer = " ,sq(a))

    elif choice == "6":
        a = get_number("enter  number: ")
        # b = get_number("enter second number : ")
        print("answer = " ,cube(a))

    elif choice == "7":
        a = get_number("enter first number: ")
        b = get_number("enter second number : ")
        print("answer = " ,power(a,b))

    elif choice == "8":
        a = get_number("enter  number: ")
        # b = get_number("enter second number : ")
        print("answer = ", sq_rt(a))

    elif choice == "9":
        a = get_number("enter first number: ")
        b = get_number("enter second number : ")
        print("answer = ", percent(a,b),"%")

    elif choice == "10":
        print("thank you for using smart calculator")
        break
    
    else:
        print("invalid choice.")