print("CODSOFT Internship - Task 2")
print("Advanced Python Calculator")
print("===== FLEXIBLE CALCULATOR =====")

while True:

    num1 = float(input("\nEnter 1st number: "))
    num2 = float(input("Enter 2nd number: "))

    print("\nChoose Mode:")
    print("1. Normal Mode (use original numbers)")
    print("2. Chain Mode (update result step by step)")

    mode = input("Enter mode (1/2): ")

    print("\nChoose operations (separate by space)")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choices: ")
    operations = choice.split()

    if mode == '1':
        for op in operations:

            if op == '1':
                print("Addition:", num1 + num2)

            elif op == '2':
                print("Subtraction:", num1 - num2)

            elif op == '3':
                print("Multiplication:", num1 * num2)

            elif op == '4':
                if num2 != 0:
                    print("Division:", num1 / num2)
                else:
                    print("Cannot divide by zero")

            else:
                print("Invalid operation:", op)

    elif mode == '2':
        result = num1

        for op in operations:

            if op == '1':
                result = result + num2

            elif op == '2':
                result = result - num2

            elif op == '3':
                result = result * num2

            elif op == '4':
                if num2 != 0:
                    result = result / num2
                else:
                    print("Cannot divide by zero")
                    break

            else:
                print("Invalid operation:", op)

        print("Final Result:", result)

    else:
        print("Invalid mode selected")

    again = input("\nDo you want to continue? (yes/no): ")

    if again.lower() == 'no':
        print("Calculator closed.")

        break
