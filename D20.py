import random
while True:
    input('Aperte ENTER para rolar um d20')
    d20 = random.randint(1,20)
    print(d20)
    if d20 == 1:
        print('ERRO CRÍTICO')
    elif d20 == 20:
        print('ACERTO CRÍTICO')
