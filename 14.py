# 1. feladat
n = int(input("Add meg a versenyzők számát: "))

# 2. feladat
nevek = []
pontok = []
for i in range(1, n + 1):
    nevek.append(input(f"{i}. vresenyző neve: "))
    pontok.append(input(f"{nevek[-1]} pontszáma: "))
print()

# 3. feladat
összeg = 0
for item in pontok:
    összeg += item
print("A pontszámok átlaga: ", round(összeg / n, 1))

# 4. feladat
maxi = 0
for i in range(1, n):
    if pontok[i] > pontok[maxi]:
        maxi = i
nyertes_indexek = []
for i in range(n):
    if pontok[i] == pontok[maxi]:
        nyertes_indexek.append(i)
print("A legnagyobb pontszámot elért versenyző(k): ")
for index in nyertes_indexek:
    print(f"{nevek[index]} - {pontok[index]} pont")

# 5. feladat
számláló = 0
for item in pontok:
    if item % 5 == 0:
        számláló += 1
print(f"{számláló} versenyző ért el kerek pontszámot.")

# 6. feladat
pontszam = int(input("Adj meg egy pontszámot és megkeresem, hogy kik azok akik ettől rosszabul teljesítettek: "))
for i in range(n):
    if pontok[i] < pontszam:
        print(f"{nevek[i]} - {pontok[i]} pont")