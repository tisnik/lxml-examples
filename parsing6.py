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
