numero = int(input("Qual o número? "))
def verEnt(numero):
    if numero > 0:
        return "Seu número é positivo"
    elif numero < 0:
        return "Seu número é negativo"
    else:
        return "Seu número é zero"
print(verEnt(numero))