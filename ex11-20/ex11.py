# most of what software does is the following:
# take some kind of input from a person
# change it
# print something out to show how it changed

# putting an end= ' ' at the end of each line tells print not to end the line with a new line character & to go to the next line
# ex. How old are you? 33 (with end=' ' -> all on one line)
# vs. How old are you?
# 33 (without)
# print("How old are you?", end=' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()

# print(f"So, you're {age} years old, {height} tall, and {weight} pounds heavy.")

# what does input() do?
# allows user input
# input(prompt) -> a string representing a default message before the input
# ex. x = input('Enter your name: ')
# print('Hello, ' + x)

# name = input('Enter your name: ')
# print('Hello, ' + name)

# print("Enter a number: ", end=' ')

# num = int(input())

# new_num = num * 2

# print("Your new number is: ", new_num)

print("What's your current age?", end=' ')
age = int(input())
new_age = age + 20
print("What's your name?", end=' ')
name = input()
print("What year is it?", end=' ')
year = int(input())
new_year = year + 20

print(f"Your name will still be {name}! You will be",
      new_age, "years old in", new_year)
