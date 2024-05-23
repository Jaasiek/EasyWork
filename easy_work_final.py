# Imports
import pandas as pd
from functions.helping_functions import convert_to_int, remove_elements
from functions.early_news import early_news_fcpxml
from functions.early_talks import early_talks_fcpxml
from functions.early_trends import early_trends_fcpxml
from functions.today_news import today_news_fcpxml
from functions.today_talks import today_talks_fcpxml
from functions.today_trends import today_trends_fcpxml
from functions.tonight_news import tonight_news_fcpxml
from functions.tonight_talks import tonight_talks_fcpxml
from functions.tonight_trends import tonight_trends_fcpxml

# Inputs
# fcpx_library = input(
# "\nPodaj ściężkę do swojej biblioteki FCPX (przeciągnij do terminala): "
# )
# fcpx_library = fcpx_library.strip("'")
csv_path = input("Podaj lokalizację pliku CSV (przeciągnąć plik do terminala): ")
csv_path = csv_path.strip("'")
# event_name = input("Podaj nazwę eventu, do którego chcesz przypisać dane projekty: ")

# CSV read and modification
df = pd.read_csv(f"{csv_path}", sep=";")
df_clean = df.dropna()
emmision_hours = remove_elements(df["GODZINA_EMISJI"].values.tolist())
program_name = remove_elements(df["PROGRAM"].values.tolist())
file_names = remove_elements(df["NAZWA_PLIKU"].values.tolist())
hours_int = [convert_to_int(hour) for hour in emmision_hours]
emmision_hours = emmision_hours = [convert_to_int(hour) for hour in emmision_hours]

print(emmision_hours, len(emmision_hours))
print(program_name, len(program_name))
print(file_names, len(file_names))

# Creating files


# Od 8 do 15 będziemy używać WIPE EARLY
# Od 15 do 20 WIPE TODAY
# Od 20 do 24 WIPE TONIGHT


for file in file_names:
    if 80000 <= emmision_hours[file_names.index(file)] < 150000:
        if "News" in program_name[file_names.index(file)]:
            pass
        if "Talks" in program_name[file_names.index(file)]:
            pass
        if "Trends" in program_name[file_names.index(file)]:
            pass
    elif 150000 <= emmision_hours[file_names.index(file)] < 200000:
        if "News" in program_name[file_names.index(file)]:
            pass
        if "Talks" in program_name[file_names.index(file)]:
            pass
        if "Trends" in program_name[file_names.index(file)]:
            pass
    elif 200000 <= emmision_hours[file_names.index(file)] < 240000:
        if "News" in program_name[file_names.index(file)]:
            pass
        if "Talks" in program_name[file_names.index(file)]:
            pass
        if "Trends" in program_name[file_names.index(file)]:
            pass
