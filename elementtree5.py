#!/usr/bin/env python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2017, 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import lxml.etree as ET

root = ET.Element("root", atribut1="1", attribut2="2", popis="koren")

left1stLevel = ET.SubElement(root, "left", popis="levy vnitrni poduzel")
middle1stLevel = ET.SubElement(root, "middle", popis="prostredni vnitrni poduzel")
right1stLevel = ET.SubElement(root, "right", popis="pravy vnitrni poduzel")

left2ndLevelA = ET.SubElement(left1stLevel, "left", popis="list zcela nalevo")
middle2ndLevelA = ET.SubElement(left1stLevel, "middle", popis="list")
right2ndLevelA = ET.SubElement(left1stLevel, "right", popis="list")

left2ndLevelB = ET.SubElement(middle1stLevel, "left", popis="list")
middle2ndLevelB = ET.SubElement(middle1stLevel, "middle", popis="prostredni list")
right2ndLevelB = ET.SubElement(middle1stLevel, "right", popis="list")

left2ndLevelC = ET.SubElement(right1stLevel, "left", popis="list")
middle2ndLevelC = ET.SubElement(right1stLevel, "middle", popis="list")
right2ndLevelC = ET.SubElement(right1stLevel, "right", popis="list zcela napravo")

# konstrukce stromu
tree = ET.ElementTree(root)

# zapis do souboru
tree.write("test5.xml")

tree.write("test5_pretty_print.xml", pretty_print=True)
