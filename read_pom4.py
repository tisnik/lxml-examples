import lxml.etree as ET

xml = "pom.xml"
tree = ET.parse(xml)

root = tree.getroot()

dependency_ids = tree.xpath("/project/dependencies/dependency/groupId/text()")

for dependency_id in dependency_ids:
    print(dependency_id)
