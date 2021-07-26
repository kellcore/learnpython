# usual command line argument handling
import sys
script, input_encoding, error = sys.argv

# define main function which will be called at the end of the script


def main(language_file, encoding, errors):
    # read one line from the languages file
    line = language_file.readline()
    # use an if-statement to test if line has something in it
    # the readline function will return an empty string when it reaches the end of the file
    # as long as readline gives us something, the code in the if block will run -> if it doesn't, Python will skip those lines
    if line:
        # call a separate function to do the actual printing of the line
        print_line(line, encoding, errors)
        # call the function from within itself to loop to the next line
        # loop will end when readline returns an empty string - this code won't run
        return main(language_file, encoding, errors)

# start the definition for print_line which does the actual encoding for each line from languages.txt


def print_line(line, encoding, errors):
    # .strip() removes spaces at the beginning and end of the string -> can pass in specific characters to remove as leading/trailing characters
    # in this case, we remove the trailing \n on the line string
    next_lang = line.strip()
    # .encode() encodes the string using the specified encoding -> if none is specified, utf-8 is used as default
    # here, we take the language and encode it into raw bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # .decode() decodes the string using the codec registered for encoding
    # we do the inverse by decoding the bytes from raw_bytes and creating a Python string
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # prints out both strings
    print(raw_bytes, "<===>", cooked_string)


# we're done defining functions, so we open the languages.txt file
languages = open("languages.txt", encoding="utf-8")
# call the main function with all the correct parameters so it gets everything going
main(languages, input_encoding, error)

# this exercise uses the languages.txt file downloaded from https://learnpythonthehardway.org/python3/languages.txt
# ----------
# BITS AND BYTES
# ----------
# computers use electricity to flip switches on or off
# switches can represent:
# 1 = on
# 0 = off
# we call these 1s and 0s "bits"
# computers take these 1s and 0s and use them to encode larger numbers
# a computer will use 8 of these 1s and 0s to encode 256 numbers (0-255)
# encode -> an agreed-upon standard for how a sequence of bits should represent a number
# a "byte" is a sequence of 8 bits (1s and 0s)
# once you have bytes, you can start to store and display text by deciding on another convention for how a number maps to a letter
# ASCII (American Standard Code for Information Interchange) - the most popular convention for mapping a number to a letter
# once you have the ASCII convention for encoding a character using 8 bits (a byte), we can then "string" them together to make a word
# the problem with ASCII -> it only encodes English and a few other similar languages
# turns out there's a lot more characters than 256 used throughout the world
# to solve this problem, Unicode was created
# meant to be a "universal encoding" of all human languages
# you can use 32 bits to encode a Unicode character, and that is more characters than we could possibly find!
# a 32-bit number means we could store 4, 294, 967, 295 characters
# 32 bits = 4 bytes which means there's wasted space in most text we want to encode
# could also use 16 bits (2 bytes), but that still leads to wasted space
# solution -> use a clever convention to encode most common characters using 8 bits and then "escape" into larger numbers when we need to encode more characters
# we have one more convention that is nothing more than a compression encoding which makes it possible for most common characters to use 8 bits and then escape into 16 or 32 as needed
# UTF-8 -> "Unicode Transformation Format 8 Bits" -> convention for encoding text in Python
# it's a convention for encoding Unicode characters into sequences of bytes, which are sequences of bits, which turn sequences of switches on and off
# you can use other conventions but UTF-8 is the current standard
# ----------
# OUTPUT
# ----------
# the ex23.py script is taking bytes written inside the b' ' (byte string) and converting them to the utf-8 encoding specified
# left has numbers for each byte of the UTF-8 (in hexadecimal)
# right has character output as actual UTF-8
# think about this as:
# left side is the Python numerical bytes (or "raw" bytes) Python uses to store the string
# you specify this with b' ' to tell Python this is bytes
# the raw bytes are then displayed "cooked" on the right so you can see the real characters
# ----------
# DISSECTING THE CODE
# ----------
# string - a UTF-8 encoded sequence of characters for displaying or working with text
# bytes are the "raw" sequence of bytes that Python uses to store this UTF-8 string and start with a b' ' to tell Python you are working with raw bytes
# >>> raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
# >>> utf_string = "文言"
# >>> raw_bytes.decode()
# '文言'
# >>> utf_string.encode()
# b'\xe6\x96\x87\xe8\xa8\x80'
# >>> raw_bytes == utf_string.encode()
# True
# >>> utf_string == raw_bytes.decode()
# True
# ----------
# MNEMONIC
# ----------
# DBES - Decode Bytes, Encode Strings
