import pandas as pd


lokalizacja_csv = input(
    "Podaj lokalizację pliku CSV (przeciągnąć plik do terminala) : "
)

lokalizacja_csv_bez_cudzysłowów = lokalizacja_csv.strip("'")

df = pd.read_csv(f"{lokalizacja_csv_bez_cudzysłowów}", sep=";")
df_clean = df.dropna()
godziny_emisji = df_clean["GODZINA_EMISJI"].values.tolist()
program = df_clean["PROGRAM"].values.tolist()
nazwa_plików = df_clean["NAZWA_PLIKU"].values.tolist()


print(program)

print(
    program[nazwa_plików.index("0604_World_News_Flash_2300_ZDP-3345782J")],
    godziny_emisji[nazwa_plików.index("0604_World_News_Flash_2300_ZDP-3345782J")],
)
