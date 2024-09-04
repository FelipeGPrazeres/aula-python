#Variáveis do preço
precos = [100,200,300]
multiplicadorDesconto = 0.1
desconto = 0
total = 0
valorFinal = 0

#Soma do total, float para inserção de decimal
total = float(sum(precos))

#IF cálculo do desconto (total*0.1)
if total > 500:
    desconto = total*multiplicadorDesconto

#Cálculo do valor final
valorFinal = total-desconto

#Output do Total, Desconto e Valorfinal
print(f"Total antes do desconto: R$ {total}")
print(f"Desconto aplicado: R$ {desconto}")
print(f"Total com desconto: R$ {valorFinal}")