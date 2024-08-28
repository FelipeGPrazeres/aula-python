a = 2
b = 6
c = 3
operacaoAnd = a == b and c*a == b
print(f"Operação 1 AND {operacaoAnd}")
operacaoOr = a == b or c*a == b
print(f"Operação 1 OR {operacaoOr}")
print("###########################")
operacaoAnd = a == (c+b) and b == c
print(f"Operação 2 AND {operacaoAnd}")
operacaoOr = a == (c+b) or b == c
print(f"Operação 2 OR {operacaoOr}")
print("###########################")
operacaoAnd = a > 5 and b<3 == b
print(f"Operação 3 AND {operacaoAnd}")
operacaoOr = a > 5 or b<3 == b
print(f"Operação 3 OR {operacaoOr}")
print("###########################")
operacaoAnd = a < 5 and c>=3
print(f"Operação 4 AND {operacaoAnd}")
operacaoOr = a < 5 or c>=3
print(f"Operação 4 OR {operacaoOr}")
print("###########################")
operacaoAnd = not b == 6 and 3*2 == b
print(f"Operação 5 AND {operacaoAnd}")
operacaoOr = not b == 6 or 3*2 == b
print(f"Operação 5 OR {operacaoOr}")
print("###########################")
operacaoAnd = c<5 and not b > 6
print(f"Operação 6 AND {operacaoAnd}")
operacaoOr = c<5 or not b > 6
print(f"Operação 6 OR {operacaoOr}")