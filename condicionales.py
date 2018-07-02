###################
### CONDICIONAL ###
###################

# CONDICIONAL : IF
x = None

if (x):
    print('Ah Caray!..tengo algo')
else:
    print('No tengo nada')


# CONDICIONAL : IF ELIF ELSE
def main():
    x, y = 8, 4

    if (x < y):
        st = 'X es menor que Y'
    elif (x == y):
        st = 'X es igual a Y'
    else:
        st = 'X es mayor que Y'
    print(st)


if __name__ == '__main__':
    main()


# CONDICIONAL : FORMA-CORTA
def main():
    x, y = 8, 4
    st = 'X es menor que Y' if (x < y) else 'X es mayor que Y'
    print(st)


if __name__ == '__main__':
    main()

# EJEMPLO : IF ELIF ELSE
total = 100
country = "US"
# country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
elif total <= 100:
    print("Shipping Cost is $25")
elif total <= 150:
    print("Shipping Costs $5")
else:
    print("FREE")
if country == "AU":
    if total <= 50:
        print("Shipping Cost is  $100")
else:
    print("FREE")


### SENTENCIA : SWITCH
def switch(argument):
    switcher = {
        0: 'Caso 0',
        1: 'Caso 1',
        2: 'Caso 2'
    }
    return switcher.get(argument, 'Nada')


# Damos valor de 0
if __name__ == '__main__':
    argument = 0
    print(switch(argument))

# Damos valor de 1
if __name__ == '__main__':
    argument = 1
    print(switch(argument))