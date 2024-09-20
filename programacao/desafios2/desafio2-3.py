def manipularString(stringinput):
    stringmaiuscula = stringinput.upper()
    stringminuscula = stringinput.lower()
    quantidadeCaracteres = len(stringinput)
    return (stringmaiuscula, stringminuscula, quantidadeCaracteres)

def main():
    stringinput = input("Digite a string ")
    resultadoMaiuscula, resultadoMinuscula, resultadoCaracteres = manipularString(stringinput)
    print(f"Sua palavra em maiusculo: {resultadoMaiuscula}")
    print(f"Sua palavra em minusculo: {resultadoMinuscula}")
    print(f"Totais de caracteres da sua palavra: {resultadoCaracteres}")
main()