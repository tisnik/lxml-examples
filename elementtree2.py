import lxml.etree as ET

root = ET.Element("root")
root.text = "any text"

left = ET.SubElement(root, "left")
left.text = "ěščř"

middle = ET.SubElement(root, "middle")
middle.text = "<&>"

right = ET.SubElement(root, "right")
right.text = ""

# konstrukce stromu
tree = ET.ElementTree(root)

# zapis do souboru
tree.write("test2.xml")

tree.write("test2_pretty_print.xml", pretty_print=True)
