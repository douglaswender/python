m=0
for i in range(0, 10, 1):
    n = int(input("Informe um número:"))
    if(n>m):
        m=n

print("O maior número é: %d" % m)