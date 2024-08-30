dia = 28
idademin = 14
idademax = 17
verf = True
pdia = int(input("Dia da inscrição "))
pidade = int(input("Idade do atleta "))
pindicacao = (input("Tem indicação? "))
pespera = (input("Está na lista de espera? "))
if (pdia <= dia == True) or (pindicacao == "Sim" and pdia ==29):
    print("Sua inscrição está dentro do período \n")
    if pidade >= idademin or pidade <= idademax:
        print("Você tem a idade necessária \n")
        if not pespera == "Sim":
            print("Você não está na lista de espera \n")
            print("Parabéns sua inscrição foi realizada \n")
if pespera == "Sim":
    print("Inscrições da lista de espera não estão sendo mais aceitas \n")
    verf = False
if pidade < idademin:
    print("Você é menor que a idade minima \n")
    verf = False
if pidade > idademax:
    print("Você é maior que a idade máxima \n")
    verf = False
if (pdia > 28) and (pindicacao == "Não"): 
    print("Você está fora do período de inscrição e não tem indicação \n")
    verf = False
if verf == False:
    print("Não foi possivel realizer sua inscrição \n")