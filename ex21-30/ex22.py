# What Do You Know So Far?

# print() prints a string to the screen -> like console.log() in JS
# comments are preceded with a # -> called an octothorpe
# text or code with a # in front of it will be grayed out and not run when you run the program
# % is a modulus operator -> gives remainder of left value divided by right value
# this prints 0 as the result since 2 divides evenly into 4
print("4 % 2 = ", 4 % 2)
# True and False are booleans -> binary values
# use the equals sign to create a variable -> Python uses snake case, so word_word is valid syntax instead of camel case's wordWord -> make sure your variable name isn't a protected word
# add an f to format strings when printing
# to print the value of a variable, use brackets around the variable name ex. {word}
# can also use .format() syntax to format a string -> more often used with an already created string you might find in a loop
# can use + sign to concatenate two strings saved to variables ex. print (w + e) will print the strings saved to both variables
# end=' ' adds a space between words instead of printing them on two separate lines
# formatter.format() function
# create variable called formatter and set it equal to a string holding 4 {}
# call .format function on the formatter variable -> formatter.format() and pass 4 arguments that match up with the 4 {} in formatter -> doesn't have to be 4 specifically, just make sure the number of arguments matches the number of {} in formatter
# if you print(formatter.format()), this creates and prints a new string that has {} replaced with the 4 arguments you passed in
# \n is a new line character -> this is very handy!
# if you have a multi-line paragraph or something similar to print, use triple quotes instead of double or single
# there a various escape sequences available for different characters -> use a backslash \ to encode in a string ex. "I am 5' 8\" tall." uses \ to escape the double quotes
# \t is a tab
# \v prints the text next to it in a newline after a tab space
# can use built-in input() function to get input from a user
# input(prompt) -> a string representing a default message before the input
# anything captured from an input will be a string, so if you want to accept a number from a user and use it as an integer, you have to use int(input()) to convert it
# pydoc -> documentation generator and online help system
# the argument to pydoc can be the name of a function, module, package, etc. -> ex. entering pydoc input in terminal
# open -> opens a file using the file() type and returns a file object
# file object -> when opening a file, the mode can be r (reading -> default mode), w (writing), or a (appending)
# file will be created when opening if it doesn't already exist and will be truncated when opened for writing
# can add a + to the mode for simultaneous reading and writing
# os -> miscellaneous operating system interfaces -> provides a portable way of using operating system dependent functionality
# sys -> system-specific parameters and functions -> always available -> provides access to objects maintained/used by the interpreter & functions that interact strongly with the interpreter
# script -> another name for .py files
# python3 ex13.py -> ex13.py is called an argument
# you write a script that accepts arguments
# import -> how you add features to your script from Python feature set -> aka modules or libraries
# argv -> argument variable -> holds the arguments you pass to your script when you run it
# syntax -> from sys import argv
# script, first, second, third = argv -> this takes whatever's in argv, unpacks it, and assigns it to all of the variables on the left in order
# argv vs input()
# difference has to do with where the user gives input
# use argv when you want the user to give your script inputs on the command line
# use input() when you want the user to give your script inputs with their keyboard while the script is running
# .read() -> reads text file and prints file object to the screen -> no parameters
# .close() -> closes the text file -> make sure you run this before your script ends!
# .truncate() -> empties the file
# .write() -> writes to file
# exists -> returns True if a file exists based on its name in a string as an argument and returns False if it does not
# def -> defines a function
# format for creating Python functions:
# def print_two_again(arg1, arg2):
# print(f"arg1: {arg1}, arg2: {arg2}")
# end the def line with a colon and indent the next line
# indentations matter in Python!
# dedent when the function ends
# *args -> take all the arguments to the function and put them in args as a list
# you can pass in math problems as arguments instead of numbers or values
# ex. cheese_and_crackers(10 + 20, 5 + 6)
# you can also pass in variables and perform math operations on them
# ex. cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# a file in Python has a "read head" and you can "seek" this read head around the file in different positions and work with it there
# ex. f.seek(0) -> moves to the start of the file
# readline() -> returns the \n that's in the file at the end of that line -> adding end="" at the end of your print function calls avoids adding double \n to every line
