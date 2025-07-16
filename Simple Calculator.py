# Description: Develop a basic calculator that can perform four primary arithmetic operations:
# addition, subtraction, multiplication, and division.
# # Create functions for each operation.
# # Take two inputs from the user and allow them to select the desired operation.
# # Handle division by zero with appropriate error messages.
#
print("""Welcome to this Simple Calculator:
Enter value 1 and value 2""")
print()
input1 = int(input("Enter value 1: "))
input2 = int(input("Enter value 2: "))

print("""
         Select 1 for addition:
         select 2 for substitution:
         select 3 for multiplication:
         select 4 for division:""")
print()
select = input("Enter selection: ")


def arithmetic(x, y):
    sum = x + y
    print(f"sum = {sum}")


def substitution(x, y):
    sub = x - y
    print(f"substitution = {sub}")


def multiplication(x, y):
    mult = x * y
    print(f"Multiplication = {mult}")


def division(x, y):
    try:
        div = x / y
        print(f"Division = {div}")
    except ZeroDivisionError as e:
        print("Can not divide with zero")
    finally:
        print("This will always output")


if select == '1':
    arithmetic(input1, input2)
elif select == '2':
    substitution(input1, input2)
elif select == '3':
    multiplication(input1, input2)
elif select == '4':
    division(input1, input2)
else:
    print("invalid selection")
