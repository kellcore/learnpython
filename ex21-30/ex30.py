# create and set the values for our variables
people = 30
cars = 40
trucks = 15

# if the number of cars is greater than the number of people, print this statement
if cars > people:
    print("We should take the cars.")
# otherwise, if the number of cars is less than the number of people, print this statement
elif cars < people:
    print("We should not take the cars.")
# if neither of the above expressions results in True, print this statement
else:
    print("We can't decide.")
# if the number of trucks is greater than the number of cars, print this statement
if trucks > cars:
    print("That's too many trucks.")
# otherwise, if the number of trucks is less than the number of cars, print this statement
elif trucks < cars:
    print("Maybe we could take the trucks.")
# if neither of those expressions are true, print this statement
else:
    print("We still can't decide.")
# if the number of people is greater than the number of trucks, print this statement
if people > trucks:
    print("Alright, let's just take the trucks.")
# otherwise, print this statement
else:
    print("Fine. Let's stay home then.")
