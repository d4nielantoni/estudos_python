"""
Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!


The number 89 is the first integer with more than one digit that fulfills the property partially introduced
in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number:
89 8**1 + 9**2
The next number in having this property is 135:
See this property again: 135 1**1 + 3**2 + 5**3
Task
We need a function to collect these numbers, that may receive two integers a, b that defines the range
[a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described
above.

"""
a = 1
b = 100
 
def sum_dig_pow(a, b):
    eureka = []
    for i in range(a, b + 1):
        total = 0
        for j in range(len(str(i))):
            total += int(str(i)[j]) ** (j + 1)
        if total == i:
            eureka.append(total)
    return eureka

print(sum_dig_pow(a, b))

