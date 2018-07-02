##############
# PARSER XML #
##############

import xml.etree.ElementTree as ET

tree = ET.parse('myXML2.xml')
root = tree.getroot()

# Obten toda la informacion
print('Expertise data:')

for elem in root:
    for subelem in elem:
        print(subelem.text)
