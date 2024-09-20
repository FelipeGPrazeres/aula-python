def adicionarContato1(contatos,pessoa):
    contatos.append(pessoa)
    return contatos

def verificarQuantidade(contatos):
    qttContatos = len(contatos)
    return qttContatos

def main():
    contatos = []
    pessoa1 = {"nome": "Alice", "telefone": "123-456-789"}
    pessoa2 = {"nome": "Bob", "telefone": "987-654-321"}

    print(f"Atualmente há {verificarQuantidade(contatos)} pessoas")
    adicionarContato1(contatos,pessoa1)
    print(f"Atualmente há {verificarQuantidade(contatos)}")
    print(f"Os contatos presentes são: {contatos}")
    adicionarContato1(contatos,pessoa2)
    print(f"Atualmente há {verificarQuantidade(contatos)}")
    print(f"Os contatos presentes são: {contatos}")
main()