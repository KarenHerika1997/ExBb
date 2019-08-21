import json
produtos = []
quantidades = []
categorias = []
contador = 1
bol = True

while bol:
    opcao = int(input('********** CONTROLE DE ESTOQUE ********** \n [1] - Listar Produtos \n [2] - Cadastrar Produtos \n [3] - Excluir Produtos \n [4] - Sair: '))    
    if opcao == 1:
        arquivo = open('ListadeProdutos.json', 'r')
        print(arquivo.read())
    if opcao == 2:
        decisao = input('Deseja adicionar um produto? [S]im ou [N]ão? ').upper()
        while decisao == 'S':
            arquivo = open('ListadeProdutos.json', 'a')
            id = input('Qual o Id do produto? ')
            id = json.dumps(id)
            produto = input('Qual o nome do produto? ')
            produto = json.dumps(produto)
            quantidade = input('Qual a quantidade? ')
            quantidade = json.dumps(quantidade)
            categoria = input('Qual a categoria do produto? ')
            categoria = json.dumps(categoria)
            x = {
                "Id": id ,
                "Produto": produto,
                "Quantidade": quantidade,
                "Categoria": categoria,
            }
            x = str(x)
            arquivo.write(x + "\n")
            arquivo.close()
            decisao = input('Deseja adicionar outro produto? [S]im ou [N]ão? ').upper()

    elif opcao == 3:
        arquivo = open('ListadeProdutos.json', 'r')
        print('   Id-Produto-Qtd-Categoria')
        print(arquivo.read())
        idex = input('Qual item você deseja excluir? ')
        with open(arquivo, 'w') as arq:
            if idex in arq:
                idex = ""
                produto = ""
                quantidade = ""
                categoria = ""
                
    elif opcao == 4:
        bol = False
    if (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
        print('Opção Inválida, Digite novamente! ')