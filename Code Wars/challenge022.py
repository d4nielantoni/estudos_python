"""
Count characters in your string

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should
be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(s):
    counter = {}
    for i in s:
        counter[i] = counter.get(i,0) + 1
    return counter

print(count(''))
print(count('Hello world'))