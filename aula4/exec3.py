data = str(input())

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])
#print(dia, mes, ano)

#print(data[2])
#print(data[5])
if(data[2] and data[5] !='/'):
   print("Formato de data errado!")
else:
    if(dia>31):
        print("Formato de data incorreto, data maior que 31")
    elif mes>12:
        print("Formato de data incorreto, mes maior que 12")
    elif ano>9999:
        print("Formato de data incorreto, ano maior que 4 dígitos")
    else:
        print("Formato de data é válido!")