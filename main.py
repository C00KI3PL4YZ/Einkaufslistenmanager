import os
import pydoc

def list_directory(path="./"):
    files = []
    for file in os.listdir(path):
        if file.startswith("."):
            continue
        elif file.endswith(".csv"):
            files.append(file)
    return files

def hinzufuegen_artikel(liste):
    clear_screen()
    artikel = input("Neuen Artikel zur Einkaufsliste hinzufügen: ")
    if artikel == "exit":
        return
    liste.append(artikel)

def entfernen_artikel(liste):
    print("Artikel zum entfernen: ")
    for idx, artikel in enumerate(liste):
        print(f"{idx}: {artikel}")
    auswahl = input("Nummer angeben: ")
    if auswahl == "exit":
        return
    try:
        idx = int(auswahl)
    except ValueError:
        print("Ungültige Eingabe")
        return
    try:
        artikel = liste[idx]
    except IndexError:
        print("Ungültige Eingabe")
        return
    liste.remove(artikel)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def anzeigen_artikel(liste):
    clear_screen()
    pydoc.pager("\n".join(liste))
    # for artikel in liste:
        # print(artikel)
    # print("\n\n")

def speichern_liste(liste, dateiname):
    with open(dateiname, "w") as file:
        for artikel in liste:
            file.write(artikel + "\n")

def laden_liste(dateiname):
    liste = []
    if dateiname != "" and dateiname != None:
        with open(dateiname, "r") as file:
            for line in file:
                liste.append(line.strip()) 
        return dateiname, liste
    else:
        lsdir = list_directory()
        if len(lsdir) >= 1:
            print("Dateien gefunden:")
            for idx, file in enumerate(lsdir):
                print(f"{idx}: {file}")
            auswahl = input("Dateipfad angeben oder Nummer auswählen: ")
            if auswahl.isdigit():
                dateiname = lsdir[int(auswahl)]
            else:
                dateiname = auswahl
            dateiname, liste =  laden_liste(dateiname)
            return dateiname, liste
        else:
            print("Keine Datei im aktuellen Verzeichnis gefunden - kompletten Pfad angeben oder Namen einer neuen Datei")
            dateiname = input("Dateiname oder Pfad angeben: ")
            # check if file exists
            dateiname, liste = datapath(dateiname)
            return dateiname, liste

def datapath(dateiname):

    if os.path.isfile(dateiname):
        liste = laden_liste(dateiname)
    else:
        with open(dateiname, "w") as file:
            pass
        liste = []
        return dateiname, liste


    

if __name__ == "__main__":
    main_liste = []
    dateiname = ""

    clear_screen()
    dateiname, main_liste = laden_liste(dateiname)
    print("Dateiname: " + dateiname)
    print(main_liste)

    clear_screen()
    while True:
        print("0: Artikel hinzufügen")
        print("1: Artikel entfernen")
        print("2: Artikel anzeigen")
        print("3: Liste speichern")
        print("4: Liste laden")
        print("5: Beenden")
        auswahl = input("Auswahl: ")
        if auswahl == "0":
            hinzufuegen_artikel(main_liste)
        elif auswahl == "1":
            entfernen_artikel(main_liste)
        elif auswahl == "2":
            anzeigen_artikel(main_liste)
        elif auswahl == "3":
            speichern_liste(main_liste, dateiname)
        elif auswahl == "4":
            main_liste = laden_liste(dateiname)
        elif auswahl == "5":
            print(main_liste)
            if main_liste != laden_liste(dateiname):
                print("Änderungen speichern?")
                speichern = input("Y/n: ")
                if speichern == "y" or speichern == "" or speichern == "Y":
                    speichern_liste(main_liste, dateiname)
                else:
                    print("Änderungen nicht gespeichert")
            break
        else:
            print("Ungültige Eingabe")
