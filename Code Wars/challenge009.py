"""
Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""

def find_short(s):
    list = s.split()
    lenght = float("inf")
    for word in list:
        if len(word) < lenght:
            lenght = len(word)

    return lenght
