def calculadora():#função para iniciar a calculadora pedindo para o usuário selecionar a operação
    operacao = input('''
Por favor escolha o tipo de operação:
+ Adição
- Subtração
* Multiplicação
/ divisão
''')

#variáveis com a entrada do usuário/ números a serem calculados
    numero_1 = int(input('Insira o primeiro numero: '))
    numero_2 = int(input('Insira o segundo numero: '))

###################cadeia de cálculos####################
    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - numero_2)

    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * numero_2)

    elif operacao == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / numero_2)

    else:
        print('você escolheu um valor inválido, reinicie o programa.')

        
########adiciona Again()#####
    again()

def again():
    calc_again = input('''
Voce quer calcular de novo?
Por favor selecione S para SIM ou N para NAO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('ADEUS :) ')
    else:
        again()

calculadora()
