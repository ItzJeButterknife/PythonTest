import random
kansen = 3

print("Je krijgt drie kansen om het getal te raden")
naam = input("wat is uw naam? ")
lijst = random.randrange(1,20)
print(lijst)

while kansen > 0:
    raad = int(input("wat is het getal"))
    if raad == lijst:
        print("gefeliciteerd ", naam, " je hebt gewonnen")
    else:
        kansen -= 1
else:
    print("helaas ", naam, " je hebt verloren.")


