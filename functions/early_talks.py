import xml.etree.ElementTree as ET


def early_talks_fcpxml(file, library_location, event_name, path):

    fcpxml_root_early_talks = ET.Element("fcpxml", version="1.10")
    resources_early_talks = ET.SubElement(fcpxml_root_early_talks, "resources")
    format_early_talks = ET.SubElement(
        resources_early_talks,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_early_talks = ET.SubElement(
        resources_early_talks,
        "asset",
        id="r2",
        name="WIPE_TALKS_EARLY_OUT",
        uid="1BC31B2C93AFC7606622005716489788",
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
    media_rep_out_early_talks = ET.SubElement(
        asset_early_talks,
        "media-rep",
        kind="original-media",
        sig="1BC31B2C93AFC7606622005716489788",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20EARLY/WIPE_TALKS_EARLY_OUT.mov",
    )
    bookmark_out_early_talks = ET.SubElement(media_rep_out_early_talks, "bookmark")
    bookmark_out_early_talks.text = "Ym9va/ADAAAAAAQQMAAAAMb/Xmr1+3qUgEE/rnZHzeIBG0L3eSqurdmkwzMElN4aBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBFQVJMWQAAGAAAAAEBAABXSVBFX1RBTEtTX0VBUkxZX09VVC5tb3YYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_out_early_talks = ET.SubElement(asset_early_talks, "metadata")
    md1_out_early_talks = ET.SubElement(
        metadata_out_early_talks,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_out_early_talks = ET.SubElement(
        metadata_out_early_talks,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_out_early_talks = ET.SubElement(
        metadata_out_early_talks,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_out_early_talks = ET.SubElement(
        metadata_out_early_talks,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_out_early_talks = ET.SubElement(
        metadata_out_early_talks, "md", key="com.apple.proapps.spotlight.kMDItemCodecs"
    )
    array_md5_out_early_talks = ET.SubElement(md5_out_early_talks, "array")
    string1_out_early_talks = ET.SubElement(array_md5_out_early_talks, "string")
    string1_out_early_talks.text = "Apple ProRes 4444"
    string2_out_early_talks = ET.SubElement(array_md5_out_early_talks, "string")
    string2_out_early_talks.text = "Linear PCM"
    md6_out_early_talks = ET.SubElement(
        asset_early_talks,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 20:20:41 +0100",
    )
    asset_r3_early_talks = ET.SubElement(
        resources_early_talks,
        "asset",
        id="r3",
        name="WIPE_TALKS_EARLY_IN",
        uid="0417E30A8F19A21E5AFF59BC0BB57AA2",
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
    media_rep_in_early_talks = ET.SubElement(
        asset_r3_early_talks,
        "media-rep",
        kind="original-media",
        sig="0417E30A8F19A21E5AFF59BC0BB57AA2",
        src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20EARLY/WIPE_TALKS_EARLY_IN.mov",
    )
    bookmark_in_early_talks = ET.SubElement(media_rep_in_early_talks, "bookmark")
    bookmark_in_early_talks.text = "Ym9va/ADAAAAAAQQMAAAAM1p4yehjJtjOaJcNT9q79q98K/GPAVAjjJXFmxIoHgyBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBFQVJMWQAAFwAAAAEBAABXSVBFX1RBTEtTX0VBUkxZX0lOLm1vdgAYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_in_early_talks = ET.SubElement(asset_r3_early_talks, "metadata")
    md1_in_early_talks = ET.SubElement(
        metadata_in_early_talks,
        "md",
        key="com.apple.proapps.studio.rawToLogConversion",
        value="0",
    )
    md2_in_early_talks = ET.SubElement(
        metadata_in_early_talks,
        "md",
        key="com.apple.proapps.spotlight.kMDItemProfileName",
        value="HD (1-1-1)",
    )
    md3_in_early_talks = ET.SubElement(
        metadata_in_early_talks,
        "md",
        key="com.apple.proapps.studio.cameraISO",
        value="0",
    )
    md4_in_early_talks = ET.SubElement(
        metadata_in_early_talks,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
        value="0",
    )
    md5_in_early_talks = ET.SubElement(
        metadata_in_early_talks,
        "md",
        key="com.apple.proapps.studio.cameraColorTemperature",
    )
    array_md5_in_early_talks = ET.SubElement(md5_in_early_talks, "array")
    string1_in_early_talks = ET.SubElement(array_md5_in_early_talks, "string")
    string1_in_early_talks.text = "Apple ProRes 4444"
    string2_in_early_talks = ET.SubElement(md5_in_early_talks, "string")
    string2_in_early_talks.text = "Linear PCM"
    md6_in_early_talks = ET.SubElement(
        metadata_in_early_talks,
        "md",
        key="com.apple.proapps.mio.ingestDate",
        value="2024-03-13 20:20:41 + 0100",
    )

    library_early_talks = ET.SubElement(
        fcpxml_root_early_talks, "library", location=f"{library_location}"
    )
    event_early_talks = ET.SubElement(
        library_early_talks,
        "event",
        name=f"{event_name}",
        uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
    )
    project_early_talks = ET.SubElement(
        event_early_talks,
        "project",
        name=f"{file}",
        uid="3FC36AED-8DF9-4638-8DE5-8785932D7A0A",
        modDate="2024-04-06 20:14:03 +0200",
    )
    sequence_early_talks = ET.SubElement(
        project_early_talks,
        "sequence",
        fomrat="r1",
        duration="17300/2500s",
        tcStart="0s",
        tcFormat="NDF",
        audioLayout="stereo",
        audioRate="48k",
    )
    spine_early_talks = ET.SubElement(sequence_early_talks, "spine")
    gap1_early_talks = ET.SubElement(
        spine_early_talks,
        "gap",
        name="Gap",
        offset="0s",
        start="3600s",
        duration="9700/2500s",
    )
    asset_clip1_early_talks = ET.SubElement(
        gap1_early_talks,
        "asset-clip",
        ref="r2",
        lane="1",
        offset="3600s",
        name="WIPE_TALKS_EARLY_OUT",
        duration="9700/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip1_early_talks = ET.SubElement(
        asset_clip1_early_talks,
        "keyword",
        start="0s",
        duration="9700/2500s",
        value="wipe early",
    )
    marker_asset_clip_early_talks = ET.SubElement(
        asset_clip1_early_talks,
        "marker",
        start="12/5s",
        duration="100/2500s",
        value="Marker 1",
    )
    asset_clip2_early_talks = ET.SubElement(
        spine_early_talks,
        "asset-clip",
        ref="r3",
        offset="9700/2500s",
        name="WIPE_TALKS_EARLY_IN",
        duration="7600/2500s",
        tcFormat="NDF",
        audioRole="dialogue",
    )
    keyword_asset_clip2_early_talks = ET.SubElement(
        asset_clip2_early_talks,
        "keyword",
        start="0s",
        duration="7600/2500s",
        value="wipe early",
    )
    marker_asset_clip2_early_talks = ET.SubElement(
        asset_clip2_early_talks,
        "marker",
        start="11/25s",
        duration="100/2500s",
        value="Marker 1",
    )
    smart_collection1_early_talks = ET.SubElement(
        library_early_talks, "smart-collection", name="Projects", match="all"
    )
    match_clip_smart_collection1_early_talks = ET.SubElement(
        smart_collection1_early_talks, "match-clip", rule="is", type="project"
    )
    smart_collection2_early_talks = ET.SubElement(
        library_early_talks, "smart-collection", name="All Video", match="any"
    )
    match_media1_smart_collection2_early_talks = ET.SubElement(
        smart_collection2_early_talks, "match-media", rule="is", type="videoOnly"
    )
    match_media2_smart_collection2_early_talks = ET.SubElement(
        smart_collection2_early_talks, "match-media", rule="is", type="videoWithAudio"
    )
    smart_collection3_early_talks = ET.SubElement(
        library_early_talks, "smart-collection", name="Audio Only", match="all"
    )
    match_media1_smart_collection3_early_talks = ET.SubElement(
        smart_collection3_early_talks, "match-media", rule="is", type="audioOnly"
    )
    smart_collection4_early_talks = ET.SubElement(
        library_early_talks, "smart-collection", name="Stills", match="all"
    )
    match_media1_smart_collection_4_early_talks = ET.SubElement(
        smart_collection4_early_talks, "match-media", rule="is", type="stills"
    )
    smart_collection5_early_talks = ET.SubElement(
        library_early_talks, "smart-collection", name="Favourites", match="all"
    )
    match_ratings1_smart_collection4_early_talks = ET.SubElement(
        smart_collection5_early_talks, "match-ratings", value="favourites"
    )

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_early_talks, space="  ", level=1)

    fcpxml_string_early_talks = ET.tostring(fcpxml_root_early_talks, encoding="unicode")

    fcpxml_early_talks = header + fcpxml_string_early_talks

    file_path = f"{path}/{file}.fcpxml"

    with open(file_path, "w") as handle:
        handle.write(fcpxml_early_talks)


# Copyright ® 2024  Jasiek Gawlak
