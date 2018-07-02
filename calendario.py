##############
## CALENDAR ##
##############

import calendar

# Creamos el calendario en texto plano
#                        DIA DE LA SEMANA
c = calendar.TextCalendar(calendar.SUNDAY)
#                  YEAR : MOTH
str = c.formatmonth(2018, 6)
print(str)


# Creamos el calendario en formato HTML
#                        DIA DE LA SEMANA
c = calendar.HTMLCalendar(calendar.SUNDAY)
#                  YEAR : MOTH
str = c.formatmonth(2018, 6)
print(str)

# Dias del mes
for i in c.itermonthdays(2018, 6):
    print(i)

# Nombre de los meses
for name in calendar.month_name:
    print(name)

# Nombre de los dias
for name in calendar.day_name:
    print(name)

# Hay un día de auditoría en cada primer lunes de una semana,
# y desea saber la fecha de cada mes del año, puede usar este código
# Calcular el primer lunes de cada mes

for mes in range(1,13):
    # Lista de las semans del mes
    calendario = calendar.monthcalendar(2018, mes)
    # Segundo lunes debe estar dentro de las primeras 2 semanas
    semana1 = calendario[0]
    semana2 = calendario[1]

    if semana1[calendar.MONDAY] !=0:
        auditday = semana1[calendar.MONDAY]
    else:
        auditday = semana2[calendar.MONDAY]

    print('%10s %2d' % (calendar.month_name[mes], auditday))


