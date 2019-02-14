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
