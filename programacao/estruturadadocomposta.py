print("Listas \n")
#Exemplo de listas
frutas = ["maçã", "banana", "laranja"]
print("Lista de frutas:", frutas)
#Adicionando um item
frutas.append("uva")
print("Lista de frutas atualizada:", frutas)
#Acessando um item
print("Primeira fruta:", frutas[0])
#Removendo um item
frutas.remove(frutas[1])
print("Lista nova:", frutas)

print("Dicionários \n")
#Exemplo com dicionários/objeto
pessoa = {"nome": "Ana", "idade": 30}
print("Pessoa:", pessoa)
#Acessando valores
print("Nome:", pessoa["nome"])
#Adicionando um novo par chave-valor
pessoa["cidade"] = "São Paulo"
print("Pessoa atualizada", pessoa)

print("Dicionários dentro de dicionários \n")
#dicionario dentro dicionario
pessoa2 = {"nome2": "Brenda", "idade2": 26, "filhos":{"nome2": "Catarina", "idade2": 6}}
print(pessoa2)
print(pessoa2["nome2"])
print(pessoa2["filhos"])
print(pessoa2["filhos"]["nome2"])
#deletando valor do dicionário
del pessoa2["filhos"]
print(pessoa2)

print("Dicionário dentro de lista \n")
#Dicionário dentro de variável
#Definição da lista e dissionário
listaPessoas = []
pessoa3 = {"nome3": "Ana", "idade3": 32}
#Adicionando dicionário dentro da variável
listaPessoas.append(pessoa3)
print(listaPessoas)
#Adicionando mais um dicionário a lista
pessoa3 = {"nome3": "Brenda", "idade3": 26}
listaPessoas.append(pessoa3)
print(listaPessoas)
#Mais um
pessoa3 = {"nome3": "Fernanda", "idade3": 48}
listaPessoas.append(pessoa3)
print(listaPessoas)
#Analisando o dicionário de índice 1 da lista
brenda = listaPessoas[1]
print(brenda)

print("Tuplas \n")
#tupla x = 10 y = 30 z = 20
tupla = (10,20)
print(tupla)
tupla = (tupla[0], 30, tupla[1])
print(tupla)
#x = 10 y = 30 z = 30
tupla = (10,20,30)
print(tupla)
novoIndice = 30
tupla = (tupla[0], novoIndice, tupla[1])
print(tupla)

print("Conjuntos \n")
#conjunto eliminando duplicados
lista = [1,2,2,3,4,4]
conjunto = set(lista)
print(conjunto)

print("Conjuntos e suas operações \n")
#Conjuntos e suas operações
a = {1,2,3}
b = {3,4,5}
print(a&b)
print(a|b)
print(a-b)

print("Verificação no conjunto \n")
conjunto = {1,2,3,4,5}
print(3 in conjunto)
print(6 in conjunto)