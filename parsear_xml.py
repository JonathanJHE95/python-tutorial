##############
# PARSER XML #
##############

import xml.dom.minidom

# Imprimir documento
def main():
    # usamos parse para cargar el archivo XML
    doc = xml.dom.minidom.parse('myXML.xml')

    # Imprime el documento nodo y su primer hijo
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # Obtener la lista de los tag, e imprimirlos
    # uno por uno
    expertise = doc.getElementsByTagName('expertise')
    print('%d expertise: ' % expertise.length)
    for skill in expertise:
        print(skill.getAttribute('name'))

    # Crear un tag en un elemento XML
    newespertise = doc.createElement('expertise')
    newespertise.setAttribute('name', 'BigData')
    doc.firstChild.appendChild(newespertise)
    print(' ')

    # Obtener la lista de los tag, e imprimirlos
    # uno por uno
    expertise = doc.getElementsByTagName('expertise')
    print('%d expertise: ' % expertise.length)
    for skill in expertise:
        print(skill.getAttribute('name'))

if __name__ == '__main__':
    main()

