def converte(graus):
    f = (9*graus+160)/5
    k = graus + 273.15

    return ("Fahrenheit: %.2f\nKelvin: %.2f" % (f,k))


print(converte(32))