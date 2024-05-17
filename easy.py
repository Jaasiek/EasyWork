import pandas as pd

biblioteka_fcpx = input(
    "\nPodaj ściężkę do swojej biblioteki FCPX (przeciągnij do terminala): "
)

biblioteka = biblioteka_fcpx.strip("'")

folder_docelowy = input(
    "\nPodaj ścieżkę do folderu, w którym chcesz zapisać nowe .fcpxml (przeciągnij folder do terminala): "
)
folder = folder_docelowy.strip("'")


lokalizacja_csv = input(
    "Podaj lokalizację pliku CSV (przeciągnąć plik do terminala) : "
)
event_name = input("Podaj nazwę eventu, do którego chcesz przypisać dane projekty: ")
lokalizacja_csv_bez_cudzysłowów = lokalizacja_csv.strip("'")
df = pd.read_csv(f"{lokalizacja_csv_bez_cudzysłowów}", sep=";")
df_clean = df.dropna()
nazwy_plików = df_clean["NAZWA_PLIKU"].values.tolist()

for nazwa in nazwy_plików:

    sciezka_do_pliku = f"{folder}/{nazwa}.fcpxml"

    with open(sciezka_do_pliku, "w") as plik:

        plik.write(
            f"""<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE fcpxml>
    <fcpxml version="1.10">
        <resources>
            <format id="r1" name="FFVideoFormat1080p25" frameDuration="100/2500s" width="1920" height="1080" colorSpace="1-1-1 (Rec. 709)"/>
        </resources>
        <library location="{biblioteka}">
            <event name="{event_name}" uid="DD5FD257-E7B0-456A-9F4B-DF501D3FA5CE">
                <project name="{nazwa}" uid="CC3C090D-2E7C-4608-A7BC-82FA58909ECB" modDate="2024-04-06 17:45:16 +0200">
                    <sequence format="r1" duration="0s" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
                        <spine/>
                    </sequence>
                </project>
            </event>
            <smart-collection name="Projects" match="all">
                <match-clip rule="is" type="project"/>
            </smart-collection>
            <smart-collection name="All Video" match="any">
                <match-media rule="is" type="videoOnly"/>
                <match-media rule="is" type="videoWithAudio"/>
            </smart-collection>
            <smart-collection name="Audio Only" match="all">
                <match-media rule="is" type="audioOnly"/>
            </smart-collection>
            <smart-collection name="Stills" match="all">
                <match-media rule="is" type="stills"/>
            </smart-collection>
            <smart-collection name="Favorites" match="all">
                <match-ratings value="favorites"/>
            </smart-collection>
        </library>
    </fcpxml>
    """
        )
print(
    f"\nUtworzono {len(nazwy_plików)} plików.fcpxml\nZostały utworzone w folderze: {folder} \nZ pliku {lokalizacja_csv_bez_cudzysłowów}\n"
)
print("Copyright ® 2024 Jasiek Gawlak")


# Copyright ® 2024  Jasiek Gawlak
