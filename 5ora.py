import random # olyan mint a c#-ban using
#Elől tesztelős ciklusok (while)

i = 0
while i < 10:
    print(i, end= " ")
    i += 2
print()

# feladat: Számoljuk meg egy szám, számjegyeit

num = 6948272659834
számjegy_számláló = 0
while num != 0:
    num //= 10
    számjegy_számláló += 1

print("Számjegyek száma:", számjegy_számláló)

# feladat: írjuk ki az első n db fibonacci számot!
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

n = 20
print(f"Fibonacci sorozat első {n} eleme:")
a = 1
b = 1
while n > 0:
    print(a, end = " ")
    c = a + b
    a = b
    b = c
    n -= 1
print()


# Melyik számra gondoltam?
num = random.randint(1, 100)
guessCount = 0
guess = 0
while guessCount <= 7 and guess != num:
    guess = int(input("Tippelj egy egész számot!\n"))
    if num > guess:
        print("Ettől nagyobb számra gondoltam.")
    elif num < guess:
        print("Ettől kisebb számra gondoltam.")
    guessCount += 1

if guess == num:
    print(f"Gratulálok! Sikeresen kitaláltad {guessCount} lépésből, hogy erre a számra gondoltam: {num}")
else:
    print(f"Ez most nem jött össze! Erre a számra gondoltam: {num}")

# 1. feladat: Írjunk egy programot ami, ezt írja ki:
"""
*
**
***
****
*****
******
*******
********   (8)
*******
******
*****
****
***
**
*
"""
# 2. feladat: Olvassunk be folyamatosan számokat, amiket összegezzünk, egész addig, amíg 0-t nem írunk be
#5, 3, 4, 6, 0 -> 18

