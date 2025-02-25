szöveg = "A fekete cica átsétált az úton, hogy megegye az ott találhati párizsit."
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

print(szöveg.startswith("A"))
print(szöveg.startswith("x"))
print(szöveg.endswith("."))
print(szöveg.endswith("k"))

szó = "kUtYa"
print(szó)
print(szó.capitalize()) # Kutya
print(szó.lower())      # kutya
print(szó.upper())      # KUTYA

print("a cica története".title()) # Minden szót nagybetűvel kezd

print(szöveg.lower().count("a"))



thing_1 = input("Type an object:\n")
thing_2 = input("Type another object:\n")
adjective = input("Give me an adjective:\n")
song_name = input("Give me the name of a song:\n")
celebrity = input("Give me a celebrity name:\n")
feeling = input("Give me a feeling:\n")
verb = input("Give me a verb:\n")
place = input("Give me a place:\n")
food = input("Give me a food item:\n")
person = input("Give me a person/name:\n")

print(f"""
    I just got back from a pizza party with {person}.
    Can you believe we got to eat {adjective} pizza in {place}?!
    Everyone got to choose their own toppings.
    I made '{food} and {thing_1}' pizza, which is my favorite!
    They even stuffed the crust with {thing_2}. How {feeling}!
    If that wasn't good enough already, {celebrity} was there singing {song_name}.
    I was so inspired by the music, I had to get up out of my seat and {verb}.
    """)