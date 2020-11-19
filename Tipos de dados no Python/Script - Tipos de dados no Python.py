# Neste arquivo, veremos um pouco sobre os tipos de dados no Python.
# O comando print('\n') é para pular/quebrar linhas.

#Tipo: Sting;
print('\n')
nome = 'Luiz Phelipe'
print('Valor: ', nome)
print('Tipo: ',type(nome))
print('\n')

#Tipo: Boolean
boleano = True
print('Valor: ', boleano)
print('Tipo: ',type(boleano))
print('\n')

#Tipo: Inteiro;
numero_int = 5
print('Valor: ', numero_int)
print('Tipo: ',type(numero_int))
print('\n')

#Tipo: Float;
numero_float = 12.5863
print('Valor: ', numero_float)
print('Tipo: ',type(numero_float))
print('\n')

#Tipo: Número complexo;
x1=5;x2=4;x=complex(x1, x2)
print(x.real) #número real
print(x.imag) #número imaginário
print('Valor: ', x) #Valor referente a (x)
print('Tipo: ',type(x)) #Tipo referente a (x)
print('\n')

#Tipo: List / Array:
#Notar que aqui você poder imprir as posições. Lembre-se que as posições sempre começam por [0]. Exemplo abaixo.
#Notar que você pode manipular e alterar também o conteúdo da posição.
#Notar que a lista/array aceita tipo de dados diferentes e podemos pela posição, verificar qual o tipo daquele dados. Exemplo abaixo.
y = ['Papagaio', 'Zoológico', 'Fauna', 'Restaurante', 10, 15.785, False, True]
print('Imprimindo somente o ',y[0], ' da lista/array.')
print('Valor: ', y)
print('Tipo: ',type(y))
print('Tipo: ',type(y[5])) #Verificando o tipo de dados na posição 5, que seria o tipo (float).
print('\n')

#Tipo: Tupla:
#Notar que a tupla é muito parecido com o tipo (list/array), porém, diferente dele, o tipo (tupla) não pode ser manipulado os valores de dentro. É somente o que está dentro e sem permissão para modificação de acordo com a posição [0], [1], etc.
#Notar que aqui você poder imprir as posições. Lembre-se que as posições sempre começam por [0]. Exemplo abaixo.
#Notar que a tupla aceita tipo de dados diferentes e podemos pela posição, verificar qual o tipo daquele dados. Exemplo abaixo.
z = ('Papagaio', 'Zoológico', 'Fauna', 'Restaurante', 10, 15.785, False, True)
print('Imprimindo somente o ',z[0], ' da tupla.')
print('Valor: ', z)
print('Tipo: ',type(z))
print('Tipo: ',type(z[5])) #Verificando o tipo de dados na posição 5, que seria o tipo (float).
print('\n')

#Tipo: Range, onde seria um método para criação de list/array conforme parametros do comando.
w = range(1,21,1) #Geração de list/array
w1 = list(range(1,21,1))
print('Valor: ', w)
print('Tipo: ',type(w))
print('Valor: ', w1) #Exemplo de um comando range gerando uma (list/array) de (1 a 20 no intervalo de 1 em 1)
print('\n')

#Tipo: Dictionary
#Um dicionário é uma coleção não ordenada, mutável e indexada. No Python, os dicionários são escritos com chaves e têm chaves e valores
dicto = {
    'Nome': 'Carlos Abreu',
    'Estado': 'São Paulo',
    'Cidade': 'Santo Amaro',
    'País': 'Brasil'
}
print('Valor: ', dicto)
print('Tipo: ',type(dicto))

#Digamos que queira imprimir o valor da chave (Cidade). Exemplo abaixo:
print('O valor da chave Cidade é ',dicto['Cidade'])
print('O valor da chave Estado é ',dicto['Estado'])
print('\n')


#Tipo: SET
#O SET não deixa repetir valores e os ordena.
s = {8,5,9,8,9,5,1,2,4,5,9}
print('Valor: ', s)
print('Tipo: ',type(s))