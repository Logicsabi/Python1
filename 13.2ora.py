data = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2']

print("2.feladat")
km = 0
for szakasz in data:
    if szakasz[0] == "F":
        km += float(szakasz[1:])
    else:
        km += float(szakasz[2:])
print(f"A verseny távja {km} km volt.")