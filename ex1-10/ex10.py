# the backslash character \ encodes difficult to type characters into a string
# there are various escape sequences available for different characters (ex. "I am 6'2\" tall." -> escape double-quote inside string)
# can also use triple quotes """ """ -> can put as many lines of text as you'd like between the quotes
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fatter_cat = """
I'll do another list: \n\t* Noms\n\t* Cheezburgers\n\t* String
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fatter_cat)

calico_cat = '''
Here's a cool new list for all the hep cats!
\t* Cat \\ Essentials \\
    \t\v+ Springy Grass
    \t\v+ Toe Bean Cleaner
    \t\v+ Tail Fluffer
'''
print(calico_cat)
