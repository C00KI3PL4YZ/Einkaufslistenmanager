import psycopg2 

def hinzufuegen_artikel(liste, artikel):
    liste.append(artikel)


def remove_artikel(liste, artikelnr):
    liste.pop(int(artikelnr))


def anzeigen_artikel(liste):
    print(liste)


def speichern_liste(liste, dateiname):
    with open(dateiname, "w") as file:
        for artikel in liste:
            file.write(artikel + "\n")


def load_list(dateiname):
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


# def create_database_if_not_exists(dbadresse, db_port, db_name, db_user, db_pass, db_table):
#     conn = start_connection(dbadresse, db_port, "postgres", db_user, db_pass)
#     cursor = conn.cursor()

#     cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = '$db_name'")
#     exists = cursor.fetchone()
#     # if not exists:
#         # cursor.execute('CREATE DATABASE $db_name')
#     conn.close()
#     exists2 = create_table_if_not_exists(dbadresse, db_port, db_name, db_user, db_pass, db_table)
#     return exists and exists2

def create_table_if_not_exists(dbadresse, db_port, db_name, db_user, db_pass, db_table):
    conn = start_connection(dbadresse, db_port, db_name, db_user, db_pass)
    cursor = conn.cursor( )
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = %s
        );
    """, (db_table,))
    exists = cursor.fetchone()[0]
    if not exists:
        cursor.execute(f"""
            CREATE TABLE {db_table} (
                id SERIAL PRIMARY KEY,
                artikel TEXT NOT NULL
            );
        """)
    conn.close()
    return exists








def start_connection(db_adresse, db_port, db_name, db_user, db_pass):
    try:
        conn = psycopg2.connect(
            host=db_adresse,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        print("Verbindung erfolgreich")
        return conn

    except Exception as e:
        print("Fehler beim Verbindungsaufbau")
        print(e)
        return None



if __name__ == "__main__":
    checkdbconn = True
    main_liste = []
    dateiname = "file.csv"
    db_adresse = "localhost"
    db_port = "5432"
    db_name = "einkaufsliste"
    db_user = "postgres"
    db_pass = "postgres"
    db_table = "liste"
    # exists = create_database_if_not_exists(db_adresse, db_port, db_name, db_user, db_pass, db_table)
    # if exists:
        # print("Datenbank wurde erstellt")
    dbconn = start_connection(db_adresse, db_port, db_name, db_user, db_pass)
    saved = True
    # print("Ausgewählte Datei: " + dateiname)
    # main_liste = load_list(dateiname)
    if checkdbconn == True:
        print("Datenbankverbindung erfolgreich")
        exit()
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
            saved = False
            hinzufuegen_artikel(main_liste, artikel)
        elif auswahl == "2":
            for i in range(len(main_liste)):
                print(f"{i}: {main_liste[i]}")
            artikelnr = input("Artikel: ")
            saved = False
            remove_artikel(main_liste, artikelnr)
        elif auswahl == "3":
            anzeigen_artikel(main_liste)
        elif auswahl == "4":
            speichern_liste(main_liste, dateiname)
            saved = True
        elif auswahl == "5":
            main_liste = load_list(dateiname)
            saved = True
        elif auswahl == "6":
            print(main_liste)
            if not saved:
                speichern = input("Liste speichern? (J/n): ")
                if speichern == "j" or speichern == "J" or speichern == "":
                    speichern_liste(main_liste, dateiname)
            break
        else:
            print("Ungültige Eingabe")
