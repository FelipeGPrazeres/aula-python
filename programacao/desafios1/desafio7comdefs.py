alunos={"rafael":9, "galvao":10, "porto":5, "ryan": 6}

def recuperarNotaAluno(aluno):
    if aluno in alunos:
        print(f"Sua nota de {aluno} é {alunos[aluno]}")
    else:
        print("Aluno não está no banco de dados! Tente novamente")

        operacao = input("Deseja tentar novamente? (S/N)")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa Finalizado")
        else:
            print("Operação não reconhecida! O programa irá finalizar")

def main():
    aluno = input("Qual o seu aluno ")

    recuperarNotaAluno(aluno)

main()