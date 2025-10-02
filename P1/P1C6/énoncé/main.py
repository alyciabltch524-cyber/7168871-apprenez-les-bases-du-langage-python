# Écrivez votre code ici !
fruits = ["pomme" , "banane" , "orange" ]
fruits.append("kiwi")

print(f"dans ma liste de fruits il y a : {fruits}")

fruits.remove("orange")
print(f" a present il n y a que {fruits} dans ma liste de fruits")

fruits[1] = "ananas"
print(f"ma liste de fruits se compose de {fruits}")

print(f"la longueur de ma liste de fruits est de {len(fruits)}")

fruits.sort()
print(f"ma liste de fruits est composé de : {fruits} ")
