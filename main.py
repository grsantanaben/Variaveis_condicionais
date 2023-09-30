#Segundo sabado - Aula3 Concatenação
#age = input('Digite sua idade: ')
#name = input ('Digite seu nome: ')
#compras = float(input('Digite suas compras do mes: '))
#compras2 = float(input('Digite suas compras do mes anterior: '))
#print ('Nome', name,'', 'Idade', age,'', 'Soma das compras:', compras + compras2,'')

#n1 = int(input ('Digite um numero: '))
#n2 = int(input ('Digite outro numero: '))
#op = 'soma:'
#print (op, 'n1' + 'n2')

##### EXERCICIOS #####
### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

#2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

#3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

#4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

#5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.

#6 - Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".**

#7 - Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.**

#8 - Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.**

#9 - Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.**

          #Exercicio 1
# numint = int(input('Digite um número inteiro:'))
# result = numint*numint
# print("Esse é o quadro do numero digitado ",result)

          #Exercicio 2
# nome1 = "Gabriel"
# nome2 = "Rodrigues"
# print ("Essa é a junção dos nomes: ", nome1,"" + nome2)

          #Exercicio 3 (String, vai apresentar o texto)
# n1 = (input("Digite um número: "))
# n2 = (input("Digite outro número: "))
# print ("Os numeros digitados foram: ", n1,n2 )

          #Exercicio 4
# linguagem = "Python"
# num = int(input("Digite um numero: "))
# print(linguagem,"", num)


                            ##Format
# nome = input("Qual é o seu nome -")
# idade = input("Qual a sua idade -")
# endereco = input("Qual é o seu endereco -")
# cargo = input("Qual é o seu cargo -")
# print(f"Meu nome é {nome}, Minha idade é {idade}, Meu endereço é {endereco}, Meu cargo é {cargo}")


           #Exercicio 5.
# frase = "Dia de muita aula"
# palavra = input("Digite uma palavra ")
# #print(palavra,",",frase)
# print (f"Minha frase ficou assim: {frase},{palavra}\n")


          #Exercicio 6
# hora = int(input("Digite o horário: "))
# min = int(input("Digite quantos minutos tem a hora: "))
# seg = int(input("Digite os segundos: "))
# #print ('hh:',hora,'mm:',min,'ss:',seg)
# print (f"Hora:{hora},Min:{min},Seg:{seg}\n")

          #Exercicio 7
# ddd = int(input("DDD: "))
# tel = int(input("Telefone: "))
# #print ("Telefone completo", ddd,tel)
# print (f"DDD:{ddd},Telefone:{tel}\n")

          #Exercicio 8
# i1 = "ovos"
# i2 = "leite"
# i3 = "farinha"
# i4 = "manteiga"
# i5 = "fermento"
# print (f"Ingredientes usados {i1,i2,i3,i4,i5}\n")
#print ("Os ingredientes da receita de bolo são esses: ", i1,i2,i3,i4,i5,)

#Exercicio 9
# adj1 = input("Digite a sua primeira impressão sobre a aula: ")
# adj2 = input("O que esta achando neste momento: ")
# adj3 = input("Chegamos ao fim da aula, qual a sua visão: ")
# print (f"A primeira impressão que tive, achei {adj1}, e com o passar do tempo mudei de idéia e esta {adj2},no final eu conclui que é {adj3}\n")



                        #ATIVIDADE 3 → IF()
#1 - Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?**
#2 - Crie um sistema para permitir a verificação de menores em um show**
#3 - Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if() ** para verificar se o aluno passou.**

#Exemplo:
# senha_digitada = input("Digite uma senha: ")
# nome = input("Digite seu nome: ")
# senha = '1234'
# if senha == senha_digitada and nome == 'Bianca':
#   print ("Acesse liberado")
# else:
#   print(f"Acesso negado, você digitou {senha} ou {nome} incorretamente")


          #Exercicio 1 - IF
# id = 18
# id1 = 45
# idade = float(input("Escolha um dos numeros: 18 ou 45? "))
# if id  ==  idade:
#   print (f"Você escolheu o menor valor: {id}")
# else:
#   print(f"Você escolheu o maior valor?: {id1} ")

          #Exercicio 2 - IF
# maior = 18
# idade_declarada = int(input("Qual sua idade? "))
# if idade_declarada < maior:
#    print ("Você não pode entrar no show.")
# else: 
#   print (f"Permitido a entrada no show, você tem {maior} anos")
          
        #Exercicio 3 - IF
nt1 = float(input("Nota de Português: "))
nt2 = float(input("Nota de Matemática: "))
nt3 = float(input("Nota de Ed. Fisica: "))
media = (nt1+nt2+nt3)/3
if media >= 7:
  print(f"Aluno aprovado {media}")
else:
  print(f"Reprovado {media}")