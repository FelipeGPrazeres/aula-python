a = 5
b = 3
c = 4

# Adição (+)
resultado = a + b + c
print(f"Soma: {resultado}")
print("####################")
#Subtração (-)
resultado = c - b
print(f"Subtração : {resultado}")
print("####################")
#Multiplicação (*)
resultado = c * b
print(f"Multiplicação : {resultado}")
print("####################")
#Divisão (/)
resultado = c / b
print(f"Divisão : {resultado}")
print("####################")
#Divisão Inteira (//)
resultado = c // b
print(f"Divisão Inteira : {resultado}")
print("####################")
#Resto da Divisão (%)
resultado = c % b
print(f"Resto da Divisão : {resultado}")
print("####################")
#Expoente (**)
resultado = c ** b
print(f"Expoente : {resultado}")
print("####################")
#Texto
resultado = "vi" + "ado"
print(f"Texto : {resultado}")
print("####################")
saldoIni = 50
custorefri = 8
custopao = 4
dela = 39.90

valorFim = (custorefri*2) + custopao + ((dela / 1000)* 300)

saldoFinal = saldoIni - valorFim
print(f"José chegou com R${saldoIni} e saiu com R${saldoFinal}")

dia = int(input("Qual o dia de hoje?"))
ppizza = int(input("Comprou quantas pizzas?"))
pbeb = int(input("Comprou quantas bebidas?"))
pbol = int(input("Comprou quantos bolos?"))
pdoc = int(input("Comprou quantas gramas de doce?"))
diaFesta = 26
pizzamin = 10
bebmin = 12
bolomin = 5
docemin = 600
print("################################################ \n")
if diaFesta == dia:
    print(" Ana está fazendo as compras no dia da festa \n")
else:
    print("Ana não está fazendo as compras no dia da festa \n")
print("################################################ \n")
if(pizzamin > ppizza):
    print("Ana não comprou pizzas suficientes \n")
else:
    print("Ana comprou pizzas suficientes \n")
print("################################################ \n")
if(bebmin > pbeb):
    print("Ana não comprou bebidas suficientes \n")
else:
    print("Ana comprou bebidas suficientes \n")
print("################################################ \n")
if(bolomin > pbol):
    print("Ana não comprou bolos suficientes \n")
else:
    print("Ana comprou bolos suficientes \n")
print("################################################ \n")
if(docemin > pdoc):
    print("Ana não comprou doces suficientes \n")
else:
    print("Ana comprou doces suficientes \n")
print("################################################ \n")