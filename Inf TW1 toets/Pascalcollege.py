def Waardering(punten):
    if punten >= 34:
        print("waardering: goed ")
    elif punten < 34 and punten >= 28:
        print("waardering: voldoende ")
    elif punten <= 28 and punten >= 0:
        print("waardering: onvoldoende ")
    elif punten > 40:
        print("maximaal 40 punten invullen aub")
    elif punten < 0:
        print("Vul aub een positief getal in")

while 1:
    punten = input("Hoeveel punten zijn er behaald? ")
    try:
        punten = int(punten)
        Waardering(punten)
    except ValueError:
        print("vul een nummer in aub")
        pass

