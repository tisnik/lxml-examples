import lxml.etree as ET

xml = "test5.xml"
tree = ET.parse(xml)

root = tree.getroot()

# relativni cesta
nodes = root.xpath("right/right")

print("Nodes: {}".format(len(nodes)))

for node in nodes:
    print(node.get("popis"))
