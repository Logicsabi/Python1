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