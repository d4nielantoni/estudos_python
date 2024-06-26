"""
Sum Mixed Array

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

"""
def sum_mix(arr):
    return sum(int(num) for num in arr)

print(sum_mix([1, 2, 3, 4, 5]))