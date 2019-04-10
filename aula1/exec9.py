peso = float(input("informe o peso\n"))
altura = float(input("informe a altura\n"))

imc = peso/(altura*altura)

if(imc<18.5):
    print("Abaixo do peso, IMC: ", imc)
elif(imc>=18.5 and imc<25):
    print("Peso normal, IMC: ", imc)
elif(imc>=25.0 and imc<30):
    print("Sobrepeso, IMC: ", imc)
elif(imc>=30 and imc<35):
    print("Obesidade grau 1, IMC: ", imc)
elif(imc>=35 and imc<40):
    print("Obesidade grau 2, IMC: ", imc)
else:
    print("Obesidade grau 3, IMC: ", imc)
