import csv

plik = 'kontakty.csv'

def dodaj_kontakt():
    imie = input("Imię: ")
    telefon = input("Telefon: ")
    with open(plik, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([imie, telefon])
    print("Kontakt zapisany.\n")

def pokaz_kontakty():
    print("\nLista kontaktów:")
    try:
        with open(plik, 'r') as f:
            reader = csv.reader(f)
            for wiersz in reader:
                print(f"{wiersz[0]} - {wiersz[1]}")
    except FileNotFoundError:
        print("Brak kontaktów.\n")

while True:
    print("1. Dodaj kontakt")
    print("2. Pokaż kontakty")
    print("3. Wyjście")
    wybor = input("Wybierz: ")

    if wybor == '1':
        dodaj_kontakt()
    elif wybor == '2':
        pokaz_kontakty()
    elif wybor == '3':
        break
    else:
        print("Nieprawidłowy wybór.\n")
