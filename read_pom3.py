import lxml.etree as ET

xml = "pom.xml"
tree = ET.parse(xml)

root = tree.getroot()

dependencies = tree.xpath("/project/dependencies/dependency")

for dependency in dependencies:
    print(dependency.xpath("groupId/text()")[0])
