# write a code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam and prints
# greetings!
# if anything else is stored in spam

spam = [1, 2, 3]
for details in spam:
    if details == 1:
        print("Hello")
    elif details == 2:
        print("Howdy")
    else:
        print("Greetings")