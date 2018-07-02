###################
# INTERNET ACCESS #
###################

import  urllib.request

# Abrimos una conexion al url
weburl = urllib.request.urlopen('https://www.youtube.com/watch?v=r3AEUWweDyE')

# Codigo : 200 nos dice que fue exiosa la conexion
#obtenemos el codigo resultado y lo mostramos
print('El codigo fue: '+str(weburl.getcode()))

# Imprime el codigo html
# Leer la informacion del url
data = weburl.read()
print(data)






