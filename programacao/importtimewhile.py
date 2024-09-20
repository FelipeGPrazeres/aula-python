# import time
# import webbrowser
# dia = 5
# while dia > 0:
#     print(dia)
#     time.sleep(1)
#     dia -= 1
# print("Feliz Lula novo!")
# condicao = input("Quer testar a senha? S/N ")
# if condicao == "S":
#     contaNome = input("Digite seu nome ")
#     senhaCerta = input("Digite sua senha ")
#     senha = ""
#     nome = ""
#     while senha != senhaCerta and nome != contaNome:
#         nome = input("Digite o nome ")
#         senha = input("Digite a senha ")
#     print("Acesso permitido!")
#     webbrowser.open("https://www.youtube.com/shorts/ShBtK1eYacY")

# for i in range(6):
#     if i % 2 == 0:
#         continue
#     print("Ímpar ", i)

bandeiras = {54: "MasterCard", 53: "Visa", 33: "Elo", 22: "Alelo"}
digito = None

while True:
    try:
        digito = int(input("Digite um número (ou digite -1 para sair): "))

        if digito == -1:
            print("Saindo do programa.")
            break
        
        if digito in bandeiras:
            print(f"A bandeira correspondente é: {bandeiras[digito]}")
            break
        else:
            print("Número inválido. Tente Novamente")
    except ValueError as vr:
        print("Não foi digitado um valor inteiro! Tente novamente")
    except Exception as e:
        print("Erro :: ", e)
