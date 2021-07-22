def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTPLYING {a} + {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 4)
height = subtract(70, 2)
weight = multiply(80, 4)
iq = divide(240, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle:")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# divide the result of iq by 2
# multiply that result by the result of weight
# subtract that result by the result of height
# add that result to the result of age

print("Let's do it the long way!")
div = divide(iq, 2)
mult = multiply(weight, div)
sub = subtract(height, mult)
plus = add(age, sub)

print("That becomes: ", plus)
