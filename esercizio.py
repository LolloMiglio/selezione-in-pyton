age = int(input("Inserisci la tua età: "))
if age < 14:
    cost = 10.0
else:
    if age > 65:
        cost = 15.0
    else:
        cost = 34.0

print("La tua tariffa è pari a", cost, "€.")
