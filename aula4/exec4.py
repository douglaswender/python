lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n = int(input("INFORME UM NÚMERO A SER PESQUISADO:\n"))

for i in range(0, len(lista), 1):
    if(lista[i]==n):
        print("O valor %d foi encontrado na posição %d !" % (n, i))
        break
    