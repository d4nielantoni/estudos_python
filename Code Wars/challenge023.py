"""
Mumbling

This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(s):
    result = ""
    for i, char in enumerate(s):
        result += char.upper() + char.lower() * i + "-"
    return result[:-1] #para remover o último hífen


print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))