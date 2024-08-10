"""
Filas = tem abordagem FIFO (First In First Out)

Inserir um novo elemento na fila inserimos na cauda (tail)
Retirar um elemento de uma fila tiramos da cabeça da fila (head)
Só lembrar do funcionamento de uma fila de banco

Filas com Deque: filas de duas pontas

"""

from collections import deque

fila = deque(['1','2','3','4','5','6','7','8','9'])

fila.append('10')
fila.popleft()
print(fila)