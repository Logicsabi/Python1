i = 1
while i <= 10:
    print(i, end = " ")
    i += 1
print()

lista = []
bemenet = "default"
bemenet = " "
while bemenet != "":
    bemenet = input("Add meg a lista következő elemét!")
    if bemenet != "":
        lista.append(bemenet)

print(lista)

for i in range(10):
    print(i, end= " ")
print()

for i in range(5, 15):
    print(i, end= " ")
print()

for i in range(2, 100, 10):
    print(i, end= " ")
print()

for i in range(100, 10, -10):
    print(i, end= " ")
print()

lista = ["Anna", "Beáta", "Cecil", "Dénes", "Elemér", "Ferenc"]
for item in lista:
    print(item, end = " ")
print()

for i in range(len(lista)):
    print(lista[i], end = " ")
print()

lista = [11, -4, 7, 1, 6, -5, -12, 0, 11, 14, -8, -9, 2, 23, 11, 10, -4, 0, 18, 4, 8, 1, 1, 11]
print(lista)
összeg = 0
for item in lista:
    összeg += item
print("A lista elemeinek az összege:", összeg)

"""2."""

lista = [11, -4, 7, 1, 6, -5, -12, 0, 11, 14, -8, -9, 2, 23, 11, 10, -4, 0, 18, 4, 8, 1, 1, 11]
print(lista)
min(lista)
for item in lista:
    min = item
print("A lista legkisebb eleme:")

lista = [11, -4, 7, 1, 6, -5, -12, 0, 11, 14, -8, -9, 2, 23, 11, 10, -4, 0, 18, 4, 8, 1, 1, 11]
print(lista)
összeg = 0
for item in lista:
    if item > 0:
        összeg += item
print("A lista pozitív elemeinek az összege:", összeg)

lista = [11, -4, 7, 1, 6, -5, -12, 0, 11, 14, -8, -9, 2, 23, 11, 10, -4, 0, 18, 4, 8, 1, 1, 11]
print(lista)
összeg = 0
for item in lista:
    if item < 0:
        összeg += item
print("A lista negatív elemeinek az összege:", összeg)

max_index = 0
for i in range(len(lista)):
    if lista[i] > lista[max_index]:
        max_index = i
print("A legnagyobb szám:", lista[max_index])

min_index = 0
for i in range(len(lista)):
    if lista[i] < lista[min_index]:
        min_index = i
print("A legkisebb szám:", lista[min_index])

számláló = 0
for item in lista:
    if item > 10:
        számláló += 1
print(számláló, "db 10-nél nagyobb szám van a listában")

print("A lista elemeinek az átlaga:", round(összeg/len(lista), 2))

pos_lista = []
neg_lista = []
for item in lista:
    if item < 0:
        neg_lista.append(item)
    if item > 0:
        pos_lista.append(item)
print("Pozitív számok:", pos_lista)
print("Negatív számok:", neg_lista)

for i in range(1, 11):
    for j in range(i):
        print(j+1, end = " ")
    print()

num = int(input("Adj meg egy egész számot!\n"))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
if prime:
    print("Ez egy prímszám")
else:
    print("Ez egy összetett szám")