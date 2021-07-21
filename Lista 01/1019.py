tempo = int(input())

horas = tempo//3600
restoHoras = tempo%3600
minutos = restoHoras//60
segundos = restoHoras%60
print(horas, restoHoras, minutos, segundos)
print('{}:{}:{}' .format(horas, minutos, segundos))