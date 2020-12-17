# we define our function, name it cheese_and_crackers, and pass it two arguments called cheese_count and boxes_of_crackers
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
# we print a formatted string with cheese_count
# print(f"You have {cheese_count} cheeses!")
# we print a formatted string with boxes_of_crackers
# print(f"You have {boxes_of_crackers} boxes of crackers!")
# we print two more strings and end with a new line character
# print("Gosh, that's enough for a party!")
# print("Get a blanket.\n")


# we print a line about passing in just numbers to the function
# print("We can just give the function numbers directly:")
# we call the function and pass in two integers
# cheese_and_crackers(20, 30)

# we print a line about passing in variables
# print("OR, we can use variables from our script:")
# we store our integers in two different variables
# amount_of_cheese = 10
# amount_of_crackers = 50
# we call the function again and pass in the two variables instead of the raw numbers
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we print a line about doing math with the arguments
# print("We can even do math inside too:")
# we run the function again and pass in two addition problems as arguments instead of numbers or variables
# cheese_and_crackers(10 + 20, 5 + 6)

# we print a line about combining variables with math
# print("And we can combine the two, variables and math:")
# we run the function again, pass in the variables, and perform a math operation on the variables
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def give_mouse_cookie():
    yes_cookie = input("Should we give a mouse a cookie? Y/N ")
    if (yes_cookie == "Y"):
        cookie_count = input("How many cookies? ")
        print(f"You gave a mouse {cookie_count} cookies!")
    else:
        print("No cookies for mouse! This is so sad.")


give_mouse_cookie()
