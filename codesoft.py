print("=" * 50)
print("      ADVANCED PYTHON CALCULATOR")
print("=" * 50)

while True:

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Floor Division (//)")
    print("8. Exit")

    choice = input("\nEnter Choice (1-8): ")

    if choice == "8":
        print("\nThank you for using the calculator. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\nInvalid Choice! Please try again.")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print(f"\nResult: {num1} + {num2} = {num1 + num2}")

    elif choice == "2":
        print(f"\nResult: {num1} - {num2} = {num1 - num2}")

    elif choice == "3":
        print(f"\nResult: {num1} * {num2} = {num1 * num2}")

    elif choice == "4":
        if num2 != 0:
            print(f"\nResult: {num1} / {num2} = {num1 / num2}")
        else:
            print("\nError: Division by zero is not allowed!")

    elif choice == "5":
        if num2 != 0:
            print(f"\nResult: {num1} % {num2} = {num1 % num2}")
        else:
            print("\nError: Division by zero is not allowed!")

    elif choice == "6":
        print(f"\nResult: {num1}^{num2} = {num1 ** num2}")

    elif choice == "7":
        if num2 != 0:
            print(f"\nResult: {num1} // {num2} = {num1 // num2}")
        else:
            print("\nError: Division by zero is not allowed!")