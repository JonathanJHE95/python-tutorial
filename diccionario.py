# En un diccionario se defines 2 valores
#
# Key : Puede ser un elemento
# Value : Puede ser un una lista, un lista dentro de otra,
#           numeros, etc
#
# Puntos importantes al usar keys
#   - No se permite mas de un valor por clave
#   - No se permiten keys duplicadas
#   - El key puede ser de cualquier tipo
#   - Los key son distintan con mayusculas y minusculas,
#       tienden a tratarse como keys distintas

# Ejemplo de una lista
diccionario = {'Sam': 24, 'Country': 'USA', 'Program': 'iCarly', 'Friend': 'Carly'}

# Imprimir direccion
print(diccionario['Program'])

# nombre = key = Sam
# edad = value = 24
print(diccionario['Sam'])

# Copiar informacion de un diccionario a otro
Boys = {'Tim': 18, 'Charlie':12, 'Robert':25}
Girls = {'Tiffany':22}
studentX = Boys.copy()
studentY = Girls.copy()
print(studentX)
print(studentY)

# Agregar nuevo elemento a diccionario
Girls.update({'Sara': 12})
print(Girls)

# Borrar elemento a un diccionario
del Boys['Tim']
print(Boys)

# Mostrar listado de elementos
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % list(Dict.items()))

# Comprobar la existencia, elemento(s) de un diccionario
# dentro de otro
Boys = {'Tim': 18, 'Charlie':12, 'Robert':25}
Girls = {'Tiffany':22}

for key in list(Boys.keys()):
    if key in list(Dict.keys()):
        print(True)
    else:
        print(False)

# Imprimir elementos de un diccionario en orden
# alpabetico
Students = list(Dict.keys())
Students2 = list(Dict.keys())
# Ordenar lista forma ascendente
Students.sort()
# Ordenar lista forma descendente
Students2.sort(reverse=True)
# Impresion de los elementos
# Forma ascendente
print('---Acendente---')
for S in Students:
    print(":".join((S,str(Dict[S]))))

# Forma descendente
print('---Descendente---')
for S in Students2:
    print(":".join((S,str(Dict[S]))))

# Imprime el numero de elementos en un diccionario
print("Tamaño de un diccionario\nSize: %d" % len(Dict))

# Imprime el tipo de variable
print("Tipo de variable: %s" %type (Dict))

# Regresar diccionario como una cadena de texto
print("Cadena de texto:%s"%str(Dict))






