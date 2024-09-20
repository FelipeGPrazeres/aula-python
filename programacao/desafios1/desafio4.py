listafrutas = ["banana","maca","uva"]
print("Lista de frutas", listafrutas)
adicionar = input("Escolha uma fruta para adicionar ")
listafrutas = listafrutas.append(adicionar)
print("Lista de frutas nova: ", listafrutas)
removerfruta = input("Escolha uma fruta para remover ")

if removerfruta in listafrutas:
    listafrutas = listafrutas.remove(removerfruta)
    print("Lista após remoção: ", listafrutas)
