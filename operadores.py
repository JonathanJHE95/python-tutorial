################
###OPERADORES###
################

### ARITMETICOS ### + - / * % , etc
# SUMA
x = 5
y = 6
print('La suma es:', x + y)

# RESTA
print('La resta es:', x - y)

# RESIDUO
print('Residuo: ', y % x)

#### COMPARACION ###  ( ==, != , <>, >,<=, etc)
# Mayor que
print('X > Y : ', x > y)

# Son iguales
print('Son iguales: ', x == y)

### ASIGNACION ### (+=, - = , *=, /= , etc.)
# asinamos un valor a la variable
res = x + y
# esto es igual a: res = res + x
res += x
print(("Line 1 - Result of + is ", res))

### LOGICOS ### AND OR NOT
# AND : regresa TRUE si ambos son TRUE
# OR : regresa TRUE si almenos un es TRUE
# NOT : regresa TRUE si es FALSE

a = True
b = False
print(('a and b is', a and b))
print(('a or b is', a or b))
print(('not a is', not a))

### EXISTENCIA ###
# in : Checa si el valor existe en la lista
# not in : Checa sino exista en la lista
x = 4
y = 8
list = [1, 2, 3, 4, 5];
if (x in list):
    print("X : Si esta disponible")
else:
    print("X : No esta disponible")
if (y not in list):
    print("Y : No esta disponible")
else:
    print("Y : Si esta disponible")

### IDENTITY ###
x = 20
y = 20
# Comprueba que dos elementos sean iguales
if (x is y):
    print("X & Y : Son iguales")

y = 30
# Comprueba que dos elementos son distintos
if (x is not y):
    print("X & Y : Son diferentes")

# Operador de precedencia # Se encierra en parentesis
v = 4
w = 5
x = 8
y = 2
z = 0
# Se encierra en parentesis dando prioridad
z = (v+w) * x / y
print("El resultado es: ", z)





