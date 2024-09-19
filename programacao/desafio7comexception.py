alunos={"rafael":9, "galvao":10, "porto":5, "ryan": 6}

def recuperarNotaAluno(aluno):
    try:
        if aluno in alunos:
            print(f"Sua nota de {aluno} é {alunos[aluno]}")
        else:
            raise KeyError
    except KeyError:
        print("Aluno não está no banco de dados! Tente novamente")

        operacao = input("Deseja tentar novamente? (S/N)")
        if operacao.upper() == "S":
            main()
        elif operacao.upper() == "N":
            print("Programa Finalizado")
        else:
            raise ValueError("Operação não reconhecido")
    except ValueError as ve:
            print(ve)

def main():
    try:
        aluno = input("Qual o seu aluno ")
        recuperarNotaAluno(aluno)
    except Exception as e:
        print(f"Ocorreu um erro: {e}") 

main()