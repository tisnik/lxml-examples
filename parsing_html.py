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

parser = ET.HTMLParser()

url = "http://www.zyvra.org/html/simple.htm"

tree   = ET.parse(url, parser)

root = tree.getroot()

print("\n\n\nContent:")
result = ET.tostring(tree.getroot(), pretty_print=True, method="html")
print(result)

print("\n\n\nTitle:")
title = root.xpath("/html/head/title/text()")
print(title[0])

divs = root.xpath("body//p")

print("\n\n\nText:")

for div in divs:
    print(div.text)

print("\n\n\nAlign:")

for div in divs:
    print(div.get("align"))
