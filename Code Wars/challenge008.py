"""
Basic Mathematical Operations

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
"""

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    else:
        return "Invalid"


test_sum = (basic_op("+",1,2))
test_sub = (basic_op("-",2,1))
test_mul = (basic_op("*",2,2))
test_div = (basic_op("/", 4,2))

print(test_sum)
print(test_sub)
print(test_mul)
print(test_div)