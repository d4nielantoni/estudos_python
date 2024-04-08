"""
Third Angle of a Triangle

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle
"""

def other_angle(a, b):
    c = 180 - (a + b)
    return c

print(other_angle(30,30))