import csv

arq = open("lista.csv", "w")
writer = csv.writer(arq)
writer.writerow( ( 'ID', 'Produto','Quantidade', 'Categoria'  ) )
arq.close()

#Inserir novos produtos:


#Validar se o id é do tipo número
num = 0


while num == 0:
    id = int(input(" Qual é o Id do produto? "))
    if id == True:
        arq = open("lista.csv", "a")
        writer = csv.writer(arq)
        writer.writerow( (id))
        arq.close()
        num = 1
    else:
        print("Número inválido, por favor, digite um número válido. ")


#---------------------------------

# produto = input("Qual o produto? ")
# arq = open("lista.csv", "a")
# writer = csv.writer(arq)
# writer.writerow( (produto))
# arq.close()

# #Validar se a quantidade é do tipo número
# while num2 == 0:
#     if num2 == 0:
#         quantidade = int(input("Qual a quantidade? "))
#         arq = open("lista.csv", "a")
#         writer = csv.writer(arq)
#         writer.writerow( (produto))
#         arq.close()
#         num = 1

#     except ValueError:
#         print("Insira um número válido! ") 
# #---------------------------------

# categoria = input("Qual é a categoria? ")
# arq = open("lista.csv", "a")
# writer = csv.writer(arq)
# writer.writerow( (categoria))
# arq.close()
    