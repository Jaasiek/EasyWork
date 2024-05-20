import pandas as pd
from datetime import datetime


lokalizacja_csv = input(
    "Podaj lokalizację pliku CSV (przeciągnąć plik do terminala) : "
)

lokalizacja_csv_bez_cudzysłowów = lokalizacja_csv.strip("'")

df = pd.read_csv(f"{lokalizacja_csv_bez_cudzysłowów}", sep=";")
df_clean = df.dropna()
godziny_emisji = df_clean["GODZINA_EMISJI"].values.tolist()
program = df_clean["PROGRAM"].values.tolist()
nazwa_plików = df_clean["NAZWA_PLIKU"].values.tolist()


# print(godziny_emisji)

# print(
#     program[nazwa_plików.index("0604_World_News_Flash_2300_ZDP-3345782J")],
#     godziny_emisji[nazwa_plików.index("0604_World_News_Flash_2300_ZDP-3345782J")],
# )


def convert_to_int(godzina):
    if godzina.endswith("+"):
        godzina = godzina[:-1]
    time_obj = datetime.strptime(godzina, "%H:%M:%S.%f")
    int_representation = time_obj.hour * 10000 + time_obj.minute * 100 + time_obj.second
    return int_representation


# Convert each time string to HHMMSS format as an integer
int_list = [convert_to_int(godzina) for godzina in godziny_emisji]

print(int_list)
