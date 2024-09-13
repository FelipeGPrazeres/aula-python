alunos={"rafael":9, "galvao":10, "porto":5, "ryan": 6}
nome = input("Qual o seu nome ")
if nome in alunos:
    print(f"Sua nota de {nome} é {alunos[nome]}")
else:
    print("Aluno não está no banco de dados")