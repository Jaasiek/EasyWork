import xml.etree.ElementTree as ET


def deafult_fcpxml(file, library_location, event_name, path):
    fcpxml_root_deafult = ET.Element("fcpxml", version="1.10")
    resources_deafult = ET.SubElement(fcpxml_root_deafult, "resources")
    format_deafult = ET.SubElement(
        resources_deafult,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1 (Rec. 709)",
    )
    library_location_deafult = ET.SubElement(
        fcpxml_root_deafult, "library", location=f"{library_location}"
    )
    event_name_deafult = ET.SubElement(
        library_location_deafult,
        "event",
        name=f"{event_name}",
        uid="DD5FD257-E7B0-456A-9F4B-DF501D3FA5CE",
    )
    project_name_deafult = ET.SubElement(
        event_name_deafult,
        "project",
        name=f"{file}",
        uid="CC3C090D-2E7C-4608-A7BC-82FA58909ECB",
        modDate="2024-04-06 17:45:16 +0200",
    )
    sequence_deafult = ET.SubElement(
        project_name_deafult,
        "sequence",
        format="r1",
        duration="0s",
        tcStart="0s",
        tcFormat="NDF",
        audioLayout="stereo",
        audioRate="48k",
    )
    spine_deafult = ET.SubElement(sequence_deafult, "spine")
    smart_1_deafult = ET.SubElement(
        library_location_deafult, "smart-collection", name="Projects", match="all"
    )
    match1_clip_1_deafult = ET.SubElement(
        smart_1_deafult, "match-clip", rule="is", type="projects"
    )
    smart_2_deafult = ET.SubElement(
        library_location_deafult, "smart-collection", name="All Video", match="any"
    )
    match1_clip_2_deafult = ET.SubElement(
        smart_2_deafult, "match-media", rule="is", type="videoOnly"
    )
    match2_clip_2_deafult = ET.SubElement(
        smart_2_deafult, "match-media", rule="is", type="videoWithAudio"
    )
    smart_3_deafult = ET.SubElement(
        library_location_deafult, "smart-collection", name="Audio Only", match="all"
    )
    match1_clip_3_deafult = ET.SubElement(
        smart_3_deafult, "match-media", rule="is", type="audioOnly"
    )
    smart_4_deafult = ET.SubElement(
        library_location_deafult, "smart-collection", name="Stills", match="all"
    )
    match1_clip_4_deafult = ET.SubElement(
        smart_4_deafult, "match-media", rule="is", type="stills"
    )
    smart_5_deafult = ET.SubElement(
        library_location_deafult, "smart-collection", name="Favorites", match="all"
    )
    match1_ratings_deafult = ET.SubElement(
        smart_5_deafult, "match-ratings", value="favorites"
    )

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_deafult, space="  ", level=1)

    fcpxml_string_deafult = ET.tostring(fcpxml_root_deafult, encoding="unicode")

    fcpxml_deafult = header + fcpxml_string_deafult

    file_path = f"{path}/{file}.fcpxml"

    with open(file_path, "w") as handle:
        handle.write(fcpxml_deafult)


# Copyright ® 2024  Jasiek Gawlak
