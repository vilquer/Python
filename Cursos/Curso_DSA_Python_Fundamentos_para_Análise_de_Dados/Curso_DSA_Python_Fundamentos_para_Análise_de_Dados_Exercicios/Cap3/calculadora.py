import os

def desenha_tela():
    os.system('cls')
    print('**************************** Calculadora Python! ****************************')
    print('\n')
    print('\n')
    print('*** Escolha uma operação ***')
    print('\n')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('x - Sair')
    print('\n')

def calcula(n1, n2, op):
    n1 = int(n1)
    n2 = int(n2)
    if op == '1':
        return(n1+n2)
    elif op == '2':
        return(n1-n2)
    elif op == '3':
        return(n1*n2)
    elif op == '4':
        return(n1/n2)
    
def entradas(op):
    numero1 = int(input('digite o primeiro valor: '))
    numero2 = int(input('digite o primeiro valor: '))
    return(numero1, numero2, op)
    
def run():
    while True:   
        desenha_tela()
        operacao = input('Escolha uma opção: ')
        if operacao == '1':
            calc = entradas(operacao)
            print('O resultado da operação foi: {}'.format(calcula(calc[0],calc[1],calc[2])))
            input()
        elif operacao == '2':
            calc = entradas(operacao)
            print('O resultado da operação foi: {}'.format(calcula(calc[0],calc[1],calc[2])))
            input()
        elif operacao == '3':
            calc = entradas(operacao)
            print('O resultado da operação foi: {}'.format(calcula(calc[0],calc[1],calc[2])))
            input()
        elif operacao == '4':
            calc = entradas(operacao)
            print('O resultado da operação foi: {}'.format(calcula(calc[0],calc[1],calc[2])))
            input()
        elif operacao == 'x':
            print('**************************** OBRIGADO! ****************************')
            exit()


if __name__ == "__main__":
    run()