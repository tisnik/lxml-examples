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

xml = "test2.xml"
tree = ET.parse(xml)

root = tree.getroot()

text = root.xpath("//text()")
print(text)

text = root.xpath("left//text()")
print(text)

text = tree.xpath("/root/left//text()")
print(text)
