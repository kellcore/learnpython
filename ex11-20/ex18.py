# this one is like the scripts with argv
# we tell python we want to make a function using def for define
# we give the function a name on the same line as def
# we tell it we want *args which is like argv parameter but for functions
# we end the line with a colon and indent

# the * tells Python to take all the arguments to the function and then put them in args as a list
def print_two(*args):
    # first indented line unpacks the arguments
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# okay, that *args is actually pointless, we can just do this:
# this skips the unpacking arguments step and just uses the names we want inside the parentheses


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument


def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no arguments


def print_none():
    print("I got nothin'.")


print_two("Kelly", "Corey")
print_two_again("Kelly", "Corey")
print_one("First!")
print_none()
