from de_f import get_movies, get_serial, search, generate_views, farming_views, top_tittle, add_serial, odcinki, zbior

while True:
    question = int(input(f'Wybierz:\n1.Pokaz dostepne filmy\n2.Pokaz dostepne seriale\n'
        f'3.Wyszukaj serial/film\n4.Wygeneruj obserwacje\n5.Wygeneruj 10xwyswietlenia\n'
        f'6.Pokaz najpopularniejszy produkt\n7.Dodaj serial\n8.Sprawdz ilosc dostepnych odc\n9.koniec '))
    print()
    if question == 1:
        get_movies()
    elif question == 2:
        get_serial()
    elif question == 3:
        search()
    elif question == 4:
        generate_views()
    elif question == 5:
        farming_views()
    elif question == 6:
        top_tittle(zbior)
    elif question == 7:
        add_serial()
    elif question == 8:
        odcinki()
    elif question == 9:
        break