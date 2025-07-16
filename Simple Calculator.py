# Description: Develop a basic calculator that can perform four primary arithmetic operations:
# addition, subtraction, multiplication, and division.
# # Create functions for each operation.
# # Take two inputs from the user and allow them to select the desired operation.
# # Handle division by zero with appropriate error messages.
#
input1 = input("Enter value 1: ")
input2 = input("Enter value 2: ")


def arithmetic(x, y):
    return x + y


def substitution(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    try:
        x / 0

    except ZeroDivisionError as e:
        print("Can not divide with zero")
    finally:
        print("This will always output")


print("""Welcome to this Simple Calculator:
Enter input 1 and input 2
Select 1 for addition:
select 2 for substitution:
select 3 for multiplication:
""")