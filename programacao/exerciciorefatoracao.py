#Variáveis do preço
precosProdutos = [100,200,300]
#Soma do total, float para inserção de decimal
totalPreco = float(sum(precosProdutos))
print(f"Total antes do desconto: R$ {totalPreco}")
#IF cálculo do desconto (total*0.1)
if totalPreco > 500:
    totalPreco = totalPreco - (totalPreco*0.1)
#Output do Total, Desconto e Valorfinal
    print(f"Total com desconto: R$ {totalPreco}")
else:
    diferenca = 500 - totalPreco
    print(f"Adicione mais {diferenca} em produtos para ganhar um desconto de 10%!")