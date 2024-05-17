import xml.etree.ElementTree as ET

root = ET.Element("fcpxml", version="1.0")
project = ET.SubElement(root, "project")
resources = ET.SubElement(project, "resources")
format = ET.SubElement(
    resources, "format", id="r1", frameDuration="100/2997s", width="1920", height="1080"
)

clip = ET.SubElement(project, "clip", name="example", format="f1", duration="100/2997s")

ET.indent(root, space="  ", level=0)

print(ET.tostring(root, encoding="unicode", method="xml"))
