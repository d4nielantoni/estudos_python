"""
Beginner Series #4 Cockroach

The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm
per second, rounded down to the integer (= floored).

For example:

1.08 --> 30
Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

1 km = 100000 cm
1 hora = 3600 segundos
entao 1 km/h para cm/s = 100000/ 3600
"""

def cockroach_speed(s):
    return int(s * 100000 / 3600)

print(cockroach_speed(1.08))
print(cockroach_speed(1.09))

