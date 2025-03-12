# Version 2 
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    while True:
        print("-"*45)
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("-"*45)
        choice = input("Enter choice (1 to 5): ")

        if choice == '5':
            print("Exiting!")
            break
        elif choice in ['1', '2', '3', '4']:
            while True:
                n1 = input("Enter the first non-negative integer: ")
                if n1.isdigit():
                    number1 = int(n1)
                    break
                else:
					print("Invalid! Please enter a non-negative integer.")

            while True:
                n2 = input("Enter the second non-negative integer: ")
                if n2.isdigit():
                    number2 = int(n2)
                    break
                else:
                    print("Invalid! Please enter a non-negative integer.")

            if choice == '4' and number2 == 0:
                print("Division by zero is not allowed!")
                continue

            if choice == '1':
                ans = add(number1, number2)
                op = "Addition"
            elif choice == '2':
                ans = subtract(number1, number2)
                op = "Subtraction"
            elif choice == '3':
                ans = multiply(number1, number2)
                op = "Multiplication"
            elif choice == '4':
                ans = divide(number1, number2)
                op = "Division"

            print("-"*45)
            print(f"{op} of {number1} and {number2} gives: {ans}")
            print("-"*45)
		else:
            print("Your choice is invalid. Please select a valid choice.")

if __name__ == "__main__":
    main()