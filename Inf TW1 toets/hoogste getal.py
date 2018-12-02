aantal = int(input("Hoeveel cijfers wil je invullen? "))
cijfers = []


for i in range(aantal):
    cijfer = input("geef het cijfer")
    cijfers.append(cijfer)

print(cijfers[aantal-1], max(cijfers))
