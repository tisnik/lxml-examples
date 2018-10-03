import lxml.etree as ET

root = ET.Element("root")

left = ET.SubElement(root, "left")
right = ET.SubElement(root, "right")

# konstrukce stromu
tree = ET.ElementTree(root)

# zapis do souboru
tree.write("test1.xml")

tree.write("test1_pretty_print.xml", pretty_print=True)
