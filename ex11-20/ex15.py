# importing argv module from sys package to use in our script
from sys import argv
# create two variables called script and filename and assigning them to argv (argument values)
script, filename = argv
# opens a file using the file() type and returns a file object -> this is the preferred way to open a file -> assigns it to variable txt
txt = open(filename)
# prints out the name of the file passed in as filename
print(f"Here's your file {filename}: ")
# what you get back from open is a file and we give it a command using the ., the name of the command, and parameters just like with open and input
# txt.read() says "Hey, txt! Do your read command with no parameters!"
# reads the txt file created above and prints the file object to the screen
print(txt.read())
txt.close()
# a message asking for the filename from the user
print("Type the filename again: ")
# creates an input for the user to type the filename again with the prefix > and assigns it to the variable file_again
file_again = input("> ")
# opens the file object named in file_again and assigns it to the variable txt_again
txt_again = open(file_again)
# reads the file object found in txt_again and prints the file object to the screen
print(txt_again.read())
txt_again.close()

# can delete filename from argv and this will run with just the name of the script - user can enter filename as part of input instead
# print("Enter filename here: ")
# file_name = input("> ")
# new_txt = open(file_name)
# print(f"Here's your file {file_name} and its file object: ")
# print(new_txt.read())
