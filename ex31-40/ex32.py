the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists -> first, start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# the range() function returns a sequence of numbers, starting with 0 by default, incrementing by 1 (by default) and stopping before a specified number
# range(start, stop, step)
# step is an optional parameter which changes how the range increments
for i in range(0, 6, 2):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

print(type(elements))
