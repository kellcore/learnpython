# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weigh? ")

# print(f"So, you're {age} years old, {height} tall, and {weight} pounds.")

# pydoc -> documentation generator and online help system
# ex. pydoc input in terminal
# pydoc automatically generates documentation from Python modules
# the argument to pydoc can be the name of a function, module, or package, or a dotted reference to a class, method, or function within a module or module in a package
# info via https://docs.python.org/3/library/pydoc.html

# open -> opens a file using the file() type and returns a file object -> this is the preferred way to open a file

# file is an object -> mode can be 'r' (reading -> default mode), 'w' (writing), or 'a' (appending)
# file will be created if it doesn't exist when opened for writing or appending -> will be truncated when opened for writing
# add a 'b' for binary files
# add a '+' to the mode for simultaneous reading and writing

# os -> OS routines for NT or Posix depending on what system we're on -> miscellaneous operating system interfaces
# provides a portable way of using operating system dependent functionality
# this exports all functions from posix, nt, etc.
# programs that import and use 'os' stand a better chance of being portable between different platforms

# sys -> provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter
# system-specific parameters and functions
# it is always available

# takes the input first and then prints the question and the input together -> doesn't work!
print("How old are you?", input())
