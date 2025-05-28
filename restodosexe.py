import random
from collections import Counter, defaultdict
from itertools import groupby

# Exercícios Fáceis
def ex6'():
    nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
    print("Maior:", max(nums), "Menor:", min(nums))

def ex7():
    lista = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lista):
        print(lista[i])
        i += 1

def ex8():
    cores = ["azul", "verde", "amarelo"]
    cores.insert(1, "vermelho")
    print(cores)

def ex9():
    l = [3, 1, 4, 1, 5, 9]
    print("Crescente:", sorted(l))
    print("Decrescente:", sorted(l, reverse=True))

def ex10():
    palavras = ["maçã", "banana", "uva"]
    print(", ".join(palavras))

def ex11():
    zeros = [0 for _ in range(10)]
    print(zeros)

def ex12():
    for _ in range(5):
        n = int(input("Digite um número: "))
        print(f"{n} é maior que 10?" , n > 10)

def ex13():
    pares = [x for x in range(1, 11) if x % 2 == 0]
    print(pares)

def ex14():
    frutas = ["banana", "maçã", "uva"]
    frutas.insert(0, "morango")
    print(frutas)

def ex15():
    letras = ["A", "B", "C"]
    print(letras.pop())

def ex16():
    l = [10, 20, 30, 40, 50]
    l[1] = 99
    print(l)

def ex17():
    l = [int(input("Digite um número: ")) for _ in range(5)]
    print("Média:", sum(l)/len(l))

def ex18():
    print(7 in [3, 6, 9, 12])

def ex19():
    nomes = []
    while True:
        nome = input("Digite um nome ou 'sair': ")
        if nome.lower() == "sair":
            break
        nomes.append(nome)
    print(nomes)

def ex20():
    letras = ['a', 'b', 'c', 'd', 'e']
    print("".join(letras))

# Exercícios Médios
def ex21():
    nums = [int(input("Número: ")) for _ in range(10)]
    for n in nums[:]:
        if n % 2 == 0:
            nums.remove(n)
    print(nums)

def ex22(lista):
    return list(set(lista))

def ex23(lista):
    nova = []
    for item in lista:
        if item not in nova:
            nova.append(item)
    return nova

def ex24(nums):
    pares = [n for n in nums if n % 2 == 0]
    impares = [n for n in nums if n % 2 != 0]
    return pares, impares

def ex25():
    frase = input("Digite uma frase: ")
    return frase.split()

def ex26(lista):
    return lista[::-1]

def ex27():
    pilha = []
    pilha.append(1); print(pilha)
    pilha.append(2); print(pilha)
    pilha.pop(); print(pilha)

def ex28(lista):
    return sum([x for x in lista if isinstance(x, (int, float))])

def ex29():
    lista = []
    while True:
        print("1. Adicionar\n2. Remover\n3. Listar\n4. Sair")
        op = input("Escolha: ")
        if op == "1":
            lista.append(input("Item: "))
        elif op == "2":
            lista.remove(input("Item a remover: "))
        elif op == "3":
            print(lista)
        elif op == "4":
            break

def ex30(strings):
    return [len(s) for s in strings]

def ex31(lista):
    return lista == sorted(lista)

def ex32(nomes):
    return [n.upper() for n in nomes]

def ex33():
    return [x for x in range(1, 101) if x % 3 == 0]

def ex34():
    lista = []
    while True:
        n = int(input("Digite um número (-1 para sair): "))
        if n == -1:
            break
        lista.append(n)
    print("Média:", sum(lista)/len(lista))

def ex35():
    pessoas = [("Ana", 20), ("João", 17), ("Luiz", 30)]
    for nome, idade in pessoas:
        if idade > 18:
            print(nome)

def ex36(lista):
    return sorted(set(lista))[-2]

def ex37(palavras):
    return [p for p in palavras if len(p) >= 4]

def ex38(lista):
    return lista[::-1]

def ex39(l1, l2):
    return list(l1) + list(l2)

def ex40(lista, val):
    return lista.count(val)

# Exercícios Difíceis
def ex41(l1, l2):
    return list(set(l1) & set(l2))

def ex42(lista):
    return dict(Counter(lista))

def ex43():
    carrinho = []
    while True:
        print("1. Adicionar\n2. Remover\n3. Total\n4. Sair")
        op = input("Escolha: ")
        if op == "1":
            nome = input("Produto: ")
            preco = float(input("Preço: "))
            carrinho.append((nome, preco))
        elif op == "2":
            nome = input("Produto a remover: ")
            carrinho = [item for item in carrinho if item[0] != nome]
        elif op == "3":
            print("Total:", sum(p[1] for p in carrinho))
        elif op == "4":
            break

def ex44(lista, n):
    return [lista[i:i+n] for i in range(0, len(lista), n)]

def ex45(lista_de_listas):
    return [item for sublist in lista_de_listas for item in sublist]

def ex46(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ex47():
    alunos = [(input("Nome: "), float(input("Nota: "))) for _ in range(3)]
    alunos.sort(key=lambda x: x[1], reverse=True)
    print(alunos)

def ex48(lista):
    return [x**2 for x in lista if x % 2 == 0]

def ex49(lista, n):
    return lista[-n:] + lista[:-n]

def ex50(lista):
    return max(lista, key=lambda x: x[1]), min(lista, key=lambda x: x[1])

def ex51():
    fila = []
    while True:
        print("1. Chegada\n2. Atender\n3. Sair")
        op = input("Escolha: ")
        if op == "1":
            fila.append(input("Nome: "))
        elif op == "2":
            print("Atendido:", fila.pop(0))
        elif op == "3":
            break

def ex52(lista):
    def count_vowels(s):
        return sum(s.count(v) for v in 'aeiouAEIOU')
    return sorted(lista, key=count_vowels)

def ex53(lista, alvo):
    ini, fim = 0, len(lista)-1
    while ini <= fim:
        meio = (ini + fim) // 2
        if lista[meio] == alvo:
            return True
        elif lista[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return False

def ex54(lista):
    d = defaultdict(list)
    for palavra in lista:
        d[len(palavra)].append(palavra)
    return dict(d)

def ex55(lista):
    return [(x, y) for i, x in enumerate(lista) for y in lista[i+1:] if x + y == 10]

def ex56():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for linha in matriz:
        print(sum(linha))

def ex57(l1, l2):
    return [(l1[i], l2[i]) for i in range(min(len(l1), len(l2)))]

def ex58(lista):
    n = len(lista)
    seq = []
    for i in range(n):
        temp = [lista[i]]
        for j in range(i+1, n):
            if lista[j] > temp[-1]:
                temp.append(lista[j])
        if len(temp) > len(seq):
            seq = temp
    return seq

def ex59(celsius):
    return [round((c * 9/5) + 32, 2) for c in celsius]

def ex60():
    usuarios = []
    while True:
        op = input("1. Cadastrar, 2. Login, 3. Sair: ")
        if op == "1":
            usuarios.append((input("Login: "), input("Senha: ")))
        elif op == "2":
            l, s = input("Login: "), input("Senha: ")
            if (l, s) in usuarios:
                print("Bem-vindo!")
            else:
                print("Login inválido")
        elif op == "3":
            break

# Exercícios com Dicionários
def ex61():
    alunos = {
        "João": [7, 8, 9],
        "Maria": [6, 7, 8]
    }
    for nome, notas in alunos.items():
        print(nome, "Média:", sum(notas)/len(notas))

def ex62():
    pessoas = [{"nome": "Ana", "idade": 20, "cidade": "SP"},
               {"nome": "João", "idade": 30, "cidade": "RJ"}]
    for p in pessoas:
        print(p)

def ex63():
    produtos = {}
    while True:
        nome = input("Produto (ou 'fim'): ")
        if nome == "fim":
            break
        preco = float(input("Preço: "))
        produtos[nome] = preco
    busca = input("Buscar produto: ")
    print("Preço:", produtos.get(busca, "Não encontrado"))

def ex64():
    return {i: i**2 for i in range(1, 6)}

def ex65():
    dados = [(input("Nome: "), int(input("Idade: "))) for _ in range(2)]
    return dict(dados)

def ex66():
    frutas = {"maçã": 10, "banana": 5}
    vendas = ["maçã", "banana", "banana"]
    for fruta in vendas:
        frutas[fruta] -= 1
    print(frutas)

def ex67():
    agenda = {
        "Ana": ["1234-5678"],
        "João": ["8765-4321"]
    }
    nome = input("Consultar: ")
    print(agenda.get(nome, "Não encontrado"))

def ex68():
    tuplas = [("nome", "Ana"), ("idade", 30)]
    return dict(tuplas)

def ex69(d, chave):
    print(d.get(chave, "Chave não encontrada"))

def ex70(palavra):
    return {letra: i for i, letra in enumerate(palavra)}

def ex71(d):
    return sum([sum(t) for t in d.values()])

def ex72(d):
    for nome, notas in d.items():
        if sum(notas)/len(notas) >= 7:
            print(nome)

def ex73(d):
    return {v: k for k, v in d.items()}

def ex74(d, nome):
    print(d.get(nome, []))

def ex75():
    votos = [("Ana", "A"), ("João", "B"), ("Ana", "A")]
    contagem = Counter([v[1] for v in votos])
    print(dict(contagem))

def ex76():
    frase = input("Frase: ").lower()
    cont = Counter(c for c in frase if c.isalpha())
    print(dict(cont))

def ex77():
    return {1: ("Arroz", 10.0), 2: ("Feijão", 8.0)}

def ex78(palavras):
    d = defaultdict(list)
    for p in palavras:
        d[len(p)].append(p)
    return dict(d)

def ex79():
    return {"caneta": (100, 1.5), "lápis": (200, 1.0)}

def ex80():
    dados = [("SP", 30), ("RJ", 32), ("SP", 28)]
    temp = defaultdict(list)
    for cidade, t in dados:
        temp[cidade].append(t)
    return {k: sum(v)/len(v) for k, v in temp.items()}
