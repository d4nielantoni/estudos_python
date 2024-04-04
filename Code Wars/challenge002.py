"""
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.

"""

def invert(lst):
    invert_list = []
    for number in lst:
        list.append(number * -1)

    return invert_list

print(invert([1,2,3,4,5]))


