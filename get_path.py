import lxml.etree as ET

root = ET.Element("root", atribut1="1", attribut2="2", popis="koren")

left1stLevel = ET.SubElement(root, "left", popis="levy vnitrni poduzel")
right1stLevel = ET.SubElement(root, "right", popis="pravy vnitrni poduzel")

left2ndLevelA = ET.SubElement(left1stLevel, "left", popis="list zcela nalevo")
right2ndLevelA = ET.SubElement(left1stLevel, "right", popis="list")

left2ndLevelB = ET.SubElement(right1stLevel, "left", popis="list")
right2ndLevelB = ET.SubElement(right1stLevel, "right", popis="list zcela napravo")

# konstrukce stromu
tree = ET.ElementTree(root)

print(tree.getpath(root))
print(tree.getpath(left1stLevel))
print(tree.getpath(right2ndLevelB))
