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

