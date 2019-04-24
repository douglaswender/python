total = 0

def somalista(lista):
    total = 0
    for i in range(0, len(lista), 1):
        total=lista[i]+total
    return total

list = [2,3,5]

total = somalista(list)

print(total)