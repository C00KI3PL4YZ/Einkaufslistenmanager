import os
import curses

def list_directory(path="./"):
    files = []
    for file in os.listdir(path):
        if file.startswith("."):
            continue
        elif file.endswith(".csv"):
            files.append(file)
    return files

def hinzufuegen_artikel(liste, artikel):
    if artikel == "exit":
        return
    liste.append(artikel)

def entfernen_artikel(liste, artikel):
    if artikel == "exit":
        return
    liste.remove(artikel)

def anzeigen_artikel(liste):
    print(liste)

def speichern_liste(liste, dateiname):
    with open(dateiname, "w") as file:
        for artikel in liste:
            file.write(artikel + "\n")

def laden_liste(dateiname):
    liste = []
    lsdir = list_directory()
    if dateiname != "" and dateiname != None:
        with open(dateiname, "r") as file:
            for line in file:
                liste.append(line.strip()) 
        return liste
    else:
        if len(lsdir) >= 1:
            print("Dateien gefunden:")
            for idx, file in enumerate(lsdir):
                print(f"{idx}: {file}")
            auswahl = int(input("Auswahl: "))
            dateiname = lsdir[auswahl]
            main_liste = laden_liste(dateiname)
        else:
            print("Keine Dateien gefunden - Neue Datei wird erstellt")
            dateiname = input("Dateiname oder Pfad angeben: ")
            # check if file exists
            if os.path.isfile(dateiname):
                liste = laden_liste(dateiname)
            else:
                with open(dateiname, "w") as file:
                    pass
                liste = []
                return [dateiname, liste]

    

if __name__ == "__main__":
    main_liste = []
    dateiname = ""

    dateiname

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
            if main_liste != laden_liste(dateiname):
                print("Änderungen speichern?")
                speichern = input("Y/n: ")
                if speichern.lower == "y" or "":
                    speichern_liste(main_liste, dateiname)
                else:
                    print("Änderungen nicht gespeichert")
            break
        else:
            print("Ungültige Eingabe")
