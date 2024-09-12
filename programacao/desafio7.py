alunos={"rafael":9, "galvao":10, "porto":5, "ryan": 6}
nome = input("Qual o seu nome ")
if nome in alunos:
    if nome == "rafael":
        print(f"Sua nota é {alunos['rafael']}")
    if nome == "galvao":
        print(f"Sua nota é {alunos['galvao']}")
    if nome == "porto":
        print(f"Sua nota é {alunos['porto']}")
    if nome == "ryan":
        print(f"Sua nota é {alunos['ryan']}")
else:
    print("Aluno não está no banco de dados")