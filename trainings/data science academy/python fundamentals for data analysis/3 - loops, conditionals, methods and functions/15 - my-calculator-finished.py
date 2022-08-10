# Variáveis com as mensagens que serão impressas na tela no início do programa informando as opções disponíveis.
message_sum = '1 - Soma'
message_subtraction = '2 - Subtração'
message_multiplication = '3 - Multiplicação'
message_division = '4 - Divisão'

# Mensagem que será impressa no início do programa.
print('****************************** Python Calculator ******************************\n')

# Mensagem que será impressa no início do programa.
print('Selecione o número da opção desejada:\n')

# Mensagens que serão impressas no início do programa.
print(message_sum)
print(message_subtraction)
print(message_multiplication)
print(message_division)

# Este comando (\n) é para que seja pulado uma linha.
print('\n')

# Variável com o input da mensagem solicitando que o usuário digite a opção desejada.
message = int(input('Digite sua opção (1/2/3/4): '))

# Este comando (\n) é para que seja pulado uma linha.
print('\n')

# Estrutura condicional com if para caso seja escolhida a opção 1.
# A opção 1 é a escolha para quando o usuário quiser realizar uma soma.
if message == 1:
    
    # Variável que irá solicitar ao usuário que seja inserido o primeiro número da operação matemática.
    a = int(input('Digite o primeiro número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')

    # Variável que irá solicitar ao usuário que seja inserido o segundo número da operação matemática.
    b = int(input('Digite o segundo número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')
    
    soma = a + b
    
    print(a, ' + ', b, ' = ', soma)

# Estrutura condicional com elif para caso seja escolhida a opção 2.
# A opção 1 é a escolha para quando o usuário quiser realizar uma subtração.
elif message == 2:
    
    # Variável que irá solicitar ao usuário que seja inserido o primeiro número da operação matemática.
    c = int(input('Digite o primeiro número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')

    # Variável que irá solicitar ao usuário que seja inserido o segundo número da operação matemática.
    d = int(input('Digite o segundo número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')
    
    subtracao = c - d
    
    print(c, ' - ', d, ' = ', subtracao)

# Estrutura condicional com elif para caso seja escolhida a opção 3.
# A opção 1 é a escolha para quando o usuário quiser realizar uma multiplicação.
elif message == 3:
    
    # Variável que irá solicitar ao usuário que seja inserido o primeiro número da operação matemática.
    e = int(input('Digite o primeiro número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')

    # Variável que irá solicitar ao usuário que seja inserido o segundo número da operação matemática.
    f = int(input('Digite o segundo número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')
    
    multiplicacao = e * f
    
    print(e, ' * ', f, ' = ', multiplicacao)

# Estrutura condicional com elif para caso seja escolhida a opção 4.
# A opção 1 é a escolha para quando o usuário quiser realizar uma divisão.
elif message == 4:
    
    # Variável que irá solicitar ao usuário que seja inserido o primeiro número da operação matemática.
    g = int(input('Digite o primeiro número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')

    # Variável que irá solicitar ao usuário que seja inserido o segundo número da operação matemática.
    h = int(input('Digite o segundo número: '))

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')
    
    divisao = g / h
    
    print(g, ' / ', h, ' = ', divisao)

# Comando else para caso a opção inserida seja diferente das opções disponíveis.
# Neste caso será informando a mensagem abaixo e o programa será finalizado.
else:

    # Imprimir na tela a mensage abaixo.
    print('Opção inválida!')

    # Este comando (\n) é para que seja pulado uma linha.
    print('\n')