def get_sum(a,b):
    if a == b:
        return a

    elif a > b:
        a, b = b, a

    n = b - a + 1
    sum_integers = (n * (a + b)) // 2
    return sum_integers


result = get_sum(2,5) #14
print(result)
