Statystyki Opisowe - Aplikacja GUI

Opis projektu
--------------
Aplikacja okienkowa stworzona w Pythonie przy użyciu biblioteki Tkinter, która umożliwia analizę danych z plików CSV i Excel poprzez obliczanie podstawowych statystyk opisowych.

Funkcjonalności
---------------
Obsługa plików:
- CSV (.csv)
- Excel (.xlsx, .xls)

Funkcje analityczne:
- Automatyczne wykrywanie kolumn numerycznych
- Średnia arytmetyczna
- Mediana
- Odchylenie standardowe
- Rozstęp

Inne:
- Intuicyjny interfejs użytkownika
- Wyniki prezentowane w czytelnej formie

Wymagane biblioteki
--------------------
- pandas
- tkinter (wbudowany w Pythona)
- openpyxl (dla plików Excel)

Instrukcja instalacji
----------------------
1. Sprawdź wersję Pythona (wymagana wersja 3.10+):
- py --version
2. Jeśli python jest zainstalowany przejdź do punktu 4, jeśli nie idź punkt 3.
3. Pobierz python ze strony:  https://www.python.org/downloads/. Przejdź punkt 1.
4. Zainstaluj wymagane biblioteki:
- py -m pip install pandas
- py -m pip install openpyxl
   
Instrukcja użycia
------------------
1. Uruchom program:
- cd Py-Project
- py dane.py -- Tworzenie tabeli excel, na której można tworzyć dane.
- py obliczenia.py -- Odpalenie programu liczącego
2. W aplikacji:
- Kliknij "Wczytaj plik" i wybierz plik .csv lub .xlsx/.xls
- Wybierz kolumnę z listy rozwijanej
- Kliknij "Oblicz Statystyki", aby zobaczyć wyniki

Uwagi
------------------
- Obsługiwane są tylko kolumny numeryczne
- Wartości niebędące liczbami są automatycznie pomijane
- Wyniki są zaokrąglane do dwóch miejsc po przecinku

Autorzy
------------------
- Rafał Jasiura
- Michał Zawartka
