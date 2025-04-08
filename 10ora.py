import random

szamok = [4, 1, 3, 9, 2, 8, 2, 4, 6, 3, 1, 0, 2, 5, 3, 2]

seen = []
for item in szamok:
    if item not in seen:
        seen.append(item)
print(seen)

no_duplications = list(set(szamok))
print(no_duplications)

lista1 = [6,3,2,9,2,18,1]
lista2 = [8,4,2,1,2,6,8,8]
lista3 = [1,2,3,4,5,6]

for item in lista2:
    lista1.append(item)
print(lista1)

lista1.extend(lista3)
print(lista1)

lista = [4, 4.12, True, False, "cica", 5, 6.0, 8, [1,2,3], 9, 4.2321, 0]
integer_lista = []
for item in lista:
    if type(item) == int:
        integer_lista.append(item)
print(integer_lista)

