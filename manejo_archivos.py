######################
# MANEJO DE ARCHIVOS #
######################

# Mode	Description
# 'r' - This is the default mode. It Opens file for reading.
# 'w' - This Mode Opens file for writing.
#       If file does not exist, it creates a new file.
#       If file exists it truncates the file.
# 'x - Creates a new file. If file already exists, the operation fails.
# 'a' - Open file in append mode.
#       If file does not exist, it creates a new file.
# 't' - This is the default mode. It opens in text mode.
# 'b' - This opens in binary mode.
# '+' - This will open a file for reading and writing (updating)

# Crear un archivo de texto y agregar informacion
def main():
    # paso 1 - creacion
    f = open('prueba.txt', 'w+')

    # paso 2 - agregar informacion
    for i in range(10):
        # write - inserta datos en el archivo
        f.write('Esta es la linea %d\r\n' % (i + 1))

    # close - cerramos el archivo
    f.close()


if __name__ == '__main__':
    main()


# Agregar mas informacion en el archivo
def main():
    f = open('prueba.txt', 'a+')

    for i in range(2):
        f.write('Append linea %d\r\n' % (i + 1))

    f.close()


if __name__ == '__main__':
    main()


# Leer un archivo
def main():
    f = open('prueba.txt', 'r')

    if f.mode == 'r':
        contenido = f.read()

    print(contenido)


if __name__ == '__main__':
    main()


# Leer un archivo linea por linea
def main():
    f = open('prueba.txt', 'r')

    f1 = f.readlines()
    for x in f1:
        print(x)


if __name__ == '__main__':
    main()

