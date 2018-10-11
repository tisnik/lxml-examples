import lxml.etree as ET

xml = "pom.xml"
tree = ET.parse(xml)

root = tree.getroot()
print(ET.tostring(root))
print()

children = root.getchildren()

for child in children:
    print(child.tag)
