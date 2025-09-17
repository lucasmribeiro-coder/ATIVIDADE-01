dia = int(input("qual dia começou o evento?"))
hora = input("qual o horario que começou o evento? [hh:mm:ss] ").split(":")
hi = int(hora[0])
mi = int(hora[1])
si = int(hora[2])
dia_final = int(input("qual dia que terminou o evento?"))
hora_final = input("que horas terminou o evento? [hh:mm:ss] ").split(":")
hf = int(hora_final[0])
mf = int(hora_final[1])
sf = int(hora_final[2])
diare = dia_final - dia
horare = hf - hi
ss = sf - si
mm = mf - mi
st = diare * 86400 + horare * 3600 + mm * 60 + ss
d = st // 86400
h = (st % 86400) // 3600
m = (st % 3600) // 60
s = (st % 60 )
print(d, " dia(s)")
print(h, ' hora(s)')
print(m, " minutos")
print(s,"segundos")