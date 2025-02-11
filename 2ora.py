szöveg = "A fekete cica átsétált az úton, hogy megegye at ott találhati párizsit."
print(szöveg)
print("A szöveg hossza:", len(szöveg))

szöveg_szavanként = szöveg.split(" ")
print(szöveg_szavanként)

szöveg_azként = szöveg.split("az")
print(szöveg_azként)
első_n = szöveg.find("n")
print("Az 'n' karakter első előfordulásának helye:", első_n)

első_az = szöveg.find("az")
print("Az 'az' karakter első előfordulásának helye:", első_az)

print(szöveg_startswith("A"))
print(szöveg_startswith("x"))
print(szöveg_endswith("."))
print(szöveg_endswith("k"))

