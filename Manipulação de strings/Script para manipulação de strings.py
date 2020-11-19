#exemplos abaixo com alguns comandos úteis para manipulação de strings.

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo de seleção das posições de uma string, que é como uma list/array.
#É possível selecionar a posição dos elementos conforme exemplo abaixo.

def selecionar_posicoes():
    print('\n')
    print('Executando a função (posicoes()')
    empresa = 'Sociedade Brasileira de Programação'

    print(empresa)
    print(empresa[0:9])
    print(empresa[10:20])
    print(empresa[21:23])
    print(empresa[24:35])
    print('\n')

selecionar_posicoes()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo para contabilizar tamanho da string com comando (len).

def tamanho_string():
    print('Executando a função tamanho_string()')
    empresa = 'Sociedade Brasileira de Programação'

    print('O tamanho da strin é: ',len(empresa))
    print('\n')
    
tamanho_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo de substituição de uma parte da string por outra palavra/elemento com o comando (replace).

def substituicao_string():
    print('Executando a função substituicao_string()')
    empresa = 'Sociedade Brasileira de Programação'

    print(empresa.replace('Sociedade', 'Associação'))
    print('\n')

substituicao_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo de conversão da string para letras maiusculas.

def conversao_para_maiuscula_string():
    print('Executando a função conversao_para_maiuscula_string()')
    empresa = 'Sociedade Brasileira de Programação'

    print(empresa.upper())
    print('\n')

conversao_para_maiuscula_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo de conversão da string para letras minusculas.

def conversao_para_minuscula_string():
    print('Executando a função conversao_para_minuscula_string()')
    empresa = 'Sociedade Brasileira de Programação'

    print(empresa.lower())
    print('\n')

conversao_para_minuscula_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo do comando strip que nos auxiliar a retirar espaços no começo e final de uma determinada string.

def retirar_espacos_inicio_final_string():
    print('Executando a função retirar_espacos_inicio_final_string()')
    empresa = '  Sociedade Brasileira de Programação  '

    print(empresa)
    print(empresa.strip())
    print('\n')

retirar_espacos_inicio_final_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo do comando split, onde ele 'corta' ou 'interrompe' uma string dependendo do parametro que você utilziar, por exemplo, espaços, barras, etc.

def interromper_string():
    print('Executando a funçãointerromper_string()')
    empresa = 'Sociedade Brasileira de Programação'

    x = empresa.split(' ') #Aqui pode ser vírgula, ponto e vírgula, barra, etc.
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])

    print(empresa.split(" "))

interromper_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

