import lxml.etree as ET

xml = "test5.xml"
tree = ET.parse(xml)

root = tree.getroot()
print(ET.tostring(root))

print(root.get("atribut1"))
print(root.get("popis"))

children = root.getchildren()

for child in children:
    print(child.get("popis"))
