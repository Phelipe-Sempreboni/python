#Neste arquivo, temos exemplos de tipos númericos, conversões e o método (random).

#-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----#

#Notar que deixarei os comandos dentro de uma função, pois não é em todo momento que executaremos esses comandos.
#Caso não queira executar a função, comente ou descomente o comando (tipos_de_valores_concat_convert()).

def tipos_de_valores_concat_convert():
    print('Executando a função de tipos_de_valores_concat_convert()')
    numero_inteiro = 50
    numero_float = 3.597
    numero_complexto = 9j

    x = numero_inteiro
    y = numero_float
    z = numero_complexto

    #Notar que se você utilizar a concatenação com vírgula, não é necessário realizar nenhuma conversão (cast/convert).
    print('O Valor é: ', (x), '//', 'O Tipo é: ', type(x))
    print('O Valor é: ', (y), '//', 'O Tipo é: ', type(y))
    print('O Valor é: ', (z), '//', 'O Tipo é: ', type(z))
    print('\n')

    #Notar que se você utilizar a concatenação com sinal de (+), é necessário realizar conversão (cast/convert).
    print('O Valor é: '+ str(x) + '//' + 'O Tipo é: ' + str(type(x)))
    print('O Valor é: '+ str(y) + '//' + 'O Tipo é: ' + str(type(y)))
    print('O Valor é: '+ str(z) + '//' + 'O Tipo é: ' + str(type(z)))
    print('\n')
tipos_de_valores_concat_convert()

#-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----#


#-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----#

#Iremos utilizar os mesmos comandos acima para verificar as conversões dos tipos de números.
#Caso não queira executar a função, comente ou descomente o comando (conversoes()).

def conversoes():
    print('Executando a função de conversoes()')
    numero_inteiro = 50
    numero_float = 3.597

    x = float(numero_inteiro) #Vamos converter um inteiro para float.
    y = int(numero_float) #Vamos converter um flot par inteiro.

    print('O Valor é: ', (x), '//', 'O Tipo é: ', type(x))
    print('O Valor é: ', (y), '//', 'O Tipo é: ', type(y))
    print('\n')
conversoes()

#-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----#


#-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----#

#Neste caso abaixo, estamos utilizando o método (random) com (randrange), onde geramos números aleatórios de (0 a 61).
#Inserimos em formato (list/array) e geramos 8 posições, todas com geração de numeros entre (0 a 61).
#Mandamos imprimir todas posições e verificamos que os números virão diferentes e a cada execução virá uma nova lista de números.
#Também printamos o tipo dos dados da list/array.

def metodo_random():
    import random
    print('Executando a função de metodo_random()')
    numero_random = [
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
        random.randrange(0,61), #Geração aleatória de números entre (0 e 61) em uma list/array.
    ]

    print('Valor 1: ',numero_random[0])
    print('Valor 2: ',numero_random[1])
    print('Valor 3: ',numero_random[2])
    print('Valor 4: ',numero_random[3])
    print('Valor 5: ',numero_random[4])
    print('Valor 6: ',numero_random[5])
    print('Valor 7: ',numero_random[6])
    print('Valor 8: ',numero_random[7])

    print('Tipo: ', type(numero_random))

metodo_random()
#-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----x-----#