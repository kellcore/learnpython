# f-string - special type of string used to format - ex. f"string here {avariable}"
# Python has another type of formatting that uses .format() syntax - applies a format to an already created string such as in a loop

# types_of_people is a variable - in this instance, we set it equal to 10
types_of_people = 10
# x is a variable equal to the formatted string (note the f at the beginning and the {} around the variable)
x = f"There are {types_of_people} types of people."

# more variables
binary = "binary"
do_not = "don't"
# another variable equal to the value of the formatted string
y = f"Those who know {binary} and those who {do_not}."

# print the value of both formatted strings
print(x)
print(y)

# print formatted strings that use the variables containing previously formatted strings
print(f"I said: {x}")
print(f"I also said: '{y}'")

# this variable holds the boolean False
hilarious = False
# this variable doesn't format the string - rather, it contains empty {} and we'll pass in the value that goes there later using .format()
joke_evaluation = "Isn't that joke so funny?! {}"

# prints the value of joke_evaluation and formats the string using . notation / passes in the value that will go inside the empty curly brackets
print(joke_evaluation.format(hilarious))

# two variables with strings not formatted
w = "This is the left side of..."
e = "a string with a right side."

# prints value of both strings with + -> string concatenation!
print(w + e)
