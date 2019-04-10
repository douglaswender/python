def somaimposto(taxa, custo):
    custo = custo+(custo*taxa/100)
    return custo

arg1 = float(input("Informe a taxa:\n"))
arg2 = float(input("Informe o custo atual:\n"))

print("O novo custo do produto com a taxa: ", arg1, " e preço: ", arg2, " é de: ", somaimposto(arg1, arg2))