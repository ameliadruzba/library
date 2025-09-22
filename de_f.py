import random 
from c_lass import Film, Serial

film1 = Film("Incepcja", 2010, "Sci-Fi")
film2 = Film("Matrix", 1999, "Sci-Fi")

serial1 = Serial("Breaking Bad", 2008, "Crime", 1, 1)
serial2 = Serial("Sherlock", 2010, "Mystery", 1, 1)

zbior = [film1, film2, serial1, serial2]

def get_movies():
    filmy = []
    for item in zbior:
        if isinstance(item, Film) and not isinstance(item, Serial):
            filmy.append(item)
    posortowane = sorted(filmy, key = lambda x: x.tytul)
    for x,i in enumerate(posortowane, start=1):
        print(f"{x}. {i}")

def get_serial():
    seriale = []
    for item in zbior:
        if isinstance(item, Serial):
            seriale.append(item)
    posortowane = sorted(seriale, key = lambda x: x.tytul)
    for x,y in enumerate(posortowane, start=1):
        print(f"{x}. {y}")

def search():
    found = False
    pytanie = input('Podaj nazwe serialu lub filmu: ')
    for i in zbior:
        if i.tytul.lower() == pytanie.lower():
            found = True
            print(f'Znaleziono: {i}')
    if not found:
        print('Nie posiadamy takiego filmu w kolekcji')

def generate_views():
    losowa_liczba = random.randint(1, 100)
    element_zbioru = random.choice(zbior)
    element_zbioru.play(losowa_liczba)
    print (f'Do elementu {element_zbioru} dodano: {losowa_liczba} odtworzen')

def farming_views():
    for i in range(10):
        generate_views()

def top_tittle(zbior):
    ile_rzeczy = int(input('podaj ilosc: '))
    posortowane = sorted(zbior, key = lambda x: x.liczba_odtworzen, reverse=True)
    mini_zbior = posortowane[:ile_rzeczy]
    for l, i in enumerate(mini_zbior, start=1):
        print(f"{l}. {i.tytul}")

def add_serial():
    tytul = input('Podaj tytul: ')
    rok_produkcji = int(input('Podaj rok produkcji: '))
    gatunek = input('Podaj gatunek: ')
    numer_odcinka = int(input('Podaj numer odcinka: '))
    numer_sezonu = int(input('Podaj numer sezonu: '))
    zbior.append(Serial(tytul, rok_produkcji, gatunek, numer_odcinka, numer_sezonu))
    for i in zbior:
        return i

def odcinki():
    pytanie = input('Podaj tytul serialu, w ktorym chcesz sprawdzic ilosc odcinkow: ')
    liczbik = 0
    for i in zbior:
        if isinstance(i, Serial) and i.tytul.lower() == pytanie.lower():
            liczbik += 1
    print(f"liczba podanych odc to {liczbik}")