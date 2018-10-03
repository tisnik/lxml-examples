import lxml.etree as ET

root = ET.Element("root")
root.text = "text, který může\nobsahovat i konce řádků"

left = ET.SubElement(root, "left")
left.text = "ěščř"

right = ET.SubElement(root, "right")
right.text = "\n\n\n"

# konstrukce stromu
tree = ET.ElementTree(root)

# zapis do souboru
tree.write("test3.xml")

tree.write("test3_pretty_print.xml", pretty_print=True)
