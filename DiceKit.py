import random
while True:
  dado = input('Qual dado você deseja rodar? ')
  match dado:
    case "d20":
      d20 = random.randint(1, 20)
      print(d20)
      if d20 == 1:
        print('ERRO CRÍTICO')
      elif d20 == 20:
        print('ACERTO CRÍTICO')
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
