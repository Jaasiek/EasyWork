import xml.etree.ElementTree as ET

def today_talks_fcpxml(file, library_location, event_name, name):

    fcpxml_root_today_talks = ET.Element("fcpxml", version="1.10")
    resources_today_talks = ET.SubElement(fcpxml_root_today_talks, "resources")
    format_today_talks = ET.SubElement(
        resources_today_talks,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_today_talks = ET.SubElement(
    resources_today_talks,
    "asset",
    id="r2",
    name="WIPE_TALKS_TODAY_OUT",
    uid="C40D880BC4BB868817625D603581A7E7",
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
    media_rep_out_today_talks = ET.SubElement(
    asset_today_talks,
    "media-rep",
    kind="original-media",
    sig="C40D880BC4BB868817625D603581A7E7" ,
    src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TODAY/WIPE_TALKS_TODAY_OUT.mov"
)
    bookmark_out_today_talks = ET.SubElement(media_rep_out_today_talks, "bookmark")
    bookmark_out_today_talks.text = "Ym9va/ADAAAAAAQQMAAAABEGEiybB/CNJmdI3ojDFp6qhuI1vRxNKaiwWwRgQ07UBAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBUT0RBWQAAGAAAAAEBAABXSVBFX1RBTEtTX1RPREFZX09VVC5tb3YYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_out_today_talks = ET.SubElement(asset_today_talks, "metadata")
    md1_out_today_talks = ET.SubElement(
    metadata_out_today_talks,
    "md",
    key="com.apple.proapps.studio.rawToLogConversion",
    value="0",
)
    md2_out_today_talks = ET.SubElement(
    metadata_out_today_talks,
    "md",
    key="com.apple.proapps.spotlight.kMDItemProfileName",
    value="HD (1-1-1)",
)
    md3_out_today_talks = ET.SubElement(
    metadata_out_today_talks, "md", key="com.apple.proapps.studio.cameraISO", value="0"
)
    md4_out_today_talks = ET.SubElement(
    metadata_out_today_talks,
    "md",
    key="com.apple.proapps.studio.cameraColorTemperature",
    value="0",
)
    md5_out_today_talks = ET.SubElement(
    metadata_out_today_talks, "md", key="com.apple.proapps.spotlight.kMDItemCodecs"
)
    array_md5_out_today_talks = ET.SubElement(md5_out_today_talks, "array")
    string1_out_today_talks = ET.SubElement(array_md5_out_today_talks, "string")
    string1_out_today_talks.text = "Apple ProRes 4444"
    string2_out_today_talks = ET.SubElement(array_md5_out_today_talks, "string")
    string2_out_today_talks.text = "Linear PCM"
    md6_out_today_talks = ET.SubElement(
    asset_today_talks,
    "md",
    key="com.apple.proapps.mio.ingestDate",
    value="2024-03-13 14:34:08 +0100",
)
    asset_r3_today_talks = ET.SubElement(
    resources_today_talks,
    "asset",
    id="r3",
    name="WIPE_TALKS_TODAY_IN",
    uid="0B2F67CD44813E21A6EF76B8758376EC",
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
    media_rep_in_today_talks = ET.SubElement(
    asset_r3_today_talks,
    "media-rep",
    kind="original-media",
    sig="0B2F67CD44813E21A6EF76B8758376EC",
    src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TODAY/WIPE_TALKS_TODAY_IN.mov"
)
    bookmark_in_today_talks = ET.SubElement(media_rep_in_today_talks, "bookmark")
    bookmark_in_today_talks.text = "Ym9va/ADAAAAAAQQMAAAAJC7iP+7f9HY83UGkmOj63LAsx6bsyyFNRl5By6u9e48BAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAoAAAABAQAAV0lQRSBUT0RBWQAAFwAAAAEBAABXSVBFX1RBTEtTX1RPREFZX0lOLm1vdgAYAAAAAQYAABAAAAAgAAAAMAAAAEQAAABYAAAAbAAAAAgAAAAEAwAAMmMAAAAAAAAAAAAAAQoAABgAAAABBgAArAAAALwAAAC8AAAAvAAAALwAAAC8AAAAGAAAAAECAAABAAAAAAAAAA8AAAAAAAAAAAAAAAAAAAAAAAAAAQUAAAQAAAADAwAABwAAAAQAAAADAwAABAAAABkAAAABCQAAZmlsZTovLy9Wb2x1bWVzL1RWUFdPUkxELwAAAAgAAAAEAwAAAAAAAABkAAAYAAAAAQIAAAAAAAAAAAAA7xMAAAEAAAAAAAAAAAAAABEAAAABAQAAL1ZvbHVtZXMvVFZQV09STEQAAAAbAAAAAQkAAG5mczovLzEwLjE2LjIwLjIyMy9UVlBXT1JMRAAIAAAAAQkAAGZpbGU6Ly8vDAAAAAEBAABNYWNpbnRvc2ggSEQIAAAABAMAAACgIGh0AAAACAAAAAAEAABBxVGOmIAAACQAAAABAQAANzJFMTZENzQtRTgzNi00NjQwLTk2NkQtOTFFOEQwMzdENjFDGAAAAAECAACBAAAAAQAAAO8TAAABAAAAAAAAAAAAAAABAAAAAQEAAC8AAABgAAAA/v///wDwAAAAAAAABwAAAAIgAABIAgAAAAAAAAUgAAC4AQAAAAAAABAgAADIAQAAAAAAABEgAAD8AQAAAAAAABIgAADcAQAAAAAAABMgAADsAQAAAAAAACAgAAAoAgAAAAAAAAQAAAADAwAAAPAAAAQAAAADAwAAAAAAAAQAAAADAwAAAQAAABwAAAABBgAAvAIAAMgCAADUAgAAyAIAAMgCAADIAgAAyAIAALQAAAD+////AQAAAFQCAAAOAAAABBAAAIwAAAAAAAAABRAAAMQAAAAAAAAAEBAAAOQAAAAAAAAAVBAAAAwBAAAAAAAAVRAAABgBAAAAAAAAVhAAAAQBAAAAAAAAACAAAOACAAAAAAAAAiAAAHgBAAAAAAAABSAAACQBAAAAAAAAECAAACAAAAAAAAAAEiAAAEgBAAAAAAAAICAAAFgBAAAAAAAAUCAAAJQBAAAAAAAAENAAAAQAAAAAAAAA"
    metadata_in_today_talks = ET.SubElement(asset_r3_today_talks, "metadata")
    md1_in_today_talks = ET.SubElement(
    metadata_in_today_talks,
    "md",
    key="com.apple.proapps.studio.rawToLogConversion",
    value="0",
)
    md2_in_today_talks = ET.SubElement(
    metadata_in_today_talks,
    "md",
    key="com.apple.proapps.spotlight.kMDItemProfileName",
    value="HD (1-1-1)",
)
    md3_in_today_talks = ET.SubElement(
    metadata_in_today_talks, "md", key="com.apple.proapps.studio.cameraISO", value="0"
)
    md4_in_today_talks = ET.SubElement(
    metadata_in_today_talks,
    "md",
    key="com.apple.proapps.studio.cameraColorTemperature",
    value="0",
)
    md5_in_today_talks = ET.SubElement(
    metadata_in_today_talks, "md", key="com.apple.proapps.studio.cameraColorTemperature"
)
    array_md5_in_today_talks = ET.SubElement(md5_in_today_talks, "array")
    string1_in_today_talks = ET.SubElement(array_md5_in_today_talks, "string")
    string1_in_today_talks.text = "Apple ProRes 4444"
    string2_in_today_talks = ET.SubElement(md5_in_today_talks, "string")
    string2_in_today_talks.text = "Linear PCM"
    md6_in_today_talks = ET.SubElement(
    metadata_in_today_talks,
    "md",
    key="com.apple.proapps.mio.ingestDate",
    value="2024-03-13 14:34:08 + 0100",
)

    library_today_talks = ET.SubElement(
    fcpxml_root_today_talks, "library", location=f"{library_location}"
)
    event_today_talks = ET.SubElement(
    library_today_talks,
    "event",
    name=f"{event_name}",
    uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
)
    project_today_talks = ET.SubElement(
    event_today_talks,
    "project",
    name=f"{name}",
    uid="450CE2BF-FA9C-4375-BB18-9A945EB734BB",
    modDate="2024-04-06 20:14:03 +0200",
)
    sequence_today_talks = ET.SubElement(
    project_today_talks,
    "sequence",
    fomrat="r1",
    duration="17300/2500s",
    tcStart="0s",
    tcFormat="NDF",
    audioLayout="stereo",
    audioRate="48k",
)
    spine_today_talks = ET.SubElement(sequence_today_talks, "spine")
    gap1_today_talks = ET.SubElement(
    spine_today_talks,
    "gap",
    name="Gap",
    offset="0s",
    start="3600s",
    duration="9700/2500s",
)
    asset_clip1_today_talks = ET.SubElement(
    gap1_today_talks,
    "asset-clip",
    ref="r2",
    lane="1",
    offset="3600s",
    name="WIPE_TALKS_TODAY_OUT",
    duration="9700/2500s",
    tcFormat="NDF",
    audioRole="dialogue",
)
    keyword_asset_clip1_today_talks = ET.SubElement(
    asset_clip1_today_talks,
    "keyword",
    start="0s",
    duration="9700/2500s",
    value="wipe today",
)
    marker_asset_clip_today_talks = ET.SubElement(
    asset_clip1_today_talks,
    "marker",
    start="12/5s",
    duration="100/2500s",
    value="Marker 1",
)
    asset_clip2_today_talks = ET.SubElement(
    spine_today_talks,
    "asset-clip",
    ref="r3",
    offset="9700/2500s",
    name="WIPE_TALKS_TODAY_IN",
    duration="7600/2500s",
    tcFormat="NDF",
    audioRole="dialogue",
)
    keyword_asset_clip2_today_talks = ET.SubElement(
    asset_clip2_today_talks,
    "keyword",
    start="0s",
    duration="7600/2500s",
    value="wipe today",
)
    marker_asset_clip2_today_talks = ET.SubElement(
    asset_clip2_today_talks,
    "marker",
    start="11/25s",
    duration="100/2500s",
    value="Marker 1",
)
    smart_collection1_today_talks = ET.SubElement(
    library_today_talks, "smart-collection", name="Projects", match="all"
)
    match_clip_smart_collection1_today_talks = ET.SubElement(
    smart_collection1_today_talks, "match-clip", rule="is", type="project"
)
    smart_collection2_today_talks = ET.SubElement(
    library_today_talks, "smart-collection", name="All Video", match="any"
)
    match_media1_smart_collection2_today_talks = ET.SubElement(
    smart_collection2_today_talks, "match-media", rule="is", type="videoOnly"
)
    match_media2_smart_collection2_today_talks = ET.SubElement(
    smart_collection2_today_talks, "match-media", rule="is", type="videoWithAudio"
)
    smart_collection3_today_talks = ET.SubElement(
    library_today_talks, "smart-collection", name="Audio Only", match="all"
)
    match_media1_smart_collection3_today_talks = ET.SubElement(
    smart_collection3_today_talks, "match-media", rule="is", type="audioOnly"
)
    smart_collection4_today_talks = ET.SubElement(
    library_today_talks, "smart-collection", name="Stills", match="all"
)
    match_media1_smart_collection_4_today_talks = ET.SubElement(
    smart_collection4_today_talks, "match-media", rule="is", type="stills"
)
    smart_collection5_today_talks = ET.SubElement(
    library_today_talks, "smart-collection", name="Favourites", match="all"
)
    match_ratings1_smart_collection4_today_talks = ET.SubElement(
    smart_collection5_today_talks, "match-ratings", value="favourites"
)

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_today_talks, space="  ", level=1)

    fcpxml_string_today_talks = ET.tostring(fcpxml_root_today_talks, encoding="unicode")

    fcpxml_today_talks = header + fcpxml_string_today_talks

    file.write(fcpxml_today_talks)