def maiuscula(stringinput):
    stringmaiuscula = stringinput.upper()
def minuscula(stringinput):
    stringminuscula = stringinput.lower()
def qttcaracteres(stringinput):
    quantidadeCaracteres = len(stringinput)
def main():
    stringinput = input("Digite a string ")
    print(f"Maiusculas {maiuscula}, Minuscula {minuscula}, quantidade de letras {qttcaracteres}")
main()