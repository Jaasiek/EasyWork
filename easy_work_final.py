import pandas as pd
from datetime import datetime
from early_news import early_news_fcpxml
from early_talks import early_talks_fcpxml
from early_trends import early_trends_fcpxml
from today_news import today_news_fcpxml
from today_talks import today_talks_fcpxml
from today_trends import today_trends_fcpxml
from tonight_news import tonight_news_fcpxml
from tonight_talks import tonight_talks_fcpxml
from tonight_trends import tonight_trends_fcpxml


def convert_to_int(hour):
    if hour.endswith("+"):
        hour = hour[:-1]
    time_obj = datetime.strptime(hour, "%H:%M:%S.%f")
    int_representation = time_obj.hour * 10000 + time_obj.minute * 100 + time_obj.second
    return int_representation

csv_path = input(
    "Podaj lokalizację pliku CSV (przeciągnąć plik do terminala) : "
)

csv_path = csv_path.strip("'")

df = pd.read_csv(f"{csv_path}", sep=";")
df_clean = df.dropna()
emmision_hours = df_clean["GODZINA_EMISJI"].values.tolist()
program_name = df_clean["PROGRAM"].values.tolist()
file_names = df_clean["NAZWA_PLIKU"].values.tolist()
hours_int = [convert_to_int(hour) for hour in emmision_hours]
 
