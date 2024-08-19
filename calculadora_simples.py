def calculadora():
    
    numero_1 = float(input("insira o primeiro número: "))

    operacao = input(
      '''escolha a operação a ser utilizada:
      + somar
      - subtrair
      * multiplicar
      / dividir
      ''')
    
    numero_2 = float(input("insira o segundo número: "))

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
    
    reiniciar()

def reiniciar():
    reinicio = input('''quer calcular de novo?
                     pressione 'S' para SIM
                     pressiona 'N' para NÃO
                     ''')
    if reinicio == 's':
        calculadora()

    elif reinicio == 'n':
        print("Adeus")

    else:
        reiniciar()

calculadora()
