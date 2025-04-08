#1.a
kg = int(input("Add meg hogy hány kilogramm\n"))
print(f"{kg} kg = {kg*1000} g")

#1.b
g = int(input("Add meg hogy hány gramm\n"))
print(f"{g} g = {g/1000} kg")

#2.a
F = int(input("Add meg hogy hány Fahrenheit a hőfok\n"))
print(f"{F} F = {F*1.8+32} C")

#2.b
C = int(input("Add meg hogy hány Celsius fok van\n"))
print(f"{C} C = {C/1.8-32} F")

#3.a
km = int(input("Add meg a távolságot km-be\n"))
print(f"{km} km = {km*0.62137} mile")

#3.b
mile = int(input("Add meg a távolságot mérföldbe\n"))
print(f"{mile} mile = {mile/0.62137} km")

#4
for i in range(1,76):
    if i :
        print("bim")
    elif "valami":
        print("bam")
    else:
        print("bimbam")