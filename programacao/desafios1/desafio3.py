nome = "Felipe Galvão Prazeres"
sobrenome = nome.split()
verificarnome = (len(nome))
if verificarnome > 1:
    print(sobrenome[-1])
else:
    print("Coloque seu nome completo por favor")