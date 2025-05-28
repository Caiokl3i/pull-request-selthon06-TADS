# Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome em uma linha.
lista = []
nome1 = (input("digite o nome: "))
lista.append(nome1)
nome2 = (input("digite o nome: "))
lista.append(nome2)
nome3 = (input("digite o nome: "))
lista.append(nome3)
nome4 = (input("digite o nome: "))
lista.append(nome4)
nome5 = (input("digite o nome: "))
lista.append(nome5)

print()

for nome in lista:
    print(nome)