# Las tuplas no permiten cambios
# Tampoco pueden ser borradas
# Las tuplas son hashables

# Tupla vacia
meses = ()

# Asignacion de valores
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio')
numeros = (1,2,3,4,5,6,7,8,9)
print(meses)

# Imprimir valor en direccion
print(meses[0])
print(meses[2:6])

print(numeros[0])
print(numeros[2:6])

# Empaquetado y desmpaquetado de una tupla
# Empaquetado
x = ('Mario', 1989, 'Japon')

# Desempaquetado
# Asignamos los valores en orden a una variable
(nombre, year, pais) = x

print(nombre)
print(year)
print(pais)

# Comparacion de tuplas
# Compara el primer elemento en cada tupla
# En caso de ser verdadero
a=(5,6)
b=(1,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

# En caso de ser iguales
# Procede al siguiente elemento
a=(5,6)
b=(5,4)
if (a>b):print("a is bigger")
else: print ("b is bigger")

# En caso de ser false
a=(5,6)
b=(6,4)
if (a>b):print("a is bigger")
else: print("b is bigger")

### Regresa un lista de los elementos
# Tuples and dictionary
# Donde cada tupla, contiene un par de valores
a = {'x':100, 'y':200}
b = a.items()
print(b)

# Enlistar los elemntos
b = list(a.items())
print(b)
