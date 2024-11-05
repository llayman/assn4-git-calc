import random

def show_menu():
    print("\n---- Calculator Menu ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Generate Random Number")
    print("6. Quit")
    choice = input("Please select an option (1-6): ")
    return choice

def get_numbers(msg1: str, msg2: str) -> tuple[float, float]:
    while True:
        try:
            num1 = float(input(f"{msg1}: "))
            num2 = float(input(f"{msg2}: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def main():
    while True:
        choice = show_menu()

        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers("Enter the first number", "Enter the second number")

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {'Undefined' if num2 == 0 else num1 / num2}")
        elif choice == '5':
            num1, num2 = get_numbers("Enter the lower bound", "Enter the upper bound")
            print(f"Random number between {num1} and {num2}: {random.random() * (num2 - num1) + num1}")
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
