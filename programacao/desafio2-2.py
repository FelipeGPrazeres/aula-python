operacoesPossiveis = ["+","-","*","/"]
def soma(a,b):
    """
    Realiza a soma dos valores 1 e 2
    """
    return a + b

def subtracao(a,b):
    """
    Realiza a subtração dos valores 1 e 2
    """
    return a - b

def multiplicacao(a,b):
    """
    Realiza a multiplicação dos valores 1 e 2
    """
    return float(a * b)

def divisao(a,b):
    """
    Realiza a divisão dos valores 1 e 2
    """
    return float(a / b)

def main():
    valor1 = float(input("Digite o primeiro número: "))
    valor2 = float(input("Digite o segundo número: "))
    tipoOperacao = input("Qual o tipo de operação? (+,-,*,/)")
    if tipoOperacao not in operacoesPossiveis:
        print("Sua operação não existe!")
    if not isinstance(valor1, str) or isinstance(valor2, str):
        if tipoOperacao == "+":
            print(f"A soma desses valores é {soma(valor1,valor2)}")
        elif tipoOperacao == "-":
            print(f"A subtração desses valores é {subtracao(valor1,valor2)}")
        elif tipoOperacao == "*":
            print(f"A multiplicação desses valores é {multiplicacao(valor1,valor2)}")
        elif tipoOperacao == "/":
            if valor2 == 0:
                print("Divisão por 0 não é possível!")
            else:print(f"A divisão desses valores é {divisao(valor1,valor2)}")
    else:
        print(isinstance(valor1, str))
        print(isinstance(valor2, str))
        print("Um dos valores é inválido!")
        
main()