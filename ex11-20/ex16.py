from sys import argv
# create two variables called script and filename & assign them to argv (argument values)
script, filename = argv
# prints the next 3 lines to the screen. the first string is formatted and contains the filename passed in by the user (ex. test.txt)
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# prints the ? to the screen and waits for user input
input("?")
# if user presses enter, prints the string, opens the file, prints the next screen, and truncates (empties) the file
print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()
# prints line and asks for user input 3 times
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
# prints line to the screen
print("I'm going to write these to the file.")
# takes user input and prints it inside file created earlier (ex. test.txt) -> \n is a new line
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# target.write only takes one argument, so this won't work -> argument must be str, not tuple
# target.write(line1, "\n", line2, "\n", line3)

lines = f"{line1}\n{line2}\n{line3}\n"
target.write(lines)

# prints final string and closes file
print("And finally, we close it.")
target.close()

print("\nLet's see what you added: ")
txt = open(filename)
print(txt.read())
txt.close()
