import lxml.etree as ET

xml = "test5.xml"
tree = ET.parse(xml)

root = tree.getroot()

# absolutni cesta
nodes = root.xpath("/root/right/right")

print("Nodes: {}".format(len(nodes)))

for node in nodes:
    print(node.get("popis"))
