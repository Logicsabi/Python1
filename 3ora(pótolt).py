pet_name = "Carlos"
pet_species = "Kutya"
pet_age = 5
pet_weight = 50
pet_spayed = False # Ivartalanított

print("Állat neve:", pet_name)
print("Fajtája: " + pet_species)
print("Életkora: " + str(pet_age))
print(f"Súlya: {pet_weight} kg")
if pet_spayed:
    print("Ivartalanított")
else:
    print("Ivaros")


    a = 12
    b = 34
    c = 22

    if a > b and a > c:
        print("Az a sz ám a legnagyobb.")
    elif b > a and b > c:
        print("A b szám a legnagyobb.")
    elif c > a and c > b:
        print("A c szám a legnagyobb.")
    else:
        print("Nincs egyértelműen legnagyobb szám ezek közül.")

points = int(input("Hány pontot értél el dolgozatnál?\n"))
if points > 90:
    print("5-ös")
elif points > 75:
    print("4-es")
elif points > 60:
    print("3-as")
elif points > 45:
    print("2-es")
else:
    print("1-es")