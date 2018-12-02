aantal = int(input("Hoeveel cijfers wil je invullen? "))
cijfers = []


for i in range(aantal):
    cijfer = input("geef het cijfer")
    cijfers.append(cijfer)

print(cijfers[aantal-1])

hl = input("Wilt u het hoogste of laagste getal zien? h = hoogste, l = laagste")

if hl == "h":
    print(max(cijfers))
elif hl == "l":
    print(min(cijfers))
else:
    print("vul h of l in aub")
