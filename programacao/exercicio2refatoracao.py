#Variáveis definidas
idade = int(input("Qual sua idade? "))
categoria = "Indefinada"

#Validação da idade da pessoa para analisar sua categoria
def validarIdade(idade):
    mensagemPadrão = "A pessoa é classificada como: "
    #Definir como criança caso idade for menor de 13
    if idade < 0:
        return "Essa pessoa já nasceu?"
    elif idade > 0 and idade < 13:
        return mensagemPadrão + "Criança"

    #Definir como adolescente caso idade for menor de 18 e maior de 13
    elif idade >= 13 and idade < 18:
        return mensagemPadrão + "Adolescente"

    #Definir como adulto caso idade for maior de 18 e menor de 60
    elif idade >= 18 and idade < 60:
        return mensagemPadrão + "Adulto"

    #Definir como idoso caso idade for maior de 60
    elif idade >= 60 and idade <120:
        return mensagemPadrão + "Idoso"
    else:
        return mensagemPadrão + "Fossil"
#Chamar função para definir categoria à variável
categoriaIdade = validarIdade(idade)
#Printar categoria resultante
print(categoriaIdade)