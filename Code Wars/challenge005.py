"""
Convert a string to an array

Write a function to split a string and convert it into an array of words.

"""

def string_to_array(s):
    split_string = s.split(" ")
    return split_string

teste = string_to_array("Hello World")
print(teste)