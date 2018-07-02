var1 = 'cadenita'
var2 = 'software'

# Imprime el caracter de una direccion
print('var1[0]:', var1[0])

# Imprime apartir de una direccion
print('Apartir de 0 ', var2[:5])
print('var2[1:5]', var2[1:5])

# Comprueba la existencia d un caracter o palabra
# Imprime true or false
print('Existe')
print('w' in var2)

# Comprueba que no exista un caracter o palabra
print('No existe')
print('p' not in var2)

# Salto de linea
print('Soy un\nsalto')

# Une 2 variables
nombre = 'jonathan'
edad = 22
print(nombre,edad)

# Une 2 cadenas
cadena1 = 'Cristo'
cadena2 = '17'
print(cadena1+cadena2)

# Repite una variable
print(cadena2*6)

# Reemplaza una palabra o caracter
frase = 'soy un caramelo de leche'
frase1 = frase.replace('leche', 'crema')
print(frase1)

# Letras a minusculas
texto = 'minusculas'
print(texto.upper())

# Texto a mayusculas
texto = 'MAYUSCULAS'
print(texto.lower())

# Primer caracter de texto en mayuscula
texto="primera letra mayuscula"
print(texto.capitalize())

# Agregar algo entre cada caracter
print(":".join(nombre))

# Invertir una cadena
print(''.join(reversed(nombre)))

# Segmentar una cadena apartir de un caracter
word="guru99 career guru99"
print(word.split(' '))

# Otro ejemplo de segmentacion
word="guru99 career guru99"
print(word.split('r'))

# la cadena es inmutable, no se puede reemplazar
# el contenido
nombre.replace(nombre,cadena1)
print(nombre)

# Forma correcta de reemplazar
nombre = nombre.replace(nombre, cadena1)
print(nombre)