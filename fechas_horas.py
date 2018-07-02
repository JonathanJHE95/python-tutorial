################
### DATETIME ###
################

# date – Manipulate just date ( Month, day, year)
# time – Time independent of the day (Hour, minute, second, microsecond)
# datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
# timedelta— A duration of time used for manipulating dates
# tzinfo— An abstract class for dealing with time zones

from datetime import date
from datetime import time
from datetime import timedelta
from _datetime import datetime

def main():
    ## DATA OBJECT
    # Obtener la fecha de hoy
    today = date.today()
    print('Ahora es: ', str(today))

today = date.today()
print('Hoy es '+str(today.day)+' de '+str(today.month)+' del '+str(today.year))

if __name__ == '__main__':
    main()

############# DIA DE LA SEMANA
# Monday - 0
# Tuesday - 1
# Wednesday - 2
# Thursday - 3
# Friday - 4
# Saturday - 5
# Sunday - 6

print('El dia de hoy es: ', today.weekday())

print('La hora y dia de hoy son:', datetime.now())

hora = datetime.time(datetime.now())
print('La hora es:',hora)

# dia de la semana
wd = date.weekday(today)
# dias
days= ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print('Numero del dia de hoy:', str(wd))
print('Entonces es:', days[wd])

###### FORMATO HORA Y FECHA

now = datetime.now() # fecha actual
print(now.strftime('%Y')) # year completo
print(now.strftime('%y')) # year corto
print(now.strftime('%m')) # mes completo
print(now.strftime('%B')) # mes nombre
print(now.strftime('%b')) # mes nombre-corto
print(now.strftime('%d')) # dia-fecha
print(now.strftime('%A')) # dia nombre
print(now.strftime('%a')) # dia nombre-corto

# %C- indicates the local date and time
# %x- indicates the local date
# %X- indicates the local time

print(now.strftime('%c')) # fecha con nombres
print(now.strftime('%x')) # fecha local
print(now.strftime('%X')) # hora corta local

# FORMATO DE HORA
print('------------')
# Formato de 12 horas
# Indica si es AM o PM
# HORA : MINUTOS : SEGUNDOS
print(now.strftime('%I:%M:%S %p'))

# Formato de 24 horas
# HORA : MINUTOS
print(now.strftime('%H:%M'))

print('------------')
# EJEMPLO TIMEDELTA
print(timedelta(days=365, hours=8, minutes=15))

# Dia de hoy
print('Hoy es: '+str(datetime.now()))

# Un year despues
print('un year despues: '+str(datetime.now() + timedelta(days=365)))

# Una semana y 4 dias despues
print('Una semana y 4 dias despues: '+str(datetime.now() + timedelta(weeks=1, days=4)))

# Hace cuantos dias fue new yeat
today = date.today()
nyd = date(today.year, 1, 1)

if nyd < today:
    print('New Year fue %d dias atras' % (today - nyd).days)