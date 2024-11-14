


def hinzufuegen_artikel(liste, artikel):
    liste.append(artikel)


def entfernen_artikel(liste, artikel):
    liste.remove(artikel)

def anzeigen_artikel(liste):
    print(liste)

def speichern_liste(liste, dateiname):
    with open(dateiname, "w") as file:
        for artikel in liste:
            file.write(artikel + "\n")

def laden_liste(dateiname):
    liste = []
    with open(dateiname, "r") as file:
        for line in file:
            




