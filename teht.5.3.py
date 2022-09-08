#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

luku = int(input("Kirjoita luku "))

if luku % 1 == 0 and luku % luku == 0:
    print("Luku on alkuluku")

else:
    print("Luku ei ole alkuluku")
