import random
while True:
    #A utilização do 'while True' é pra que após uma rolagem, o programa reinicie automaticamente;facilitando o reuso.
    input('Aperte ENTER para rolar um d20')
    d20 = random.randint(1,20)
    print(d20)
    if d20 == 1:
        print('ERRO CRÍTICO')
    elif d20 == 20:
        print('ACERTO CRÍTICO')
    #Como se tratava de algo simples, decidi usar o 'if' e 'elif' para destacar os erros e acertos críticos. Deixando o código ainda mais completo.
