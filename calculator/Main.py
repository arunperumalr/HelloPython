from Operations import add, subtract, multiply, divide
from Utils import get_number

while True:
    print("\nWelcome to the calculator!")
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = int(input("Please enter your choice: "))
    if choice == 5:
        print("Thank you for using this calculator!")
        break

    x = get_number("Enter 1st number: ")
    y = get_number("Enter 2nd number: ")

    if choice == 1:
        print("Result:", add(x, y))
    elif choice == 2:
        print("Result:", subtract(x, y))
    elif choice == 3:
        print("Result:", multiply(x, y))
    elif choice == 4:
        print("Result:", divide(x, y))
    else:
        print("Invalid Input. Please enter a valid choice.")
