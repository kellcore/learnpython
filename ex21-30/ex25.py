def break_words(stuff):
    # documentation comments!
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# -----------
# INTERPRETER
# -----------

# >>> import ex25
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# All
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who

# Help on module ex25:

# NAME
#     ex25

# FUNCTIONS
#     break_words(stuff)
#         This function will break up words for us.

#     print_first_and_last(sentence)
#         Prints the first and last words of the sentence.

#     print_first_and_last_sorted(sentence)
#         Sorts the words then prints the first and last one.

#     print_first_word(words)
#         Prints the first word after popping it off.

#     print_last_word(words)
#         Prints the last word after popping it off.

#     sort_sentence(sentence)
#         Takes in a full sentence and returns the sorted words.

#     sort_words(words)
#         Sorts the words.

# -----------
# IMPORT SHORTCUT
# -----------
# Can write your import as from ex25 import * instead!
# this is like saying "import everything from ex25"
#
# >>> from ex25 import *
# >>> sentence = "All good things come to those who wait."
# >>> words = break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']


# -----------
# QUICK NOTE
# -----------
# return from a function gives the line of code that called the function a result
# you can think of a function as taking input through its arguments and returning output through return
# print is completely unrelated to this and only deals with printing output to the terminal
