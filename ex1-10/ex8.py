formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
# formatter.format() is a function -> turns the formatter variable into other strings
# how does formatter.format() work?
# takes formatter string defined on line 1
# calls format function on it
# passes format 4 arguments which match up with the 4 {} in the formatter variable
# creates & prints new string with {} replaced with the four variables
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
