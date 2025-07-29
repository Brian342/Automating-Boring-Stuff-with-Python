# Task 1: To-Do List Application
# Description: Build a simple command-line to-do list application.
# Users should be able to add, delete, mark as done, and list tasks.

# Objectives:
# Implement the ability to add, view, and delete tasks.
# Store the tasks in a file (either CSV or JSON format). Mark tasks as completed.
# Implement basic error handling (e.g., trying to delete a task that doesn’t exist).

print("Welcome user to a simple to do list application")

toDoList = []

try:
    print("Options")
    print("1: To add items")
    print("2: To Delete items")
    print("3: To mark item as Done")
    print("4: To show Your List")
    print("0: To Abort Task")

    option = input("Enter either option 1/2/3/4/0 =>")

    if option == 1:
        newItem = input("Enter your Item to the lIst(Enter 0 to cancel) =>")

    else:
        toDoList.append({"task"})

except Exception as e:
    print("Error!")

