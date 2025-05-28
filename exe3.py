#  Crie uma lista vazia e adicione 3 elementos usando append. Imprima a lista.

lista = []
nome1 = (input("digite o nome: "))
lista.append(nome1)
nome2 = (input("digite o nome: "))
lista.append(nome2)
nome3 = (input("digite o nome: "))
lista.append(nome3)

print()

for nome in lista:
    print(nome)