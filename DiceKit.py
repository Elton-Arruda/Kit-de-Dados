#Após fazer o código com o D20, senti que poderia ir mais além e contemplar os dados mais utilizados nos rpgs; aqueles que formam o Kit de dados.
import random
while True:
  dado = input('Qual dado você deseja rodar? ')
  match dado:
#De início, montei o código me utilizando apenas de 'if', 'elif' e 'else'; mas após um pesquisa, vi que o match case poderia diminuir as linhas utilizadas e deixar o código mais elegante.
    case "d20":
      d20 = random.randint(1, 20)
      print(d20)
      if d20 == 1:
        print('ERRO CRÍTICO')
      elif d20 == 20:
        print('ACERTO CRÍTICO')
#O acerto e erro crítico foram preservados - com o intuito de guardar a essência do dado.
    case "d12":
      d12 = random.randint(1, 12)
      print(d12)
    case "d10":
      d10 = random.randint(1, 10)
      print(d10)
    case "d8":
      d8 = random.randint(1, 8)
      print(d8)
    case "d6":
      d6 = random.randint(1, 6)
      print(d6)
    case "d4":
      d4 = random.randint(1, 4)
      print(d4)
    case _: print('Não foi possível encontrar o seu dado!')
#Ao mesmo tempo em que a última linha preserva o propósito do código - impedindo que o funcionamento seja afetado com digitações inesperadas -, também notifica quem utiliza.
