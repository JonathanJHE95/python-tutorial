##############
# COPY FILES #
##############

import shutil
import datetime
from os import path
from datetime import date, time, timedelta
import time

def main():
    # Haremos un duplicado del archivo actual
    if path.exists('prueba.txt'):
        # Obtenemos el archivo en la direccion
        src = path.realpath('prueba.txt')

        # filtramos la direccion
    head, tail = path.split(src)
    print('path(direccion): ' + head)
    print('file(archivo): ' + tail)

    # Cambiamos el nombre
    dst = src + '.bak'

    # Realizamos la copia del archivo
    shutil.copy(src, dst)

    # Realizar copia con permisos y metadatos
    shutil.copystat(src, dst)


if __name__ == '__main__':
    main()


# Obtener informacion de un archivo
def main():
    # Obtener fecha de modificacion
    t = time.ctime(path.getmtime('prueba.txt.bak'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('prueba.txt.bak')))


if __name__ == '__main__':
    main()