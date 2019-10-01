import xml.etree.ElementTree as ET

tree = ET.parse('prueba.xml')
root = tree.getroot()

for child in root:
    for first in child:
        print("\t {}: {}" .format(first.tag, first.text))
        for second in first:
            print("\t\t {}: {}".format(second.tag, second.text))
            for third in second:
                print("\t\t {}: {}".format(third.tag, third.text))


#^{[\s\S]+}([\s\S]+)$

