tematyka = ["today news", "early trends", "tonight talks", "early news"]

nazwy = ["1", "2", "3", "4"]

for nazwa in nazwy:
    if tematyka[nazwy.index(nazwa)] == "today news":
        print("Today news FCPXML")
    elif tematyka[nazwy.index(nazwa)] == "early news":
        print("Early news FCPXML")

    elif tematyka[nazwy.index(nazwa)] == "early trends":
        print("Early trends FCPXML")

    elif tematyka[nazwy.index(nazwa)] == "tonight talks":
        print("Tonight talks FCPXML")
