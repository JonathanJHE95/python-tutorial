###############
# Rename File #
###############

import os
from os import path

def main():
    if path.exists('prueba.txt'):
        src = path.realpath('prueba.txt')

        # Renombramos el archivo
        os.rename('prueba.txt', 'copia-prueba.txt')

        # Cambio exitoso
        print('Se cambio el nombre exitosamente')

    else:
        print('El archivo no existe')


if __name__ == '__main__':
    main()