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

artifact_id = tree.xpath("/project/artifactId/text()")[0]
print("artifact ID: {aid}".format(aid=artifact_id))

group_id = tree.xpath("/project/groupId/text()")[0]
print("Group ID: {gid}".format(gid=group_id))

version = tree.xpath("/project/version/text()")[0]
print("Version: {v}".format(v=version))
