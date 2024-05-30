import xml.etree.ElementTree as ET


def today_trends_fcpxml(file, library_location, event_name, path):

    fcpxml_root_today_trends = ET.Element("fcpxml", version="1.10")
    resources_today_trends = ET.SubElement(fcpxml_root_today_trends, "resources")
    format_today_trends = ET.SubElement(
        resources_today_trends,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_today_trends = ET.SubElement(
        resources_today_trends,
        "asset",
        id="r2",
        name="WIPE_TRENDS_TODAY_OUT",
        uid="4B60F24AB5CD58373B95D7B7F5A0773B",
        start="0s",
        duration="9700/2500s",
        hasVideo="1",
        format="r1",
        hasAudio="1",
        videoSources="1",
        audioSources="1",
        audioChannels="2",
        audioRate="48000",
    )
    media_rep_out_today_trends = ET.SubElement(
        asset_today_trends,
        "media-rep",
        kind="original-media",
        sig="4B60F24AB5CD58373B95D7B7F5A0773B",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TODAY/WIPE_TRENDS_TODAY_OUT.mov",
    )
    bookmark_out_today_trends = ET.SubElement(media_rep_out_today_trends, "bookmark")
    bookmark_out_today_trends.text = "Ym9va/QDAAAAAAQQMAAAABtTLSf8PhdYScxq/d2SvUaiKwyGawojgXqN75Pl8Aw2CAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBUT0RBWQAAGQAAAAEBAABXSVBFX1RSRU5EU19UT0RBWV9PVVQubW92AAAAGAAAAAEGAAAQAAAAIAAAADAAAABEAAAAWAAAAGwAAAAIAAAABAMAADJjAAAAAAAAAAAAAAEKAAAYAAAAAQYAALAAAADAAAAAwAAAAMAAAADAAAAAwAAAABgAAAABAgAAAQAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAAAAAAAEFAAAEAAAAAwMAAAcAAAAEAAAAAwMAAAQAAAAZAAAAAQkAAGZpbGU6Ly8vVm9sdW1lcy9UVlBXT1JMRC8AAAAIAAAABAMAAAAAAAAAZAAAGAAAAAECAAAAAAAAAAAAAO8TAAABAAAAAAAAAAAAAAARAAAAAQEAAC9Wb2x1bWVzL1RWUFdPUkxEAAAAGwAAAAEJAABuZnM6Ly8xMC4xNi4yMC4yMjMvVFZQV09STEQACAAAAAEJAABmaWxlOi8vLwwAAAABAQAATWFjaW50b3NoIEhECAAAAAQDAAAAoCBodAAAAAgAAAAABAAAQcVRjpiAAAAkAAAAAQEAADcyRTE2RDc0LUU4MzYtNDY0MC05NjZELTkxRThEMDM3RDYxQxgAAAABAgAAgQAAAAEAAADvEwAAAQAAAAAAAAAAAAAAAQAAAAEBAAAvAAAAYAAAAP7///8A8AAAAAAAAAcAAAACIAAATAIAAAAAAAAFIAAAvAEAAAAAAAAQIAAAzAEAAAAAAAARIAAAAAIAAAAAAAASIAAA4AEAAAAAAAATIAAA8AEAAAAAAAAgIAAALAIAAAAAAAAEAAAAAwMAAADwAAAEAAAAAwMAAAAAAAAEAAAAAwMAAAEAAAAcAAAAAQYAAMACAADMAgAA2AIAAMwCAADMAgAAzAIAAMwCAAC0AAAA/v///wEAAABYAgAADgAAAAQQAACQAAAAAAAAAAUQAADIAAAAAAAAABAQAADoAAAAAAAAAFQQAAAQAQAAAAAAAFUQAAAcAQAAAAAAAFYQAAAIAQAAAAAAAAAgAADkAgAAAAAAAAIgAAB8AQAAAAAAAAUgAAAoAQAAAAAAABAgAAAgAAAAAAAAABIgAABMAQAAAAAAACAgAABcAQAAAAAAAFAgAACYAQAAAAAAABDQAAAEAAAAAAAAAA=="
    metadata_out_today_trends = ET.SubElement(asset_today_trends, "metadata")
    md1_out_today_trends = ET.SubElement(
        metadata_out_today_trends,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_out_today_trends = ET.SubElement(
        metadata_out_today_trends,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_out_today_trends = ET.SubElement(
        metadata_out_today_trends,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_out_today_trends = ET.SubElement(
        metadata_out_today_trends,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_out_today_trends = ET.SubElement(
        metadata_out_today_trends, "md", key="com.apple.proapps.spotlight.kMDItemCodecs"
    )
    array_md5_out_today_trends = ET.SubElement(md5_out_today_trends, "array")
    string1_out_today_trends = ET.SubElement(array_md5_out_today_trends, "string")
    string1_out_today_trends.text = "Apple ProRes 4444"
    string2_out_today_trends = ET.SubElement(array_md5_out_today_trends, "string")
    string2_out_today_trends.text = "Linear PCM"
    md6_out_today_trends = ET.SubElement(
        metadata_out_today_trends,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 14:34:08 +0100",
    )
    asset_r3_today_trends = ET.SubElement(
        resources_today_trends,
        "asset",
        id="r3",
        name="WIPE_TRENDS_TODAY_IN",
        uid="72C7BCA4BC32792E3E95F2355450EABA",
        start="0s",
        duration="7600/2500s",
        hasVideo="1",
        format="r1",
        hasAudio="1",
        videoSources="1",
        audioSources="1",
        audioChannels="2",
        audioRate="48000",
    )
    media_rep_in_today_trends = ET.SubElement(
        asset_r3_today_trends,
        "media-rep",
        kind="original-media",
        sig="72C7BCA4BC32792E3E95F2355450EABA",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TODAY/WIPE_TRENDS_TODAY_IN.mov",
    )
    bookmark_in_today_trends = ET.SubElement(media_rep_in_today_trends, "bookmark")
    bookmark_in_today_trends.text = "Ym9va/ADAAAAAAQQMAAAANTiTBZ7oBxRdKY6yGUpmUCJttxKQMammGLFKRmSCi1pBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBUT0RBWQAAGAAAAAEBAABXSVBFX1RSRU5EU19UT0RBWV9JTi5tb3YYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_in_today_trends = ET.SubElement(asset_r3_today_trends, "metadata")
    md1_in_today_trends = ET.SubElement(
        metadata_in_today_trends,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_in_today_trends = ET.SubElement(
        metadata_in_today_trends,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_in_today_trends = ET.SubElement(
        metadata_in_today_trends,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_in_today_trends = ET.SubElement(
        metadata_in_today_trends,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_in_today_trends = ET.SubElement(
        metadata_in_today_trends,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
    )
    array_md5_in_today_trends = ET.SubElement(md5_in_today_trends, "array")
    string1_in_today_trends = ET.SubElement(array_md5_in_today_trends, "string")
    string1_in_today_trends.text = "Apple ProRes 4444"
    string2_in_today_trends = ET.SubElement(array_md5_in_today_trends, "string")
    string2_in_today_trends.text = "Linear PCM"
    md6_in_today_trends = ET.SubElement(
        metadata_in_today_trends,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 14:34:08 + 0100",
    )

    library_today_trends = ET.SubElement(
        fcpxml_root_today_trends, "library", location=f"{library_location}"
    )
    event_today_trends = ET.SubElement(
        library_today_trends,
        "event",
        name=f"{event_name}",
        uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
    )
    project_today_trends = ET.SubElement(
        event_today_trends,
        "project",
        name=f"{file}",
        uid="AFA2E3C3-992A-4FC6-A416-137CAF1D8A27",
        modDate="2024-04-06 20:14:03 +0200",
    )
    sequence_today_trends = ET.SubElement(
        project_today_trends,
        "sequence",
        format="r1",
        duration="17300/2500s",
        tcStart="0s",
        tcFormat="NDF",
        audioLayout="stereo",
        audioRate="48k",
    )
    spine_today_trends = ET.SubElement(sequence_today_trends, "spine")
    gap1_today_trends = ET.SubElement(
        spine_today_trends,
        "gap",
        name="Gap",
        offset="0s",
        start="3600s",
        duration="9700/2500s",
    )
    asset_clip1_today_trends = ET.SubElement(
        gap1_today_trends,
        "asset-clip",
        ref="r2",
        lane="1",
        offset="3600s",
        name="WIPE_TRENDS_TODAY_OUT",
        duration="9700/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip1_today_trends = ET.SubElement(
        asset_clip1_today_trends,
        "keyword",
        start="0s",
        duration="9700/2500s",
        value="wipe today",
    )
    marker_asset_clip_today_trends = ET.SubElement(
        asset_clip1_today_trends,
        "marker",
        start="12/5s",
        duration="100/2500s",
        value="Marker 1",
    )
    asset_clip2_today_trends = ET.SubElement(
        spine_today_trends,
        "asset-clip",
        ref="r3",
        offset="9700/2500s",
        name="WIPE_TRENDS_TODAY_IN",
        duration="7600/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip2_today_trends = ET.SubElement(
        asset_clip2_today_trends,
        "keyword",
        start="0s",
        duration="7600/2500s",
        value="wipe today",
    )
    marker_asset_clip2_today_trends = ET.SubElement(
        asset_clip2_today_trends,
        "marker",
        start="11/25s",
        duration="100/2500s",
        value="Marker 1",
    )
    smart_collection1_today_trends = ET.SubElement(
        library_today_trends, "smart-collection", name="Projects", match="all"
    )
    match_clip_smart_collection1_today_trends = ET.SubElement(
        smart_collection1_today_trends, "match-clip", rule="is", type="project"
    )
    smart_collection2_today_trends = ET.SubElement(
        library_today_trends, "smart-collection", name="All Video", match="any"
    )
    match_media1_smart_collection2_today_trends = ET.SubElement(
        smart_collection2_today_trends, "match-media", rule="is", type="videoOnly"
    )
    match_media2_smart_collection2_today_trends = ET.SubElement(
        smart_collection2_today_trends, "match-media", rule="is", type="videoWithAudio"
    )
    smart_collection3_today_trends = ET.SubElement(
        library_today_trends, "smart-collection", name="Audio Only", match="all"
    )
    match_media1_smart_collection3_today_trends = ET.SubElement(
        smart_collection3_today_trends, "match-media", rule="is", type="audioOnly"
    )
    smart_collection4_today_trends = ET.SubElement(
        library_today_trends, "smart-collection", name="Stills", match="all"
    )
    match_media1_smart_collection_4_today_trends = ET.SubElement(
        smart_collection4_today_trends, "match-media", rule="is", type="stills"
    )
    smart_collection5_today_trends = ET.SubElement(
        library_today_trends, "smart-collection", name="Favorites", match="all"
    )
    match_ratings1_smart_collection4_today_trends = ET.SubElement(
        smart_collection5_today_trends, "match-ratings", value="favorites"
    )

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_today_trends, space="  ", level=1)

    fcpxml_string_today_trends = ET.tostring(
        fcpxml_root_today_trends, encoding="unicode"
    )

    fcpxml_today_trends = header + fcpxml_string_today_trends

    file_path = f"{path}/{file}.fcpxml"

    with open(file_path, "w") as handle:
        handle.write(fcpxml_today_trends)


# Copyright ® 2024  Jasiek Gawlak
