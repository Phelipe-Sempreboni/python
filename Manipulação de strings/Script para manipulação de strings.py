#Exemplos abaixo com alguns comandos úteis para manipulação de strings.

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
    print('Executando a função interromper_string()')
    empresa = 'Sociedade Brasileira de Programação'

    x = empresa.split(' ') #Aqui pode ser vírgula, ponto e vírgula, barra, etc.
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])

    print(empresa.split(" "))
    print('\n')

interromper_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo da utilização do comando in, que server para verificar se certa clausula contém em determinado resultado. Se houver devolverá o comando True, caso contrário devolverá False.
#No exemplo abaixo, faremos ocorrer o True e o False.
#Cuidado na utilização da escrita da string no comando, pois, caso não esteja igual a strin da variável, ocorrerá execução incorreta do comando. O Python é sensitive case, ou seja, diferencia maiuscula de minuscula.

def comando_in():
    print('Executando a função comando_in()')
    empresa = 'Sociedade Brasileira de Programação'

    resultado = 'Brasileira' in empresa #Existe na variável empresa a string 'Brasileira'.
    print(resultado) 

    resultado_2 = 'Empresa' in empresa #Não existe na variável empresa a string 'Empresa'.
    print(resultado_2)
    print('\n')

comando_in()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo da utilização do comando not in, que server para verificar se certa clausula não contém em determinado resultado. Se não houver devolverá o comando True, caso contrário devolverá False.
#No exemplo abaixo, faremos ocorrer o True e o False.
#Cuidado na utilização da escrita da string no comando, pois, caso não esteja igual a strin da variável, ocorrerá execução incorreta do comando. O Python é sensitive case, ou seja, diferencia maiuscula de minuscula.

def comando_not_in():
    print('Executando a função comando_not_in()')
    empresa = 'Sociedade Brasileira de Programação'

    resultado = 'Brasileira' not in empresa #Existe na variável empresa a string 'Brasileira'. False.
    print(resultado) 

    resultado_2 = 'Empresa' not in empresa #Não existe na variável empresa a string 'Empresa'. True.
    print(resultado_2)
    print('\n')

comando_not_in()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo para concatenação de strings.

def concatenacao_string():
    print('Executando a função concatenacao_string()')
    empresa = 'Sociedade Brasileira de Programação'
    logradouro = 'Rua Abreu Mesquia, 5053, Alto da Lapa, São Paulo - SP'

    #comando normal.
    print(empresa)
    print(logradouro)

    #Comando com concatenção usando vírgula.
    #Com o comando utilizando vírgula não é necessário fazer conversões como inteiro para string.
    print('A empresa',empresa, 'está lolizada no endereço', logradouro,'.')

    #Comando com concatenação usando sinal de (+).
    #Com o comando utilizando sinal de (+) é necessário fazer conversões como inteiro para string.
    print('A empresa '+empresa+ ' está lolizada no endereço '+ logradouro+'.')

    print('\n')

concatenacao_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------

#Exemplo abaixo de concacatenação com comando format.
#O format substitui as variáveis do (concatenar) pelas variáveis declaradas.

def concatenacao_format_string():
    print('Executando a função concatenacao_format_string()')
    estado     = 'São Paulo'
    região     = 'Carapicuíba'
    bairro     = 'Vila Dirce'
    rua        = 'Rua Castro Neves'
    número     = 17
    referência = 'Av. Major Ferreira Neto'

    concatenar =  '{}, {}, {}, {}, {}, {}'

    print(concatenar.format(estado, região, bairro, rua, número, referência))

    print('\n')

concatenacao_format_string()

#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------#--------------