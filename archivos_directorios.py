##########################
####### EXISTENCIA #######
# DIRECTORIOS : ARCHIVOS #
##########################

# Diferente formas de verificar la existencia
# os.path.exists()
# os.path.isfile()
# os.path.isdir()
# pathlibPath.exists()


# os.path.exists() - Verifica rapida mente que exista(n)
import os.path
from os import path

def main():
    # Verifica si exsite un archivo
    print('Existe el archivo: '+str(path.exists('prueba.txt')))
    print('Existe el archivo: '+str(path.exists('prueba2.txt')))
    print('Existe el directorio: '+str(path.exists('carpeta')))

if __name__ == '__main__':
    main()

# os.path.isfile() - Verifica si es un archivo
def main():
    # Verifica si exsite un archivo
    print('Es un archivo: '+str(path.isfile('prueba.txt')))
    print('Es un archivo: '+str(path.isfile('carpeta')))

if __name__ == '__main__':
    main()

# os.path.isdir() - Verifica si es una carpeta
def main():
    # Verifica si exsite un archivo
    print('Es un directorio(carpeta): '+str(path.isdir('prueba.txt')))
    print('Es un directorio(carpeta): '+str(path.isdir('carpeta')))

if __name__ == '__main__':
    main()


# pathlibPath.exists() - Funciona en Python 3.4 o superior
# Se usa en programacion orientada a objetos para
# verificar si existe o no un archivo o directorio
import pathlib

def main():
    file = pathlib.Path('prueba.txt')
    if file.exists():
        print('El archivo existe')
    else:
        print('El archivo no existe')

if __name__ == '__main__':
    main()