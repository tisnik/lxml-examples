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

root = ET.Element("root")

left1stLevel = ET.SubElement(root, "left")
middle1stLevel = ET.SubElement(root, "middle")
right1stLevel = ET.SubElement(root, "right")

left2ndLevelA = ET.SubElement(left1stLevel, "left")
middle2ndLevelA = ET.SubElement(left1stLevel, "middle")
right2ndLevelA = ET.SubElement(left1stLevel, "right")

left2ndLevelB = ET.SubElement(middle1stLevel, "left")
middle2ndLevelB = ET.SubElement(middle1stLevel, "middle")
right2ndLevelB = ET.SubElement(middle1stLevel, "right")

left2ndLevelC = ET.SubElement(right1stLevel, "left")
middle2ndLevelC = ET.SubElement(right1stLevel, "middle")
right2ndLevelC = ET.SubElement(right1stLevel, "right")

# konstrukce stromu
tree = ET.ElementTree(root)

# zapis do souboru
tree.write("test4.xml")

tree.write("test4_pretty_print.xml", pretty_print=True)
