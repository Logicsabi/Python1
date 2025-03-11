"""
nevek = ["András", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc"]
print(nevek)
print(type(nevek))
print("A lista elemszáma:", len(nevek))

print(nevek[0])
print(nevek[3])
print(nevek[len(nevek) - 1])

print(nevek[-1])
print(nevek[-4])

print(nevek[2:5])

print(nevek[:4])

print(nevek[2:])

print(nevek[:])

nevek2 = nevek
print(nevek2)
print(nevek)

nevek = nevek[::-1]
print(nevek)

i = 0
while i < len(nevek):
    print(nevek[i], end= " ")
    i += 1
print()

for i in range(len(nevek)):
    print(nevek[i], end= " ")
print()

for item in nevek:
    print(item, end = " ")
print()

for index, item in enumerate(nevek):
    print(f"{index}: {item}", end= " ")
print()

for i in range (len(nevek)):
    print(i, end = " ")
print()

for i in range(5, 10):
    print(i, end = " ")
print()

for i in range(10, 100, 20):
    print(i, end = " ")
print()

for i in range(len(nevek) - 1, -1, -1):
    print(i, end = " ")
print()"""

"""
for i in range(1000):
    f = open(f"trash{i}.txt", "w")
    f.write(type(nevek)*10000)
    f.close()

    lista = []
    for i in range(10):
        lista.append(i)
    print(lista)"""

#1.
for i in range(0, 21):
    print(i, end = " ")
print()

#2.
for i in range(5, 16):
    print(i, end = " ")
print()

#3.
for i in range(15, 151, 15):
    print(i, end = " ")
print()

#4.
for i in range(80, 53, -1):
    print(i, end = " ")

#5.
lista = []
for i in range(1, 21):
    lista.append(i*i)
print(lista)

#6.
"""n = 20
print(f"Fibonacci sorozat első {n} eleme:")
a = 1
b = 1
while n > 0:
    print(a, end = " ")
    c = a + b
    a = b
    b = c
    n -= 1
print()"""

#vagy

lista = [1, 1]
while len(lista) < 20:
    lista.append(lista[-1] + lista[-2])
print(lista)

#7.
for i in range(1, 11):
    if i % 2 == 0:
        lista.append(-i)
    else:
        lista.append(i)
#8.
for i in range(1, 17):
    lista.append(i)
    lista.append(-i)

#9.
#az első 20 prímszám
    
#10.
#100-999 azok a számok amelyekben szerepel a 13 (132, 813)