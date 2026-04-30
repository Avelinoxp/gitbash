# #While condição:
# #bloco de código
# contador = 1

# while contador <= 10:
#     print(contador)
#     if contador == 5:
#         break
#     contador += 1
# #Break exemplo senha
# senha = ""
# while True:
#     senha = input('Digite a senha: ')
    
#     if senha =="1234":
#         print('Acesso liberado')
#         break

#     print('Senha incorreta')
#     #Usamos while True: quando
# # queremos que o programa
# # continue rodando até
# # acontecer algo dentro dele,
# # normalmente usando break.

# #Continue pular número 2
# numero = 1
# while numero <= 5:
#     if numero == 2:
#         numero += 1
#         continue

#     print(numero)
#     numero += 1
#     # Pular número 2

#     #Continue
# #     O continue pula o restante do código daquela repetição e volta para o início do
# # laço.
# contador = 0
# while contador < 10:
#     contador += 1
#     if contador % 2 == 0:
#         continue

#     print(contador)
#     #EXCELENTE EXEMPLO PARA AULA
#     numero = 0
#     while numero < 10:
#         numero += 1
#         if numero == 3:
#             continue
#         if numero == 8:
#             break

#         print(numero)
#Questão 1
#Mostre números de 1 a 10, mas pare no 6.

# contador = 1
# while contador <= 10:
#     print(contador)
#     if contador == 6:
#          break
#     contador += 1
#2 Mostre números de 1 a 10, pulando o número 5.
# numero = 1
# while numero <=10:

#     if numero == 5:
#         numero += 1
#         continue
#     print(numero)
#     numero+= 1
#3 Questão  Mostre números de 1 a 20, pulando pares e encerrando no 15.
# numero = 1
# while numero <= 20:
#     if numero == 17:
#         break
#     if numero % 2 == 0:
#         numero+= 1
#         continue
#     print(numero)
#     numero+= 1
#4 Atividade
# while True: 
#     produto =input('Digite o produto: ')
#     if produto == 'fim':
#         print('Cadastro finalizado')
#         break
#     print('Produto cadastrado', produto)

#5 Parar quando soma chegar em 20
# soma = 0
# while True:
#     numero = int(input('Digit um número: '))
#     soma += numero

#     if soma >= 20:
#         break
     
# print('Total: ', soma)

# Atividade 6 – Parada por Limite
# Crie um sistema que receba números digitados pelo usuário e vá somando os
# valores informados.
# Quando a soma total atingir ou ultrapassar 50, o programa deverá encerrar
# automaticamente utilizando o comando break.
# soma = 0
# while True:
#     numero = int(input('Digite um número:'))
#     soma += numero
#     if soma >= 50:
#         print( 'Limite atingido!')
#         print('Total', soma)
#         break

#Atividade 7
# while True:
#     senha = input('Digite sua senha:')

#     if senha == 'teste':
#         print('Acesso Liberado')
#         break
#     else:
#         print('Senha incorreta')

