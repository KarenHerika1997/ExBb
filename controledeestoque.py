produtos = []
quantidades = []
categorias = []
contador = 1
bol = True

while bol:
    opcao = int(input('********** CONTROLE DE ESTOQUE ********** \n [1] - Listar Produtos \n [2] - Cadastrar Produtos \n [3] - Excluir Produtos \n [4] - Sair: '))    
    if opcao == 2:
        decisao = input('Deseja adicionar um produto? [S]im ou [N]ão? ').upper()
        while decisao == 'S':
            arquivo = open('ListadeProdutos.txt', 'a', newline="")
            contstr = str(contador)
            arquivo.write('   ' + contstr + '   ')
            produto = input('Qual o nome do produto? ')
            arquivo.write(produto + '   ')
            quantidade = input('Qual a quantidade? ')
            arquivo.write('   ' + quantidade + '   ' )
            categoria = input('Qual a categoria? ')
            arquivo.write(categoria + "\n")
            decisao = input('Deseja adicionar outro produto? [S]im ou [N]ão? ').upper()
            contador = contador + 1
            arquivo.close()
    if opcao == 1:
            arquivo = open('ListadeProdutos.txt', 'r')
            print(arquivo.read())
    elif opcao == 3:
        arquivo = open('ListadeProdutos.txt', 'r')
        print('Posição atual no arquivo: ' + arquivo.tell())
        # print(arquivo.read())
        # index = int(input('Qual item deseja excluir? '))
        # print(arquivo.read(index))
        # for line in arquivo('ListadeProdutos.txt'):
        #     if index in line:
        #         print(line)
        # itemexcluido = produtos.pop(index)
        # print('O produto {} foi excluído com sucesso. '.format(itemexcluido))
    elif opcao == 4:
        bol = False
    if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
        print('Opção Inválida, Digite novamente! ')