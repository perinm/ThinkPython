import time

a=time.time()
dias = a//86400
r1 = a%86400
horas = r1//3600
r2 = r1%3600
minutos= r2//60
segs= (r2%60)
print(segs)

print("Se passaram "+str(int(dias))+" dias e o horário atual é: "+str(int(horas))+"h"+str(int(minutos))+"min"+str(int(segs))+"s")