import lxml.etree as ET

xml = "test5.xml"
tree = ET.parse(xml)

root = tree.getroot()
print(ET.tostring(root))
