"""
Find Maximum and Minimum Values of a List

Examples (Input -> Output)

* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5

Notes
You may consider that there will not be any empty arrays/vectors.
"""

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

list = [4,6,2,1,9,63,-134]

print(minimum(list))
print(maximum(list))
