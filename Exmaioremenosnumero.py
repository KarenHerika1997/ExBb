
def validacao(x):
    try:
        float(num)
        return True
    except:
        pass
    
    return False

def valida_resposta(res):
    if res == 'S':
        return True
    elif res =='N':
        return False
    else:
        return "Inválido"
    
ls = []
val = 0
resposta = 'S'

while resposta == 'S':
    num = input("Digite um número: ")
    n = 0
    if validacao(num) == True:
        num = int(num)
        ls.append(num)
        media = (len(ls))
        soma = (sum(ls))/media
        resposta = input(" Deseja digitar outro número? [S]im ou [N]ão? ").upper()
        while n == 0:
            valida_resposta(resposta)
            if valida_resposta(resposta) ==  True:
                n = 1
            elif valida_resposta(resposta) == False:
                n = 1
            elif valida_resposta(resposta) == "Inválido":
                resposta = input('Valor inválido. Deseja digitar outro número? [S]im ou [N]ão? ').upper()
                if resposta == 'S' or resposta == 'N':
                    n = 1           
    else:
        print('Número inválido')

print(ls)
print('O maior número digitado é o {}. '.format(max(ls)))
print('O menor número digitado é o {}. '.format(min(ls)))
print('A média dos valores da lista é de {}. '.format(soma))
