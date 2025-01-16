import os
import pydoc
import time


def list_directory(path="./"):
    files = []
    for root, dirs, filenames in os.walk(path):
        for file in filenames:
            if file.startswith("."):
                continue
            elif file.endswith(".csv"):
                files.append(os.path.join(root, file))
    return files

def hinzufuegen_artikel(liste):
    clear_screen()
    artikel = input(
        "Neuen Artikel zur Einkaufsliste hinzufügen (mehrere Artikel mit ',' oder ';' trennen): \n"
    )
    if artikel == "exit":
        return
    delimiter = "," if "," in artikel else ";" if ";" in artikel else None
    if delimiter:
        artikel_list = [art.strip() for art in artikel.split(delimiter)]
        for art in artikel_list:
            if art not in liste:
                liste.append(art)
            else:
                print(f"Artikel '{art}' bereits auf der Liste")
    else:
        if artikel in liste:
            print("\nArtikel bereits auf der Liste\n")
            wait = input("Weiter mit Enter")
            clear_screen()
        else:
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
                dateiname, liste = datapath(dateiname)
            else:
                dateiname = auswahl
                dateiname, liste = datapath(dateiname)
            return dateiname, liste
        else:
            print(
                "Keine Datei im aktuellen Verzeichnis gefunden"
            )
            dateiname = input("Pfad oder Namen einer neuen Datei angeben: ")
            # check if file exists
            dateiname, liste = datapath(dateiname)
            return dateiname, liste


def datapath(dateiname):

    if os.path.isfile(dateiname):
        dateiname, liste = laden_liste(dateiname)
    else:
        print(dateiname)
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
    time.sleep(2)


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
            dateiname = ""
            dateiname, main_liste = laden_liste(dateiname)
            clear_screen()
            print("Ausgewählte Datei: " + dateiname + "\n")
        elif auswahl == "5":
            print("")
            if main_liste != laden_liste(dateiname)[1]:
                print("Änderungen speichern?")
                speichern = input("Y/n: ")
                if (
                    speichern == ""
                    or speichern == "y"
                    or speichern == "Y"
                    or speichern == "yes"
                    or speichern == "Yes"
                    or speichern == "YES"
                    or speichern == "ja"
                    or speichern == "Ja"
                ):
                    speichern_liste(main_liste, dateiname)
                    break
                elif speichern == "back" or speichern == "exit" or speichern == "cancel":
                    continue
                elif (
                    speichern == "n"
                    or speichern == "N"
                    or speichern == "no"
                    or speichern == "No"
                    or speichern == "NO"
                    or speichern == "nein"
                    or speichern == "Nein"
                ):
                    print("Änderungen nicht gespeichert")
                    break
            else:
                break   
        else:
            print("Ungültige Eingabe")
