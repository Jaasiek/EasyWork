import xml.etree.ElementTree as ET


def tonight_talks_fcpxml(file, library_location, event_name, path):

    fcpxml_root_tonight_talks = ET.Element("fcpxml", version="1.10")
    resources_tonight_talks = ET.SubElement(fcpxml_root_tonight_talks, "resources")
    format_tonight_talks = ET.SubElement(
        resources_tonight_talks,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_tonight_talks = ET.SubElement(
        resources_tonight_talks,
        "asset",
        id="r2",
        name="WIPE_TALKS_TONIGHT_OUT",
        uid="6F3CD735A398CE1BC6D683D0B0A116DD",
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
    media_rep_out_tonight_talks = ET.SubElement(
        asset_tonight_talks,
        "media-rep",
        kind="original-media",
        sig="6F3CD735A398CE1BC6D683D0B0A116DD",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TONIGHT/WIPE_TALKS_TONIGHT%20OUT.mov",
    )
    bookmark_out_tonight_talks = ET.SubElement(media_rep_out_tonight_talks, "bookmark")
    bookmark_out_tonight_talks.text = "Ym9va/QDAAAAAAQQMAAAAL48zVc1HvWyypmP9uOsrlywy9o8PoDIbyxwW5rDdWMXCAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAwAAAABAQAAV0lQRSBUT05JR0hUGgAAAAEBAABXSVBFX1RBTEtTX1RPTklHSFQgT1VULm1vdgAAGAAAAAEGAAAQAAAAIAAAADAAAABEAAAAWAAAAGwAAAAIAAAABAMAADJjAAAAAAAAAAAAAAEKAAAYAAAAAQYAALAAAADAAAAAwAAAAMAAAADAAAAAwAAAABgAAAABAgAAAQAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAAAAAAAEFAAAEAAAAAwMAAAcAAAAEAAAAAwMAAAQAAAAZAAAAAQkAAGZpbGU6Ly8vVm9sdW1lcy9UVlBXT1JMRC8AAAAIAAAABAMAAAAAAAAAZAAAGAAAAAECAAAAAAAAAAAAAO8TAAABAAAAAAAAAAAAAAARAAAAAQEAAC9Wb2x1bWVzL1RWUFdPUkxEAAAAGwAAAAEJAABuZnM6Ly8xMC4xNi4yMC4yMjMvVFZQV09STEQACAAAAAEJAABmaWxlOi8vLwwAAAABAQAATWFjaW50b3NoIEhECAAAAAQDAAAAoCBodAAAAAgAAAAABAAAQcVRjpiAAAAkAAAAAQEAADcyRTE2RDc0LUU4MzYtNDY0MC05NjZELTkxRThEMDM3RDYxQxgAAAABAgAAgQAAAAEAAADvEwAAAQAAAAAAAAAAAAAAAQAAAAEBAAAvAAAAYAAAAP7///8A8AAAAAAAAAcAAAACIAAATAIAAAAAAAAFIAAAvAEAAAAAAAAQIAAAzAEAAAAAAAARIAAAAAIAAAAAAAASIAAA4AEAAAAAAAATIAAA8AEAAAAAAAAgIAAALAIAAAAAAAAEAAAAAwMAAADwAAAEAAAAAwMAAAAAAAAEAAAAAwMAAAEAAAAcAAAAAQYAAMACAADMAgAA2AIAAMwCAADMAgAAzAIAAMwCAAC0AAAA/v///wEAAABYAgAADgAAAAQQAACQAAAAAAAAAAUQAADIAAAAAAAAABAQAADoAAAAAAAAAFQQAAAQAQAAAAAAAFUQAAAcAQAAAAAAAFYQAAAIAQAAAAAAAAAgAADkAgAAAAAAAAIgAAB8AQAAAAAAAAUgAAAoAQAAAAAAABAgAAAgAAAAAAAAABIgAABMAQAAAAAAACAgAABcAQAAAAAAAFAgAACYAQAAAAAAABDQAAAEAAAAAAAAAA=="
    metadata_out_tonight_talks = ET.SubElement(asset_tonight_talks, "metadata")
    md1_out_tonight_talks = ET.SubElement(
        metadata_out_tonight_talks,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_out_tonight_talks = ET.SubElement(
        metadata_out_tonight_talks,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_out_tonight_talks = ET.SubElement(
        metadata_out_tonight_talks,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_out_tonight_talks = ET.SubElement(
        metadata_out_tonight_talks,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_out_tonight_talks = ET.SubElement(
        metadata_out_tonight_talks,
        "md",
        key="com.apple.proapps.spotlight.kMDItemCodecs",
    )
    array_md5_out_tonight_talks = ET.SubElement(md5_out_tonight_talks, "array")
    string1_out_tonight_talks = ET.SubElement(array_md5_out_tonight_talks, "string")
    string1_out_tonight_talks.text = "Apple ProRes 4444"
    string2_out_tonight_talks = ET.SubElement(array_md5_out_tonight_talks, "string")
    string2_out_tonight_talks.text = "Linear PCM"
    md6_out_tonight_talks = ET.SubElement(
        asset_tonight_talks,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 16:29:08 +0100",
    )
    asset_r3_tonight_talks = ET.SubElement(
        resources_tonight_talks,
        "asset",
        id="r3",
        name="WIPE_TALKS_TONIGHT_IN",
        uid="E1ED3B8ADC84FD2CAC53038C85FC5783",
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
    media_rep_in_tonight_talks = ET.SubElement(
        asset_r3_tonight_talks,
        "media-rep",
        kind="original-media",
        sig="E1ED3B8ADC84FD2CAC53038C85FC5783",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TONIGHT/WIPE_TALKS_TONIGHT%20IN.mov",
    )
    bookmark_in_tonight_talks = ET.SubElement(media_rep_in_tonight_talks, "bookmark")
    bookmark_in_tonight_talks.text = "Ym9va/ADAAAAAAQQMAAAADkYFFcvwb8g2SNbuesdGrVsSOwNrXl90zbVcI711w9kBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAwAAAABAQAAV0lQRSBUT05JR0hUGAAAAAEBAABXSVBFX05FV1NfVE9OSUdIVCBJTi5tb3YYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_in_tonight_talks = ET.SubElement(asset_r3_tonight_talks, "metadata")
    md1_in_tonight_talks = ET.SubElement(
        metadata_in_tonight_talks,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_in_tonight_talks = ET.SubElement(
        metadata_in_tonight_talks,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_in_tonight_talks = ET.SubElement(
        metadata_in_tonight_talks,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_in_tonight_talks = ET.SubElement(
        metadata_in_tonight_talks,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_in_tonight_talks = ET.SubElement(
        metadata_in_tonight_talks,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
    )
    array_md5_in_tonight_talks = ET.SubElement(md5_in_tonight_talks, "array")
    string1_in_tonight_talks = ET.SubElement(array_md5_in_tonight_talks, "string")
    string1_in_tonight_talks.text = "Apple ProRes 4444"
    string2_in_tonight_talks = ET.SubElement(md5_in_tonight_talks, "string")
    string2_in_tonight_talks.text = "Linear PCM"
    md6_in_tonight_talks = ET.SubElement(
        metadata_in_tonight_talks,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 16:29:08 + 0100",
    )

    library_tonight_talks = ET.SubElement(
        fcpxml_root_tonight_talks, "library", location=f"{library_location}"
    )
    event_tonight_talks = ET.SubElement(
        library_tonight_talks,
        "event",
        name=f"{event_name}",
        uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
    )
    project_tonight_talks = ET.SubElement(
        event_tonight_talks,
        "project",
        name=f"{file}",
        uid="EC39FE75-C650-40F0-98A2-981E69E36490",
        modDate="2024-04-06 20:14:03 +0200",
    )
    sequence_tonight_talks = ET.SubElement(
        project_tonight_talks,
        "sequence",
        fomrat="r1",
        duration="17300/2500s",
        tcStart="0s",
        tcFormat="NDF",
        audioLayout="stereo",
        audioRate="48k",
    )
    spine_tonight_talks = ET.SubElement(sequence_tonight_talks, "spine")
    gap1_tonight_talks = ET.SubElement(
        spine_tonight_talks,
        "gap",
        name="Gap",
        offset="0s",
        start="3600s",
        duration="9700/2500s",
    )
    asset_clip1_tonight_talks = ET.SubElement(
        gap1_tonight_talks,
        "asset-clip",
        ref="r2",
        lane="1",
        offset="3600s",
        name="WIPE_TALKS_TONIGHT_OUT",
        duration="9700/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip1_tonight_talks = ET.SubElement(
        asset_clip1_tonight_talks,
        "keyword",
        start="0s",
        duration="9700/2500s",
        value="wipe tonight",
    )
    marker_asset_clip_tonight_talks = ET.SubElement(
        asset_clip1_tonight_talks,
        "marker",
        start="12/5s",
        duration="100/2500s",
        value="Marker 1",
    )
    asset_clip2_tonight_talks = ET.SubElement(
        spine_tonight_talks,
        "asset-clip",
        ref="r3",
        offset="9700/2500s",
        name="WIPE_TALKS_TONIGHT_IN",
        duration="7600/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip2_tonight_talks = ET.SubElement(
        asset_clip2_tonight_talks,
        "keyword",
        start="0s",
        duration="7600/2500s",
        value="wipe tonight",
    )
    marker_asset_clip2_tonight_talks = ET.SubElement(
        asset_clip2_tonight_talks,
        "marker",
        start="11/25s",
        duration="100/2500s",
        value="Marker 1",
    )
    smart_collection1_tonight_talks = ET.SubElement(
        library_tonight_talks, "smart-collection", name="Projects", match="all"
    )
    match_clip_smart_collection1_tonight_talks = ET.SubElement(
        smart_collection1_tonight_talks, "match-clip", rule="is", type="project"
    )
    smart_collection2_tonight_talks = ET.SubElement(
        library_tonight_talks, "smart-collection", name="All Video", match="any"
    )
    match_media1_smart_collection2_tonight_talks = ET.SubElement(
        smart_collection2_tonight_talks, "match-media", rule="is", type="videoOnly"
    )
    match_media2_smart_collection2_tonight_talks = ET.SubElement(
        smart_collection2_tonight_talks, "match-media", rule="is", type="videoWithAudio"
    )
    smart_collection3_tonight_talks = ET.SubElement(
        library_tonight_talks, "smart-collection", name="Audio Only", match="all"
    )
    match_media1_smart_collection3_tonight_talks = ET.SubElement(
        smart_collection3_tonight_talks, "match-media", rule="is", type="audioOnly"
    )
    smart_collection4_tonight_talks = ET.SubElement(
        library_tonight_talks, "smart-collection", name="Stills", match="all"
    )
    match_media1_smart_collection_4_tonight_talks = ET.SubElement(
        smart_collection4_tonight_talks, "match-media", rule="is", type="stills"
    )
    smart_collection5_tonight_talks = ET.SubElement(
        library_tonight_talks, "smart-collection", name="Favourites", match="all"
    )
    match_ratings1_smart_collection4_tonight_talks = ET.SubElement(
        smart_collection5_tonight_talks, "match-ratings", value="favourites"
    )

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_tonight_talks, space="  ", level=1)

    fcpxml_string_tonight_talks = ET.tostring(
        fcpxml_root_tonight_talks, encoding="unicode"
    )

    fcpxml_tonight_talks = header + fcpxml_string_tonight_talks

    file_path = f"{path}/{file}.fcpxml"

    with open(file_path, "w") as handle:
        handle.write(fcpxml_tonight_talks)

