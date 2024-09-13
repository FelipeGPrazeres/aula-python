def saudacao(nome):
    """
    Função que sauda a pessoa
    Input: Nome da pessoa
    Output: saudacao
    """
    print(nome)
nomedapessoa = "Felipe"
saudacao(nomedapessoa)

def calcular(numero1,numero2):
    soma = numero1 + numero2
    subtracao = numero1 - numero2
    return(soma, subtracao)

numero1 = float(input("Digite 1° numero"))
numero2 = float(input("Digite 2° numero"))

valorSoma, valorSubtracao = calcular(numero1, numero2)
print(f"A soma é {valorSoma}")
print(f"A subtracao é {valorSubtracao}")