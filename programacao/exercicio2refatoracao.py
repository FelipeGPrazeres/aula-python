#Variáveis definidas
idade = int(input("Qual sua idade?"))
categoria = "Indefinada"

#Definir como criança caso for menor de 13
if idade < 13:
    categoria = "Criança"

#Definir como adolescente se for menor de 18 e maior de 13
elif idade >= 13 and idade < 18:
    categoria = "Adolescente"

#Definir como adulto se for maior de 18 e menor de 60
elif idade >= 18 and idade < 60:
    categoria = "Adulto"

#Definir como idoso se for maior de 60
else:
    categoria = "Idoso"
    
#Printar categoria resultante
print(f"Você é classificada como: {categoria}")