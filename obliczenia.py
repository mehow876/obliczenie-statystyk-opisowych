import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

# Globalna zmienna do przechowywania DataFrame
df_global = None

def wczytaj_plik():
    """Otwiera dialog wyboru pliku i wczytuje dane do globalnego DataFrame."""
    global df_global
    filepath = filedialog.askopenfilename(
        title="Wybierz plik",
        filetypes=(("Pliki Excel", "*.xlsx *.xls"),
                   ("Pliki CSV", "*.csv"),
                   ("Wszystkie pliki", "*.*"))
    )
    if not filepath:
        return

    try:
        if filepath.endswith(('.xlsx', '.xls')):
            df_global = pd.read_excel(filepath)
        elif filepath.endswith('.csv'):
            df_global = pd.read_csv(filepath)
        else:
            messagebox.showerror("Błąd typu pliku", "Nieobsługiwany typ pliku. Wybierz .csv, .xlsx lub .xls.")
            return

        sciezka_pliku_label.config(text=f"Wczytano: {filepath.split('/')[-1]}")
        aktualizuj_liste_kolumn()
        wyczysc_wyniki()

    except Exception as e:
        messagebox.showerror("Błąd wczytywania", f"Nie można wczytać pliku:\n{e}")
        df_global = None
        sciezka_pliku_label.config(text="Nie wczytano pliku")
        aktualizuj_liste_kolumn() # Wyczyści listę kolumn
        wyczysc_wyniki()


def aktualizuj_liste_kolumn():
    """Aktualizuje listę rozwijaną z nazwami kolumn."""
    global df_global
    if df_global is not None:
        kolumny = [col for col in df_global.columns if pd.api.types.is_numeric_dtype(df_global[col])]
        if not kolumny:
            messagebox.showinfo("Brak kolumn numerycznych", "Wczytany plik nie zawiera kolumn numerycznych do analizy.")
            combobox_kolumny['values'] = []
            combobox_kolumny.set('')
        else:
            combobox_kolumny['values'] = kolumny
            if kolumny:
                combobox_kolumny.current(0) # Ustawia pierwszą numeryczną kolumnę jako domyślną
    else:
        combobox_kolumny['values'] = []
        combobox_kolumny.set('')

def wyczysc_wyniki():
    """Czyści etykiety z wynikami."""
    srednia_val.config(text="-")
    mediana_val.config(text="-")
    odch_std_val.config(text="-")
    rozstep_val.config(text="-")

def oblicz_statystyki():
    """Oblicza i wyświetla statystyki dla wybranej kolumny."""
    global df_global
    if df_global is None:
        messagebox.showwarning("Brak danych", "Najpierw wczytaj plik z danymi.")
        return

    wybrana_kolumna = combobox_kolumny.get()
    if not wybrana_kolumna:
        messagebox.showwarning("Brak kolumny", "Wybierz kolumnę do analizy.")
        return

    try:
        dane_kolumny = df_global[wybrana_kolumna].dropna() # Usuwamy wartości NaN

        if not pd.api.types.is_numeric_dtype(dane_kolumny):
            messagebox.showerror("Błąd typu danych", f"Kolumna '{wybrana_kolumna}' nie jest numeryczna.")
            wyczysc_wyniki()
            return

        if dane_kolumny.empty:
            messagebox.showinfo("Brak danych", f"Kolumna '{wybrana_kolumna}' nie zawiera danych liczbowych po usunięciu braków.")
            wyczysc_wyniki()
            return

        srednia = dane_kolumny.mean()
        mediana = dane_kolumny.median()
        odch_std = dane_kolumny.std()
        rozstep = dane_kolumny.max() - dane_kolumny.min()

        srednia_val.config(text=f"{srednia:.2f}")
        mediana_val.config(text=f"{mediana:.2f}")
        odch_std_val.config(text=f"{odch_std:.2f}")
        rozstep_val.config(text=f"{rozstep:.2f}")

    except KeyError:
        messagebox.showerror("Błąd kolumny", f"Nie znaleziono kolumny: {wybrana_kolumna}")
        wyczysc_wyniki()
    except Exception as e:
        messagebox.showerror("Błąd obliczeń", f"Wystąpił błąd podczas obliczeń:\n{e}")
        wyczysc_wyniki()

# --- Konfiguracja GUI ---
root = tk.Tk()
root.title("Analizator Statystyk Opisowych")
root.geometry("400x350") # Rozmiar okna

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#90ee90")
style.configure("TLabel", padding=3)
style.configure("TCombobox", padding=3)

# Ramka dla wczytywania pliku
frame_plik = ttk.Frame(root, padding="10")
frame_plik.pack(fill=tk.X)

przycisk_wczytaj = ttk.Button(frame_plik, text="Wczytaj plik (.csv, .xlsx)", command=wczytaj_plik)
przycisk_wczytaj.pack(side=tk.LEFT, padx=5)

sciezka_pliku_label = ttk.Label(frame_plik, text="Nie wczytano pliku", width=30, anchor="w")
sciezka_pliku_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Ramka dla wyboru kolumny
frame_kolumna = ttk.Frame(root, padding="10")
frame_kolumna.pack(fill=tk.X)

ttk.Label(frame_kolumna, text="Wybierz kolumnę numeryczną:").pack(side=tk.LEFT, padx=5)
combobox_kolumny = ttk.Combobox(frame_kolumna, state="readonly", width=25)
combobox_kolumny.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Przycisk obliczeń
przycisk_oblicz = ttk.Button(root, text="Oblicz Statystyki", command=oblicz_statystyki)
przycisk_oblicz.pack(pady=10)

# Ramka dla wyników
frame_wyniki = ttk.LabelFrame(root, text="Wyniki", padding="10")
frame_wyniki.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Etykiety wyników
ttk.Label(frame_wyniki, text="Średnia:").grid(row=0, column=0, sticky="w", pady=2)
srednia_val = ttk.Label(frame_wyniki, text="-", font=("Helvetica", 10, "bold"))
srednia_val.grid(row=0, column=1, sticky="w", pady=2)

ttk.Label(frame_wyniki, text="Mediana:").grid(row=1, column=0, sticky="w", pady=2)
mediana_val = ttk.Label(frame_wyniki, text="-", font=("Helvetica", 10, "bold"))
mediana_val.grid(row=1, column=1, sticky="w", pady=2)

ttk.Label(frame_wyniki, text="Odch. standardowe:").grid(row=2, column=0, sticky="w", pady=2)
odch_std_val = ttk.Label(frame_wyniki, text="-", font=("Helvetica", 10, "bold"))
odch_std_val.grid(row=2, column=1, sticky="w", pady=2)

ttk.Label(frame_wyniki, text="Rozstęp:").grid(row=3, column=0, sticky="w", pady=2)
rozstep_val = ttk.Label(frame_wyniki, text="-", font=("Helvetica", 10, "bold"))
rozstep_val.grid(row=3, column=1, sticky="w", pady=2)

# Uruchomienie pętli głównej GUI
root.mainloop()