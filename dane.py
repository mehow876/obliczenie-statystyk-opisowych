import pandas as pd

# Dane testowe
dane = {
    'Imię': ['Anna', 'Bartek', 'Celina', 'Dawid', 'Eliza'],
    'Wiek': [23, 21, 25, 22, 24],
    'Wynik Testu': [78.5, 82.0, 69.0, 91.0, 85.0],
    'Ocena': [4.0, 4.5, 3.5, 5.0, 4.5]
}

# Tworzenie DataFrame
df = pd.DataFrame(dane)

# Zapis do pliku Excel
df.to_excel("test_dane.xlsx", index=False)

print("Plik test_dane.xlsx został zapisany.")
