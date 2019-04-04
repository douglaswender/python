num = int(input("informe o numero do funcionario:\n"))
horas = int(input("informe a quantidade de horas trabalhadas:\n")) 
valor = float(input("informe o valor que recebe por hora:\n"))

salario = horas*valor

print("o funcionario %d tem o salário de: %.2f" % (num, salario))

