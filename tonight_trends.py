import xml.etree.ElementTree as ET

def tonight_trends_fcpxml(file):
    library_location = "library location"
    event_name = "event_name"
    name = "project name"

    fcpxml_root_tonight_trends = ET.Element("fcpxml", version="1.10")
    resources_tonight_trends = ET.SubElement(fcpxml_root_tonight_trends, "resources")
    format_tonight_trends = ET.SubElement(
        resources_tonight_trends,
        "format",
        id="r1",
        name="FFVideoFormat1080p25",
        frameDuration="100/2500s",
        width="1920",
        height="1080",
        colorSpace="1-1-1(Rec. 709)",
    )
    asset_tonight_trends = ET.SubElement(
    resources_tonight_trends,
    "asset",
    id="r2",
    name="WIPE_TRENDS_TONIGHT_OUT",
    uid="489BA03DD6D5EE9666D0C96907350B12",
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
    media_rep_out_tonight_trends = ET.SubElement(
    asset_tonight_trends,
    "media-rep",
    kind="original-media",
    sig="489BA03DD6D5EE9666D0C96907350B12" ,
    src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TONIGHT/WIPE_TRENDS_TONIGHT_OUT.mov"
)
    bookmark_out_tonight_trends = ET.SubElement(media_rep_out_tonight_trends, "bookmark")
    bookmark_out_tonight_trends.text = "Ym9va/QDAAAAAAQQMAAAAL48zVc1HvWyypmP9uOsrlywy9o8PoDIbyxwW5rDdWMXCAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAwAAAABAQAAV0lQRSBUT05JR0hUGgAAAAEBAABXSVBFX1RBTEtTX1RPTklHSFQgT1VULm1vdgAAGAAAAAEGAAAQAAAAIAAAADAAAABEAAAAWAAAAGwAAAAIAAAABAMAADJjAAAAAAAAAAAAAAEKAAAYAAAAAQYAALAAAADAAAAAwAAAAMAAAADAAAAAwAAAABgAAAABAgAAAQAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAAAAAAAEFAAAEAAAAAwMAAAcAAAAEAAAAAwMAAAQAAAAZAAAAAQkAAGZpbGU6Ly8vVm9sdW1lcy9UVlBXT1JMRC8AAAAIAAAABAMAAAAAAAAAZAAAGAAAAAECAAAAAAAAAAAAAO8TAAABAAAAAAAAAAAAAAARAAAAAQEAAC9Wb2x1bWVzL1RWUFdPUkxEAAAAGwAAAAEJAABuZnM6Ly8xMC4xNi4yMC4yMjMvVFZQV09STEQACAAAAAEJAABmaWxlOi8vLwwAAAABAQAATWFjaW50b3NoIEhECAAAAAQDAAAAoCBodAAAAAgAAAAABAAAQcVRjpiAAAAkAAAAAQEAADcyRTE2RDc0LUU4MzYtNDY0MC05NjZELTkxRThEMDM3RDYxQxgAAAABAgAAgQAAAAEAAADvEwAAAQAAAAAAAAAAAAAAAQAAAAEBAAAvAAAAYAAAAP7///8A8AAAAAAAAAcAAAACIAAATAIAAAAAAAAFIAAAvAEAAAAAAAAQIAAAzAEAAAAAAAARIAAAAAIAAAAAAAASIAAA4AEAAAAAAAATIAAA8AEAAAAAAAAgIAAALAIAAAAAAAAEAAAAAwMAAADwAAAEAAAAAwMAAAAAAAAEAAAAAwMAAAEAAAAcAAAAAQYAAMACAADMAgAA2AIAAMwCAADMAgAAzAIAAMwCAAC0AAAA/v///wEAAABYAgAADgAAAAQQAACQAAAAAAAAAAUQAADIAAAAAAAAABAQAADoAAAAAAAAAFQQAAAQAQAAAAAAAFUQAAAcAQAAAAAAAFYQAAAIAQAAAAAAAAAgAADkAgAAAAAAAAIgAAB8AQAAAAAAAAUgAAAoAQAAAAAAABAgAAAgAAAAAAAAABIgAABMAQAAAAAAACAgAABcAQAAAAAAAFAgAACYAQAAAAAAABDQAAAEAAAAAAAAAA=="
    metadata_out_tonight_trends = ET.SubElement(asset_tonight_trends, "metadata")
    md1_out_tonight_trends = ET.SubElement(
    metadata_out_tonight_trends,
    "md",
    key="com.apple.proapps.studio.rawToLogConversion",
    value="0",
)
    md2_out_tonight_trends = ET.SubElement(
    metadata_out_tonight_trends,
    "md",
    key="com.apple.proapps.spotlight.kMDItemProfileName",
    value="HD (1-1-1)",
)
    md3_out_tonight_trends = ET.SubElement(
    metadata_out_tonight_trends, "md", key="com.apple.proapps.studio.cameraISO", value="0"
)
    md4_out_tonight_trends = ET.SubElement(
    metadata_out_tonight_trends,
    "md",
    key="com.apple.proapps.studio.cameraColorTemperature",
    value="0",
)
    md5_out_tonight_trends = ET.SubElement(
    metadata_out_tonight_trends, "md", key="com.apple.proapps.spotlight.kMDItemCodecs"
)
    array_md5_out_tonight_trends = ET.SubElement(md5_out_tonight_trends, "array")
    string1_out_tonight_trends = ET.SubElement(array_md5_out_tonight_trends, "string")
    string1_out_tonight_trends.text = "Apple ProRes 4444"
    string2_out_tonight_trends = ET.SubElement(array_md5_out_tonight_trends, "string")
    string2_out_tonight_trends.text = "Linear PCM"
    md6_out_tonight_trends = ET.SubElement(
    asset_tonight_trends,
    "md",
    key="com.apple.proapps.mio.ingestDate",
    value="2024-03-13 16:29:08 +0100",
)
    asset_r3_tonight_trends = ET.SubElement(
    resources_tonight_trends,
    "asset",
    id="r3",
    name="WIPE_TRENDS_TONIGHT_IN",
    uid="93E33E2258312E2F6F3FDFF65A58B785",
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
    media_rep_in_tonight_trends = ET.SubElement(
    asset_r3_tonight_trends,
    "media-rep",
    kind="original-media",
    sig="93E33E2258312E2F6F3FDFF65A58B785",
    src="file:///Volumes/TVPWORLD/OPRAWA%202024/OPRAWA%20NEWS/WIPE%20TONIGHT/WIPE_TRENDS_TONIGHT_IN.mov"
)
    bookmark_in_tonight_trends = ET.SubElement(media_rep_in_tonight_trends, "bookmark")
    bookmark_in_tonight_trends.text = "Ym9va/QDAAAAAAQQMAAAAKO8tJ2M0yEHq7GaThdCXv/r1RFXrv9qyKjEC9wPtmVACAMAAAQAAAADAwAAABgAKAcAAAABAQAAVm9sdW1lcwAIAAAAAQEAAFRWUFdPUkxECwAAAAEBAABPUFJBV0EgMjAyNAALAAAAAQEAAE9QUkFXQSBORVdTAAwAAAABAQAAV0lQRSBUT05JR0hUGgAAAAEBAABXSVBFX1RSRU5EU19UT05JR0hUX0lOLm1vdgAAGAAAAAEGAAAQAAAAIAAAADAAAABEAAAAWAAAAGwAAAAIAAAABAMAADJjAAAAAAAAAAAAAAEKAAAYAAAAAQYAALAAAADAAAAAwAAAAMAAAADAAAAAwAAAABgAAAABAgAAAQAAAAAAAAAPAAAAAAAAAAAAAAAAAAAAAAAAAAEFAAAEAAAAAwMAAAcAAAAEAAAAAwMAAAQAAAAZAAAAAQkAAGZpbGU6Ly8vVm9sdW1lcy9UVlBXT1JMRC8AAAAIAAAABAMAAAAAAAAAZAAAGAAAAAECAAAAAAAAAAAAAO8TAAABAAAAAAAAAAAAAAARAAAAAQEAAC9Wb2x1bWVzL1RWUFdPUkxEAAAAGwAAAAEJAABuZnM6Ly8xMC4xNi4yMC4yMjMvVFZQV09STEQACAAAAAEJAABmaWxlOi8vLwwAAAABAQAATWFjaW50b3NoIEhECAAAAAQDAAAAoCBodAAAAAgAAAAABAAAQcVRjpiAAAAkAAAAAQEAADcyRTE2RDc0LUU4MzYtNDY0MC05NjZELTkxRThEMDM3RDYxQxgAAAABAgAAgQAAAAEAAADvEwAAAQAAAAAAAAAAAAAAAQAAAAEBAAAvAAAAYAAAAP7///8A8AAAAAAAAAcAAAACIAAATAIAAAAAAAAFIAAAvAEAAAAAAAAQIAAAzAEAAAAAAAARIAAAAAIAAAAAAAASIAAA4AEAAAAAAAATIAAA8AEAAAAAAAAgIAAALAIAAAAAAAAEAAAAAwMAAADwAAAEAAAAAwMAAAAAAAAEAAAAAwMAAAEAAAAcAAAAAQYAAMACAADMAgAA2AIAAMwCAADMAgAAzAIAAMwCAAC0AAAA/v///wEAAABYAgAADgAAAAQQAACQAAAAAAAAAAUQAADIAAAAAAAAABAQAADoAAAAAAAAAFQQAAAQAQAAAAAAAFUQAAAcAQAAAAAAAFYQAAAIAQAAAAAAAAAgAADkAgAAAAAAAAIgAAB8AQAAAAAAAAUgAAAoAQAAAAAAABAgAAAgAAAAAAAAABIgAABMAQAAAAAAACAgAABcAQAAAAAAAFAgAACYAQAAAAAAABDQAAAEAAAAAAAAAA=="
    metadata_in_tonight_trends = ET.SubElement(asset_r3_tonight_trends, "metadata")
    md1_in_tonight_trends = ET.SubElement(
    metadata_in_tonight_trends,
    "md",
    key="com.apple.proapps.studio.rawToLogConversion",
    value="0",
)
    md2_in_tonight_trends = ET.SubElement(
    metadata_in_tonight_trends,
    "md",
    key="com.apple.proapps.spotlight.kMDItemProfileName",
    value="HD (1-1-1)",
)
    md3_in_tonight_trends = ET.SubElement(
    metadata_in_tonight_trends, "md", key="com.apple.proapps.studio.cameraISO", value="0"
)
    md4_in_tonight_trends = ET.SubElement(
    metadata_in_tonight_trends,
    "md",
    key="com.apple.proapps.studio.cameraColorTemperature",
    value="0",
)
    md5_in_tonight_trends = ET.SubElement(
    metadata_in_tonight_trends, "md", key="com.apple.proapps.studio.cameraColorTemperature"
)
    array_md5_in_tonight_trends = ET.SubElement(md5_in_tonight_trends, "array")
    string1_in_tonight_trends = ET.SubElement(array_md5_in_tonight_trends, "string")
    string1_in_tonight_trends.text = "Apple ProRes 4444"
    string2_in_tonight_trends = ET.SubElement(md5_in_tonight_trends, "string")
    string2_in_tonight_trends.text = "Linear PCM"
    md6_in_tonight_trends = ET.SubElement(
    metadata_in_tonight_trends,
    "md",
    key="com.apple.proapps.mio.ingestDate",
    value="2024-03-13 16:29:08 + 0100",
)

    library_tonight_trends = ET.SubElement(
    fcpxml_root_tonight_trends, "library", location=f"{library_location}"
)
    event_tonight_trends = ET.SubElement(
    library_tonight_trends,
    "event",
    name=f"{event_name}",
    uid="02D0CB09-3878-4C40-A592-3925110BCD4D",
)
    project_tonight_trends = ET.SubElement(
    event_tonight_trends,
    "project",
    name=f"{name}",
    uid="4882168E-DE1E-4034-94DC-895C2639F28E",
    modDate="2024-04-06 20:14:03 +0200",
)
    sequence_tonight_trends = ET.SubElement(
    project_tonight_trends,
    "sequence",
    fomrat="r1",
    duration="17300/2500s",
    tcStart="0s",
    tcFormat="NDF",
    audioLayout="stereo",
    audioRate="48k",
)
    spine_tonight_trends = ET.SubElement(sequence_tonight_trends, "spine")
    gap1_tonight_trends = ET.SubElement(
    spine_tonight_trends,
    "gap",
    name="Gap",
    offset="0s",
    start="3600s",
    duration="9700/2500s",
)
    asset_clip1_tonight_trends = ET.SubElement(
    gap1_tonight_trends,
    "asset-clip",
    ref="r2",
    lane="1",
    offset="3600s",
    name="WIPE_TRENDS_TONIGHT_OUT",
    duration="9700/2500s",
    tcFormat="NDF",
    audioRole="dialogue",
)
    keyword_asset_clip1_tonight_trends = ET.SubElement(
    asset_clip1_tonight_trends,
    "keyword",
    start="0s",
    duration="9700/2500s",
    value="wipe tonight",
)
    marker_asset_clip_tonight_trends = ET.SubElement(
    asset_clip1_tonight_trends,
    "marker",
    start="12/5s",
    duration="100/2500s",
    value="Marker 1",
)
    asset_clip2_tonight_trends = ET.SubElement(
    spine_tonight_trends,
    "asset-clip",
    ref="r3",
    offset="9700/2500s",
    name="WIPE_TRENDS_TONIGHT_IN",
    duration="7600/2500s",
    tcFormat="NDF",
    audioRole="dialogue",
)
    keyword_asset_clip2_tonight_trends = ET.SubElement(
    asset_clip2_tonight_trends,
    "keyword",
    start="0s",
    duration="7600/2500s",
    value="wipe tonight",
)
    marker_asset_clip2_tonight_trends = ET.SubElement(
    asset_clip2_tonight_trends,
    "marker",
    start="11/25s",
    duration="100/2500s",
    value="Marker 1",
)
    smart_collection1_tonight_trends = ET.SubElement(
    library_tonight_trends, "smart-collection", name="Projects", match="all"
)
    match_clip_smart_collection1_tonight_trends = ET.SubElement(
    smart_collection1_tonight_trends, "match-clip", rule="is", type="project"
)
    smart_collection2_tonight_trends = ET.SubElement(
    library_tonight_trends, "smart-collection", name="All Video", match="any"
)
    match_media1_smart_collection2_tonight_trends = ET.SubElement(
    smart_collection2_tonight_trends, "match-media", rule="is", type="videoOnly"
)
    match_media2_smart_collection2_tonight_trends = ET.SubElement(
    smart_collection2_tonight_trends, "match-media", rule="is", type="videoWithAudio"
)
    smart_collection3_tonight_trends = ET.SubElement(
    library_tonight_trends, "smart-collection", name="Audio Only", match="all"
)
    match_media1_smart_collection3_tonight_trends = ET.SubElement(
    smart_collection3_tonight_trends, "match-media", rule="is", type="audioOnly"
)
    smart_collection4_tonight_trends = ET.SubElement(
    library_tonight_trends, "smart-collection", name="Stills", match="all"
)
    match_media1_smart_collection_4_tonight_trends = ET.SubElement(
    smart_collection4_tonight_trends, "match-media", rule="is", type="stills"
)
    smart_collection5_tonight_trends = ET.SubElement(
    library_tonight_trends, "smart-collection", name="Favourites", match="all"
)
    match_ratings1_smart_collection4_tonight_trends = ET.SubElement(
    smart_collection5_tonight_trends, "match-ratings", value="favourites"
)

    header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n'

    ET.indent(fcpxml_root_tonight_trends, space="  ", level=1)

    fcpxml_string_tonight_trends = ET.tostring(fcpxml_root_tonight_trends, encoding="unicode")

    fcpxml_tonight_trends = header + fcpxml_string_tonight_trends

    file.write(fcpxml_tonight_trends)