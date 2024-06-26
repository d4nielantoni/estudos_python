"""
Sentence Smash

Sentence Smash
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can
ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't
be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
"""


def smash(words):
    """
    string = ""
    for word in words:
        string += word + " "
    return string.strip() #usei o strip para tirar o espaçamento no final da frase :)

    """
    return " ".join(words) #ou podemos só usar essa linha de código


print(smash(['hello', 'world', 'this', 'is', 'great']))
