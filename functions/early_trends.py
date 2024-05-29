import xml.etree.ElementTree as ET


def early_trends_fcpxml(file, library_location, event_name, path):

    fcpxml_root_early_trends = ET.Element("fcpxml", version="1.10")
    resources_early_trends = ET.SubElement(fcpxml_root_early_trends, "resources")
    format_early_trends = ET.SubElement(
        resources_early_trends,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_early_trends = ET.SubElement(
        resources_early_trends,
        "asset",
        id="r2",
        name="WIPE_TRENDS_EARLY_OUT",
        uid="57494EE7AC68A260463DFFC2BF4ABA89",
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
    media_rep_out_early_trends = ET.SubElement(
        asset_early_trends,
        "media-rep",
        kind="original-media",
        sig="57494EE7AC68A260463DFFC2BF4ABA89",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20EARLY/WIPE_TRENDS_EARLY_OUT.mov",
    )
    bookmark_out_early_trends = ET.SubElement(media_rep_out_early_trends, "bookmark")
    bookmark_out_early_trends.text = "Ym9va/QDAAAAAAQQMAAAAB/UxvSlxVN9Yciy7CMS6iVURIumRCYRe+8F86m6o/gRCAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBFQVJMWQAAGQAAAAEBAABXSVBFX1RSRU5EU19FQVJMWV9PVVQubW92AAAAGAAAAAEGAAAQAAAAIAAAADAAAABEAAAAWAAAAGwAAAAIAAAABAMAADJjAAAAAAAAAAAAAAEKAAAYAAAAAQYAALAAAADAAAAAwAAAAMAAAADAAAAAwAAAABgAAAABAgAAAQAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAAAAAAAEFAAAEAAAAAwMAAAcAAAAEAAAAAwMAAAQAAAAZAAAAAQkAAGZpbGU6Ly8vVm9sdW1lcy9UVlBXT1JMRC8AAAAIAAAABAMAAAAAAAAAZAAAGAAAAAECAAAAAAAAAAAAAO8TAAABAAAAAAAAAAAAAAARAAAAAQEAAC9Wb2x1bWVzL1RWUFdPUkxEAAAAGwAAAAEJAABuZnM6Ly8xMC4xNi4yMC4yMjMvVFZQV09STEQACAAAAAEJAABmaWxlOi8vLwwAAAABAQAATWFjaW50b3NoIEhECAAAAAQDAAAAoCBodAAAAAgAAAAABAAAQcVRjpiAAAAkAAAAAQEAADcyRTE2RDc0LUU4MzYtNDY0MC05NjZELTkxRThEMDM3RDYxQxgAAAABAgAAgQAAAAEAAADvEwAAAQAAAAAAAAAAAAAAAQAAAAEBAAAvAAAAYAAAAP7///8A8AAAAAAAAAcAAAACIAAATAIAAAAAAAAFIAAAvAEAAAAAAAAQIAAAzAEAAAAAAAARIAAAAAIAAAAAAAASIAAA4AEAAAAAAAATIAAA8AEAAAAAAAAgIAAALAIAAAAAAAAEAAAAAwMAAADwAAAEAAAAAwMAAAAAAAAEAAAAAwMAAAEAAAAcAAAAAQYAAMACAADMAgAA2AIAAMwCAADMAgAAzAIAAMwCAAC0AAAA/v///wEAAABYAgAADgAAAAQQAACQAAAAAAAAAAUQAADIAAAAAAAAABAQAADoAAAAAAAAAFQQAAAQAQAAAAAAAFUQAAAcAQAAAAAAAFYQAAAIAQAAAAAAAAAgAADkAgAAAAAAAAIgAAB8AQAAAAAAAAUgAAAoAQAAAAAAABAgAAAgAAAAAAAAABIgAABMAQAAAAAAACAgAABcAQAAAAAAAFAgAACYAQAAAAAAABDQAAAEAAAAAAAAAA=="
    metadata_out_early_trends = ET.SubElement(asset_early_trends, "metadata")
    md1_out_early_trends = ET.SubElement(
        metadata_out_early_trends,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_out_early_trends = ET.SubElement(
        metadata_out_early_trends,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_out_early_trends = ET.SubElement(
        metadata_out_early_trends,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_out_early_trends = ET.SubElement(
        metadata_out_early_trends,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_out_early_trends = ET.SubElement(
        metadata_out_early_trends, "md", key="com.apple.proapps.spotlight.kMDItemCodecs"
    )
    array_md5_out_early_trends = ET.SubElement(md5_out_early_trends, "array")
    string1_out_early_trends = ET.SubElement(array_md5_out_early_trends, "string")
    string1_out_early_trends.text = "Apple ProRes 4444"
    string2_out_early_trends = ET.SubElement(array_md5_out_early_trends, "string")
    string2_out_early_trends.text = "Linear PCM"
    md6_out_early_trends = ET.SubElement(
        metadata_out_early_trends,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 20:20:41 +0100",
    )
    asset_r3_early_trends = ET.SubElement(
        resources_early_trends,
        "asset",
        id="r3",
        name="WIPE_TRENDS_EARLY_IN",
        uid="4811159BC844859946FEBEBBDA0441E2",
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
    media_rep_in_early_trends = ET.SubElement(
        asset_r3_early_trends,
        "media-rep",
        kind="original-media",
        sig="4811159BC844859946FEBEBBDA0441E2",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20EARLY/WIPE_TRENDS_EARLY_IN.mov",
    )
    bookmark_in_early_trends = ET.SubElement(media_rep_in_early_trends, "bookmark")
    bookmark_in_early_trends.text = "Ym9va/ADAAAAAAQQMAAAAIo5VGAyr7eHo5EfF3aPsGbZmqXfmv0CquFgKahRgCctBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBFQVJMWQAAGAAAAAEBAABXSVBFX1RSRU5EU19FQVJMWV9JTi5tb3YYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_in_early_trends = ET.SubElement(asset_r3_early_trends, "metadata")
    md1_in_early_trends = ET.SubElement(
        metadata_in_early_trends,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_in_early_trends = ET.SubElement(
        metadata_in_early_trends,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_in_early_trends = ET.SubElement(
        metadata_in_early_trends,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_in_early_trends = ET.SubElement(
        metadata_in_early_trends,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_in_early_trends = ET.SubElement(
        metadata_in_early_trends,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
    )
    array_md5_in_early_trends = ET.SubElement(md5_in_early_trends, "array")
    string1_in_early_trends = ET.SubElement(array_md5_in_early_trends, "string")
    string1_in_early_trends.text = "Apple ProRes 4444"
    string2_in_early_trends = ET.SubElement(md5_in_early_trends, "string")
    string2_in_early_trends.text = "Linear PCM"
    md6_in_early_trends = ET.SubElement(
        metadata_in_early_trends,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 20:20:41 + 0100",
    )

    library_early_trends = ET.SubElement(
        fcpxml_root_early_trends, "library", location=f"{library_location}"
    )
    event_early_trends = ET.SubElement(
        library_early_trends,
        "event",
        name=f"{event_name}",
        uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
    )
    project_early_trends = ET.SubElement(
        event_early_trends,
        "project",
        name=f"{file}",
        uid="2669DB4B-5924-4234-AB77-64EBA81ACB55",
        modDate="2024-04-06 20:14:03 +0200",
    )
    sequence_early_trends = ET.SubElement(
        project_early_trends,
        "sequence",
        format="r1",
        duration="17300/2500s",
        tcStart="0s",
        tcFormat="NDF",
        audioLayout="stereo",
        audioRate="48k",
    )
    spine_early_trends = ET.SubElement(sequence_early_trends, "spine")
    gap1_early_trends = ET.SubElement(
        spine_early_trends,
        "gap",
        name="Gap",
        offset="0s",
        start="3600s",
        duration="9700/2500s",
    )
    asset_clip1_early_trends = ET.SubElement(
        gap1_early_trends,
        "asset-clip",
        ref="r2",
        lane="1",
        offset="3600s",
        name="WIPE_TRENDS_EARLY_OUT",
        duration="9700/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip1_early_trends = ET.SubElement(
        asset_clip1_early_trends,
        "keyword",
        start="0s",
        duration="9700/2500s",
        value="wipe early",
    )
    marker_asset_clip_early_trends = ET.SubElement(
        asset_clip1_early_trends,
        "marker",
        start="12/5s",
        duration="100/2500s",
        value="Marker 1",
    )
    asset_clip2_early_trends = ET.SubElement(
        spine_early_trends,
        "asset-clip",
        ref="r3",
        offset="9700/2500s",
        name="WIPE_TRENDS_EARLY_IN",
        duration="7600/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip2_early_trends = ET.SubElement(
        asset_clip2_early_trends,
        "keyword",
        start="0s",
        duration="7600/2500s",
        value="wipe early",
    )
    marker_asset_clip2_early_trends = ET.SubElement(
        asset_clip2_early_trends,
        "marker",
        start="11/25s",
        duration="100/2500s",
        value="Marker 1",
    )
    smart_collection1_early_trends = ET.SubElement(
        library_early_trends, "smart-collection", name="Projects", match="all"
    )
    match_clip_smart_collection1_early_trends = ET.SubElement(
        smart_collection1_early_trends, "match-clip", rule="is", type="project"
    )
    smart_collection2_early_trends = ET.SubElement(
        library_early_trends, "smart-collection", name="All Video", match="any"
    )
    match_media1_smart_collection2_early_trends = ET.SubElement(
        smart_collection2_early_trends, "match-media", rule="is", type="videoOnly"
    )
    match_media2_smart_collection2_early_trends = ET.SubElement(
        smart_collection2_early_trends, "match-media", rule="is", type="videoWithAudio"
    )
    smart_collection3_early_trends = ET.SubElement(
        library_early_trends, "smart-collection", name="Audio Only", match="all"
    )
    match_media1_smart_collection3_early_trends = ET.SubElement(
        smart_collection3_early_trends, "match-media", rule="is", type="audioOnly"
    )
    smart_collection4_early_trends = ET.SubElement(
        library_early_trends, "smart-collection", name="Stills", match="all"
    )
    match_media1_smart_collection_4_early_trends = ET.SubElement(
        smart_collection4_early_trends, "match-media", rule="is", type="stills"
    )
    smart_collection5_early_trends = ET.SubElement(
        library_early_trends, "smart-collection", name="Favorites", match="all"
    )
    match_ratings1_smart_collection4_early_trends = ET.SubElement(
        smart_collection5_early_trends, "match-ratings", value="favorites"
    )

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_early_trends, space="  ", level=1)

    fcpxml_string_early_trends = ET.tostring(
        fcpxml_root_early_trends, encoding="unicode"
    )

    fcpxml_early_trends = header + fcpxml_string_early_trends
    file_path = f"{path}/{file}.fcpxml"
    with open(file_path, "w") as handle:
        handle.write(fcpxml_early_trends)

    # Copyright ® 2024  Jasiek Gawlak
