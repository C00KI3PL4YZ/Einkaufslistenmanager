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
            liste.append(line.strip())
    return liste

def load_list_database(dbconn):
    cursor = dbconn.cursor()
    cursor.execute("SELECT * FROM liste")
    liste = cursor.fetchall()
    return liste

if __name__ == "__main__":
    main_liste = []
    dateiname = "file.csv"
    print("Ausgewählte Datei: " + dateiname)
    main_liste = laden_liste(dateiname)
    while True:
        print("1: Artikel hinzufügen")
        print("2: Artikel entfernen")
        print("3: Artikel anzeigen")
        print("4: Liste speichern")
        print("5: Liste laden")
        print("6: Beenden")
        auswahl = input("Auswahl: ")
        if auswahl == "1":
            artikel = input("Artikel: ")
            hinzufuegen_artikel(main_liste, artikel)
        elif auswahl == "2":
            artikel = input("Artikel: ")
            entfernen_artikel(main_liste, artikel)
        elif auswahl == "3":
            anzeigen_artikel(main_liste)
        elif auswahl == "4":
            speichern_liste(main_liste, dateiname)
        elif auswahl == "5":
            main_liste = laden_liste(dateiname)
        elif auswahl == "6":
            print(main_liste)
            break
        else:
            print("Ungültige Eingabe")
