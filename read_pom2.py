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
