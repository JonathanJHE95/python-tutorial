
#####################
##### VARIABLES #####
#####################

### Definicion de variables
a, b = 100, 4

print(a, 'Yo valgo menos: '+str(b))
### Reasignamos valor a la variable
a = 'que onda'

print(a)

### Concatenar variables

texto = 'mi valor es: '
numero = 99

print(texto+str(numero))

### variables globales y locales
# Variable global
v_global = 'Soy una variable global'

print(v_global)

def soyunmetodo():
    # Variable local, se declaro dentro de una funcion
    v_local = 'soy una variable local'
    print(v_local)

soyunmetodo()
print(v_global)

### variables globales y locales 2
# global
v_global2 = 'Soy global'

print(v_global2)

def soyunmetodo():
    # Asignamos el valor de global2 a l variable local
    # Debemos usar el mismo nombre en las variables
    # global y local
    global v_global2
    print(v_global2)
    v_global2 = 'Ah Caray!'

soyunmetodo()
print(v_global)

### Eliminar una variable
f = 'Me borraran'
print(f)

# Elimina la variable
del f

# Comprueba la existencia de una variable
try:
    print(f)
except NameError:
    print('Me borraron')

