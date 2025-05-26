# Prosty Analizator Statystyk Opisowych z GUI

Ten program w Pythonie umożliwia wczytanie danych z pliku arkusza kalkulacyjnego (CSV lub Excel) i obliczenie podstawowych statystyk opisowych dla wybranej kolumny numerycznej. Program posiada prosty graficzny interfejs użytkownika (GUI)
## Funkcjonalności

*   **Wczytywanie plików**: Obsługa plików w formatach `.csv`, `.xlsx` oraz `.xls`.
*   **Wybór kolumny**: Umożliwia wybór kolumny numerycznej z wczytanego pliku, dla której mają zostać obliczone statystyki.
*   **Obliczanie statystyk**:
    *   Średnia arytmetyczna
    *   Mediana
    *   Odchylenie standardowe (próby)
    *   Rozstęp (różnica między wartością maksymalną a minimalną)
*   **Prosty interfejs GUI**: Intuicyjna obsługa dzięki graficznemu interfejsowi.
*   **Obsługa brakujących danych**: Wartości `NaN` (brakujące dane) w wybranej kolumnie są automatycznie usuwane przed obliczeniami.
*   **Informacje zwrotne**: Komunikaty o błędach (np. nieprawidłowy typ pliku, brak kolumn numerycznych) oraz o statusie operacji.

## Wymagania

*   Python 3.6+
*   Biblioteki Pythona:
    *   `pandas`
    *   `openpyxl` (do obsługi plików `.xlsx`)
    *   `tkinter` (zazwyczaj dołączany do standardowej instalacji Pythona)

