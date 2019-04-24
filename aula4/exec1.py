def calculamedia(n1, n2):
    m = (n1+n2)/2

    if(m>=7):
        if(m==10):
            print("Aprovado com distinção!, média: 10")
        else:
            print("Aprovado! Média: %.1f" % m)
    else:
        print("Reprovado! Média: %.1f" % m)

calculamedia(6,7)
        