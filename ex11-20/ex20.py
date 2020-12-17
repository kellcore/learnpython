from sys import argv

script, input_file = argv

# define a function called print_all that accepts an argument named f


def print_all(f):
    # reads the f file and prints the contents to the screen
    print(f.read())

# define a function called rewind that accepts an f argument


def rewind(f):
    # f = file
    # a file in Python has a "read head" and you can "seek" this read head around the file to different positions and work with it there
    # each time we do f.seek(0), we move to the start of the file
    f.seek(0)

# define a function called print_a_line that accepts two arguments -> a line_count and an f (file)


def print_a_line(line_count, f):
    # when this function is called, print the number of the current line, read a line from the file and move the read head to right after the \n that ends that line
    # inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far
    # the readline() function returns the \n that's in the file at the end of that line -> adding an end="" at the end of your print function calls avoids adding double \n to every line
    print(line_count, f.readline(), end="")


# create a variable called current_file that opens the input file passed in from the user
current_file = open(input_file)
# prints the whole file to the screen
print("First, let's print the whole file:\n")

print_all(current_file)
# resets the read head back to the beginning of the current file
print("Now, let's rewind kind of like a tape.")

rewind(current_file)
# prints 3 lines from the file, starting with 1, and appending the number to the front of the line
print("Let's print 3 lines:")

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

# current_line = current_line + 1
# print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
