from datetime import datetime
import math


def convert_to_int(hour):
    if hour.endswith("+"):
        hour = hour[:-1]
    time_obj = datetime.strptime(hour, "%H:%M:%S.%f")
    int_representation = time_obj.hour * 10000 + time_obj.minute * 100 + time_obj.second
    return int_representation


def remove_elements(input_list):
    filtered_list = []
    for x in input_list:
        if (
            x != "___"
            and x != "__"
            and x != "_"
            and not (isinstance(x, float) and math.isnan(x))
        ):
            filtered_list.append(x)
    return filtered_list


# Copyright ® 2024  Jasiek Gawlak
