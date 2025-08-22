# calculator.py
# A simple calculator project by Trung

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "❌ Cannot take square root of a negative number"
    return x ** 0.5

def menu():
    print("\n🔢 Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("0. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter choice (0-6): ")

        if choice == "0":
            print("👋 Goodbye!")
            break

        if choice == "6":
            x = float(input("Enter number: "))
            print("Result:", square_root(x))
        else:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(x, y))
            elif choice == "2":
                print("Result:", subtract(x, y))
            elif choice == "3":
                print("Result:", multiply(x, y))
            elif choice == "4":
                print("Result:", divide(x, y))
            elif choice == "5":
                print("Result:", power(x, y))
            else:
                print("❌ Invalid choice, try again.")
