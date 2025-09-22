class Film:
    def __init__(self, tytul:str, rok_producji:int, gatunek:str):
        self.tytul = tytul
        self.rok_produkcji = rok_producji
        self.gatunek = gatunek
        self.liczba_odtworzen = 0

    def __str__(self):
        return f'{self.tytul} ({self.rok_produkcji})'
    
    def play(self, step = 1): #ta funkcja bedzie rowniez dostepna w klasie seriale poniewaz ona dziedziczy po filmach 
        self.liczba_odtworzen =+ step
        return self.liczba_odtworzen

class Serial(Film):
    def __init__(self, tytul:str, rok_produkcji:int, gatunek:str, numer_odcinka:int, numer_sezonu:int):
        super().__init__(tytul, rok_produkcji, gatunek)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
        self.liczba_odtworzen = 0

    def __str__(self):

        return f'{self.tytul} S({self.numer_odcinka:02}E{self.numer_sezonu:02}\ngatunek: {self.gatunek} rok produkcji: {self.rok_produkcji} liczba odtworzen {self.liczba_odtworzen}'
    
