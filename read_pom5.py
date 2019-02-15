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

xml = "pom.xml"
tree = ET.parse(xml)

root = tree.getroot()

dependency_ids = tree.xpath("//groupId/text()")

for dependency_id in dependency_ids:
    print(dependency_id)
