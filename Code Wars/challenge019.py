"""
Beginner Series #2 Clock

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
"""


def past(h, m, s):
    result = (h * 3600000) + (m * 60000) + (s * 1000)
    return result


print(past(0, 1, 1))
