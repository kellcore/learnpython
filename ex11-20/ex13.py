# script - another name for .py files

# python3 ex13.py -> ex13.py part of the command is called an argument

# write a script that accepts arguments

# import -> this is how you add features to your script from the Python feature set -> better known as modules or libraries
# argv -> argument variable -> holds the arguments you pass to your Python script when you run it
# from sys import argv

# read the WYSS section for how to run this!
# this line unpacks argv so that instead of holding all of the arguments, it gets assigned to four variables you can work with: script, first, second, and third
# "take whatever's in argv, unpack it, and assign it to all of these variables on the left in order"
# script, first, second, third = argv

# print("The script is called: ", script)
# print("Your first variable is: ", first)
# print("Your second variable is: ", second)
# print("Your third variable is: ", third)

# what happens if you run python3 ex13.py first 2nd? throws an error that says "not enough values to unpack (expected 4, got 3)" -> looking for script, first, second, and third, and you only entered script, first, and second

# from sys import argv
# script, first_word, second_word, third_word, fourth_word = argv

# print("The script is called: ", script)
# print("Your first variable is: ", first_word)
# print("Your second variable is: ", second_word)
# print("Your third variable is: ", third_word)
# print("Your fourth variable is: ", fourth_word)

from sys import argv

script, name, age, password = argv
name = input("What's your name? ")
age = input("How old are you? ")
password = input("What's your password? ")

print("The script is called: ", script)
print("Your name is: ", name)
print(f"You are {age} years old")
print("Your password is: ", password)

# what's the difference between argv and input()?
# the difference has to do with where the user is required to give input
# if they give your script inputs on the command line, you use argv
# if you want them to input using the keyboard while the script is running, you use input()
