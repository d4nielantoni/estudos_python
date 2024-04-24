"""
String ends with?

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(text, ending):
    return text.endswith(ending)
#endswith função que retorna True or False, verifica se realmente a String termina com o parâmetro que passamos

print(solution('abc', 'bc'))
print(solution('abc', 'd'))
