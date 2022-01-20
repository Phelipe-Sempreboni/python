# Exemplos de declaração de variáveis no escopo local e global.

# I:
# Exemplo de declaração de variável global.
# No comando abaixo deste item, tudo que for declarado fora da função, pode ser utilizado em qualquer parte do código programa, logo, é uma variável global, utilizável em qualquer ponto.
# Estamos usando a variáve global dentro de uma função.

nome = 'Luiz Phelipe'

def name():
    print(nome)
name()

# II:
# Exemplo de declaraçaão de variável local.
# No exemplo abaixo, estamos declarando uma variável dentro da função, logo, essa variável se torna local.
# Se você tentar executar a variável declarada (nome_2) fora da função, ocorrerá um erro.

def name_2():
    nome_2 = 'Luiz Utiama'
    print(nome_2)
name_2()

#Descomente esse comando de print abaixo para realizar o teste.
#print (nome_2) #Tentando executar a variável (nome_2) fora da função.

# III:
# Exemplo de declaração de variável global dentro de uma função, deixando de ser local somente para aquela função.
# Utilizando o comando (global) dentro da função para tornar a variável executável em qualquer parte do código e/ou programa.

def name_3():
    global nome_3
    nome_3 = 'Luiz Sempreboni'
    print(nome_3)
name_3()

#Deixei um print dentro da função (name_3) e um fora, para você perceber que na execução a variável (nome_3) será impressas duas vezes, tanto no escolo local quanto global.
#Executando a variável criada dentro da função, fora da própria função com o escopo de variável global, com o comando (global).
print (nome_3) 
