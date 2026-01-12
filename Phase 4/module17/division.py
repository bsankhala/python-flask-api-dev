
def divide_numbers():
    try:
        print("=== Division Program ===")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2   # may raise ZeroDivisionError

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    else:
        print("Result:", result)

    finally:
        print("Operation complete.\n")

while True:
    divide_numbers()
    ch = input("Do you want to divide again? (y/n): ").lower()
    if ch != 'y':
        print("Exiting program.")
        break
