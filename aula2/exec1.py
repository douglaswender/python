def sum(d1, d2, d3):
    return d1+d2+d3

dados =  []

for i in range(0, 3):
    dados.append(float(input("Informe um número")))

print(sum(dados[0], dados[1], dados[2]))