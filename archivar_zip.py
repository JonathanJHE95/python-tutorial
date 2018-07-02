#######
# ZIP #
#######

import shutil
from os import  path
from zipfile import ZipFile

# Crear archivos .zip
def main():
    if path.exists('prueba.txt'):
        src = path.realpath('prueba.txt')

        # Colocar arhivos dentro del ZIP
        root_dir, tail = path.split(src)
        shutil.make_archive('zip_archivo', 'zip', root_dir)

        # Exito
        print('Archivo empaquetado')

    else:
        print('El archivo no existe')


if __name__ == '__main__':
    main()


############ Agregar archivos a ZIP
def main():
    if path.exists('prueba.txt'):
        src = path.realpath('prueba.txt')

        # Colocar arhivos dentro del ZIP
        root_dir, tail = path.split(src)
        shutil.make_archive('zip_archivo', 'zip', root_dir)

        with ZipFile('zip_archivo.zip', 'w') as newzip:
            newzip.write('prueba.txt.bak')
            newzip.write('tuplas.py')

        # Exito
        print('Archivo empaquetado')

    else:
        print('El archivo no existe')


if __name__ == '__main__':
    main()