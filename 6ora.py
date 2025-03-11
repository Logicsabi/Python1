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