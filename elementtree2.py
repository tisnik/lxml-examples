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
