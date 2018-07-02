#################
### FUNCIONES ###
#################

# Definicion y llamada de un metodo
def ejemplo1():
    print('Soy una funcion')

ejemplo1()

# Funcion con retorno de variable
def cuadrado(x):
    return x*x

print(cuadrado(5))

# Funciones con valores multiples
def suma(x,y):
    print(x+y)

suma(5,6)

# Recibir valores como array
def funcion_arreglo(*args):
    print(args)

funcion_arreglo(1,2,3,4,5)