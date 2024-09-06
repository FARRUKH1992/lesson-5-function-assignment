# using while loop create The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Create functions for each arithmetic operation.
# Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
# Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    return result

def main():
    while True:
        print("\nWelcome to the Calculator App!")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Input # operation
        operation = input("Enter choice (1/2/3/4/5): ")

        if operation == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if operation not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue

        # Input amnount numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform the selected operation
        if operation == '1':
            print(f"Result: {add(num1, num2)}")
        elif operation == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif operation == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif operation == '4':
            result = divide(num1, num2)
            if result is not None:
                print(f"Result: {result}")

if __name__ == "__main__":
    main()  



# The aim of this assignment is to create a program that helps users make a shopping list.
# Write a function that lets the user add items to a list.
# Include a function to remove items from the list.
# Add a function that prints out the entire list in a formatted way.



def add_item(shopping_list):
    item = input("Enter the item to add: ")
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("You did not enter any item.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def print_list(shopping_list):
    if shopping_list:
        print("\nShopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = []
    
    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Exiting the shopping list maker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()