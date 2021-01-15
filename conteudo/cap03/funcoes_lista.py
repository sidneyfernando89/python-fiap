def listarItens(lista):
    if len(lista) > 0:
        print(f'Os listens da lista são:')
        for itens in lista:
            print(f'{itens}')
    else:
        print('A lista está vazia')

def incluirItem(lista):
    lista.append(informarItem())
    print(f'Item incluído com sucesso')
    return lista

def buscarItens(lista):
    if informarItem() in lista:
        return print('Item encontrado')
    else:
        return print('Item não encontrado')

def removerItem(lista):
    item = informarItem()
    if item in lista:
        lista.remove(item)
        print(f'Operação realizada com sucesso')
    else:
        print(f'Falha ao realizar operação')
    return lista

def atualizarItem(lista):
    item = input('Informe o item a ser atualizado')
    for item in lista:
        if item in lista:
            index = lista.index(item)
            lista[index] = informarItem()

    return lista

def tamanhoLista(lista):
    return print(f'A lista possui {len(lista)} itens')

def informarItem():
    item = input('Informe o item: ')
    return item

def perguntarOpcoes():
    return input('''
            <L> listar itens
            <I> incluir item
            <B> buscar item
            <R> remover item
            <A> atualizar item
            <T> tamanho item
            <E> Sair
            Informa a opção: ''').upper()

def menuAcoes():
    opcao = perguntarOpcoes()
    while opcao != 'E':
        if opcao == 'L':
            listarItens(minha_lista)
            opcao = perguntarOpcoes()
        elif opcao == 'I':
            incluirItem(minha_lista)
            opcao = perguntarOpcoes()
        elif opcao == 'B':
            buscarItens(minha_lista)
            opcao = perguntarOpcoes()
        elif opcao == 'R':
            removerItem(minha_lista)
            opcao = perguntarOpcoes()
        elif opcao == 'A':
            atualizarItem(minha_lista)
            opcao = perguntarOpcoes()
        elif opcao == 'T':
            tamanhoLista(minha_lista)
            opcao = perguntarOpcoes()
        elif opcao == 'E':
            break
        else:
            print(f'O valor informado é invalido')
            opcao = perguntarOpcoes()


minha_lista = []
situacao = False
menuAcoes()

