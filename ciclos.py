##############
### CICLOS ###
##############
# FOR  WHILE #
##############

# WHILE
def main():
    x = 0
    # Declaramos el WHILE
    while (x < 4):
        print(x)
        x += 1


if __name__ == '__main__':
    main()

# Declaramos el FOR
# range : lista de numeros consecutivos
for x in range(2, 7):
    print(x)


# Usamos FOR para recorrer un arreglo : lista
def main():
    # Lista de numeros
    meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo']
    for m in meses:
        print(m.capitalize())


if __name__ == '__main__':
    main()

# FOR con brake
for x in range(10,20):
    # Rompe el ciclo cuando se cumple el IF
    if (x==15): break
    print(x)

# FOR : implementando brake y continue
print('siguiente ciclo')
for x in range(10,20):
    # Rompe el ciclo cuando se cumple el IF
    if (x % 5 == 0): continue
    print(x)

# ENUMERATE : Realiza 2 cosas
#   - Regresa la direccion del item
#   - Regresa el item

Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
for i, m in enumerate(Months):
    print(i, m)



