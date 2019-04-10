def converte(h, m):
    if(h>=12):
        return "P"
    else:
        return "A"

def printa(meridian):
    if(meridian == "A"):
        print(hour,":",min," A.M.")
    else:
        print(hour-12,":",min," P.M.")

n = 1

while(n==1):
    f = input("Deseja converter novo horario?")
    if(f=="s"):
        hour = int(input("Informe as horas:\n"))
        min = int(input("Informe as horas:\n"))
        printa(converte(hour, min))

    else: 
        break