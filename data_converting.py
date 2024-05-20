from datetime import datetime

def convert_to_int(hour):
    if hour.endswith("+"):
        hour = hour[:-1]
    time_obj = datetime.strptime(hour, "%H:%M:%S.%f")
    int_representation = time_obj.hour * 10000 + time_obj.minute * 100 + time_obj.second
    return int_representation