import xml.etree.ElementTree as ET


def today_news_fcpxml(file, library_location, event_name, path):

    fcpxml_root_today_news = ET.Element("fcpxml", version="1.10")
    resources_today_news = ET.SubElement(fcpxml_root_today_news, "resources")
    format_today_news = ET.SubElement(
        resources_today_news,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_today_news = ET.SubElement(
        resources_today_news,
        "asset",
        id="r2",
        name="WIPE_NEWS_TODAY_OUT",
        uid="9AED8111D391EDFCCF856416EFF79CE8",
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
    media_rep_out_today_news = ET.SubElement(
        asset_today_news,
        "media-rep",
        kind="original-media",
        sig="9AED8111D391EDFCCF856416EFF79CE8",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TODAY/WIPE_NEWS_TODAY%20OUT.mov",
    )
    bookmark_out_today_news = ET.SubElement(media_rep_out_today_news, "bookmark")
    bookmark_out_today_news.text = "Ym9va/ADAAAAAAQQMAAAAFqdTp/jRHq5fXGmBynvblNpxOoulYmNRCHVWF46vW7IBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBUT0RBWQAAFwAAAAEBAABXSVBFX05FV1NfVE9EQVkgT1VULm1vdgAYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_out_today_news = ET.SubElement(asset_today_news, "metadata")
    md1_out_today_news = ET.SubElement(
        metadata_out_today_news,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_out_today_news = ET.SubElement(
        metadata_out_today_news,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_out_today_news = ET.SubElement(
        metadata_out_today_news,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_out_today_news = ET.SubElement(
        metadata_out_today_news,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_out_today_news = ET.SubElement(
        metadata_out_today_news, "md", key="com.apple.proapps.spotlight.kMDItemCodecs"
    )
    array_md5_out_today_news = ET.SubElement(md5_out_today_news, "array")
    string1_out_today_news = ET.SubElement(array_md5_out_today_news, "string")
    string1_out_today_news.text = "Apple ProRes 4444"
    string2_out_today_news = ET.SubElement(array_md5_out_today_news, "string")
    string2_out_today_news.text = "Linear PCM"
    md6_out_today_news = ET.SubElement(
        metadata_out_today_news,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 14:34:08 +0100",
    )
    asset_r3_today_news = ET.SubElement(
        resources_today_news,
        "asset",
        id="r3",
        name="WIPE_NEWS_TODAY_IN",
        uid="50A50BAFBBBBB9D248DC75120220FF61",
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
    media_rep_in_today_news = ET.SubElement(
        asset_r3_today_news,
        "media-rep",
        kind="original-media",
        sig="50A50BAFBBBBB9D248DC75120220FF61",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TODAY/WIPE_NEWS_TODAY_IN.mov",
    )
    bookmark_in_today_news = ET.SubElement(media_rep_in_today_news, "bookmark")
    bookmark_in_today_news.text = "Ym9va/ADAAAAAAQQMAAAACT9XI+64PTMibemu//V5J+/ghzCsjsxrkzcWv8FpKnJBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBUT0RBWQAAFgAAAAEBAABXSVBFX05FV1NfVE9EQVlfSU4ubW92AAAYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_in_today_news = ET.SubElement(asset_r3_today_news, "metadata")
    md1_in_today_news = ET.SubElement(
        metadata_in_today_news,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_in_today_news = ET.SubElement(
        metadata_in_today_news,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_in_today_news = ET.SubElement(
        metadata_in_today_news,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_in_today_news = ET.SubElement(
        metadata_in_today_news,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_in_today_news = ET.SubElement(
        metadata_in_today_news,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
    )
    array_md5_in_today_news = ET.SubElement(md5_in_today_news, "array")
    string1_in_today_news = ET.SubElement(array_md5_in_today_news, "string")
    string1_in_today_news.text = "Apple ProRes 4444"
    string2_in_today_news = ET.SubElement(md5_in_today_news, "string")
    string2_in_today_news.text = "Linear PCM"
    md6_in_today_news = ET.SubElement(
        metadata_in_today_news,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 14:34:08 + 0100",
    )

    library_today_news = ET.SubElement(
        fcpxml_root_today_news, "library", location=f"{library_location}"
    )
    event_today_news = ET.SubElement(
        library_today_news,
        "event",
        name=f"{event_name}",
        uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
    )
    project_today_news = ET.SubElement(
        event_today_news,
        "project",
        name=f"{file}",
        uid="40E11339-AFC0-40E1-8EDF-AB56E03875DB",
        modDate="2024-04-06 20:14:03 +0200",
    )
    sequence_today_news = ET.SubElement(
        project_today_news,
        "sequence",
        format="r1",
        duration="17300/2500s",
        tcStart="0s",
        tcFormat="NDF",
        audioLayout="stereo",
        audioRate="48k",
    )
    spine_today_news = ET.SubElement(sequence_today_news, "spine")
    gap1_today_news = ET.SubElement(
        spine_today_news,
        "gap",
        name="Gap",
        offset="0s",
        start="3600s",
        duration="9700/2500s",
    )
    asset_clip1_today_news = ET.SubElement(
        gap1_today_news,
        "asset-clip",
        ref="r2",
        lane="1",
        offset="3600s",
        name="WIPE_NEWS_TODAY_OUT",
        duration="9700/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip1_today_news = ET.SubElement(
        asset_clip1_today_news,
        "keyword",
        start="0s",
        duration="9700/2500s",
        value="wipe today",
    )
    marker_asset_clip_today_news = ET.SubElement(
        asset_clip1_today_news,
        "marker",
        start="12/5s",
        duration="100/2500s",
        value="Marker 1",
    )
    asset_clip2_today_news = ET.SubElement(
        spine_today_news,
        "asset-clip",
        ref="r3",
        offset="9700/2500s",
        name="WIPE_NEWS_TODAY_IN",
        duration="7600/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip2_today_news = ET.SubElement(
        asset_clip2_today_news,
        "keyword",
        start="0s",
        duration="7600/2500s",
        value="wipe today",
    )
    marker_asset_clip2_today_news = ET.SubElement(
        asset_clip2_today_news,
        "marker",
        start="11/25s",
        duration="100/2500s",
        value="Marker 1",
    )
    smart_collection1_today_news = ET.SubElement(
        library_today_news, "smart-collection", name="Projects", match="all"
    )
    match_clip_smart_collection1_today_news = ET.SubElement(
        smart_collection1_today_news, "match-clip", rule="is", type="project"
    )
    smart_collection2_today_news = ET.SubElement(
        library_today_news, "smart-collection", name="All Video", match="any"
    )
    match_media1_smart_collection2_today_news = ET.SubElement(
        smart_collection2_today_news, "match-media", rule="is", type="videoOnly"
    )
    match_media2_smart_collection2_today_news = ET.SubElement(
        smart_collection2_today_news, "match-media", rule="is", type="videoWithAudio"
    )
    smart_collection3_today_news = ET.SubElement(
        library_today_news, "smart-collection", name="Audio Only", match="all"
    )
    match_media1_smart_collection3_today_news = ET.SubElement(
        smart_collection3_today_news, "match-media", rule="is", type="audioOnly"
    )
    smart_collection4_today_news = ET.SubElement(
        library_today_news, "smart-collection", name="Stills", match="all"
    )
    match_media1_smart_collection_4_today_news = ET.SubElement(
        smart_collection4_today_news, "match-media", rule="is", type="stills"
    )
    smart_collection5_today_news = ET.SubElement(
        library_today_news, "smart-collection", name="Favorites", match="all"
    )
    match_ratings1_smart_collection4_today_news = ET.SubElement(
        smart_collection5_today_news, "match-ratings", value="favorites"
    )

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_today_news, space="  ", level=1)

    fcpxml_string_today_news = ET.tostring(fcpxml_root_today_news, encoding="unicode")

    fcpxml_today_news = header + fcpxml_string_today_news

    file_path = f"{path}/{file}.fcpxml"

    with open(file_path, "w") as handle:
        handle.write(fcpxml_today_news)


# Copyright ® 2024  Jasiek Gawlak
