import random 
from c_lass import Film, Serial

film1 = Film("Incepcja", 2010, "Sci-Fi")
film2 = Film("Matrix", 1999, "Sci-Fi")

serial1 = Serial("Breaking Bad", 2008, "Crime", 1, 1)
serial2 = Serial("Sherlock", 2010, "Mystery", 1, 1)

zbior = [film1, film2, serial1, serial2]

def get_movies():
    movies = []
    for item in zbior:
        if isinstance(item, Film) and not isinstance(item, Serial):
            movies.append(item)
    posortowane = sorted(movies, key = lambda x: x.tytul)
    for x,i in enumerate(posortowane, start=1):
        print(f"{x}. {i}")

def get_serial():
    serial = []
    for item in zbior:
        if isinstance(item, Serial):
            serial.append(item)
    posortowane = sorted(serial, key = lambda x: x.tytul)
    for x,y in enumerate(posortowane, start=1):
        print(f"{x}. {y}")

def search():
    found = False
    que = input('Podaj nazwe serialu lub filmu: ')
    for i in zbior:
        if i.tytul.lower() == que.lower():
            found = True
            print(f'Znaleziono: {i}')
    if not found:
        print('Nie posiadamy takiego filmu w kolekcji')

def generate_views():
    random_number = random.randint(1, 100)
    set_element = random.choice(zbior)
    set_element.play(random_number)
    print (f'Do elementu {set_element} dodano: {random_number} odtworzen')

def farming_views():
    for i in range(10):
        generate_views()

def top_tittle(zbior):
    how_many_items = int(input('podaj ilosc: '))
    posortowane = sorted(zbior, key = lambda x: x.liczba_odtworzen, reverse=True)
    mini_set = posortowane[:how_many_items]
    for l, i in enumerate(mini_set, start=1):
        print(f"{l}. {i.tytul}")

def add_serial():
    title = input('Podaj title: ')
    year_production = int(input('Podaj rok produkcji: '))
    typ = input('Podaj gatunek: ')
    episode = int(input('Podaj numer odcinka: '))
    sesons = int(input('Podaj numer sezonu: '))
    zbior.append(Serial(title, year_production, typ, episode, sesons))
    for i in zbior:
        return i

def odcinki():
    que = input('Podaj tytul serialu, w ktorym chcesz sprawdzic ilosc odcinkow: ')
    count = 0
    for i in zbior:
        if isinstance(i, Serial) and i.tytul.lower() == que.lower():
            count += 1
    print(f"liczba podanych odc to {count}")