# Neste arquivo, iremos ver um pouco sobre:
# Declaração de variáves com comando print; 
# Descobrir o tipo de dados da variável (str, int, floa, etc) com comando type;
# Principais terminadores de comando do Python;
# Concatenação de impressões pelo comando print;
# Comentar códigos, tanto dessa maneira, com uma única linha ou com diversas linhas, blocos, instruções, etc.   

# Observação: Python não é uma linguagem de programação fortemente tipada, logo, não precisamos declarar o tipo que será a variável, como (string, int ou float).

# Declaração de variáveis;
github = 'Meu repositório pessoal'
repositorio = 'Projetos de Python'
num_respositorio = 3
num_respositorio_2 = 1.118

# Imprimindo os valores atribuídos nas variáveis;
print (github)
print (repositorio)
print (num_respositorio)
print (num_respositorio_2)

# Descobrindo o tipo de dado da variável;
print (type(github))
print (type(repositorio))
print (type(num_respositorio))
print (type(num_respositorio_2))

# Descobrindo o tipo de dado da variável com mensagem:
# O comando print('\n') é para (pula/quebrar a linha).
print('\n')
print ('Valor: ',(github))
print ('Tipo: ',type(github))
print('\n')
print ('Valor: ',repositorio)
print ('Tipo: ',type(repositorio))
print('\n')
print ('Valor: ',num_respositorio)
print ('Tipo: ',type(num_respositorio))
print('\n')
print ('Valor: ',num_respositorio_2)
print ('Tipo: ',type(num_respositorio_2))
print('\n')

# Terminadores de comando do Python, neste caso, demonstrando com o (ponto e vírgula (;)).
# Os principais de Python são o o (ENTER) quando você quebra uma linha e o (ponto e vírgula (;)), principalmente se for escrever o código conforme o exemplo abaixo, ou seja, na mesma linha.
github_2 = 'Repositório da nossa empresa'; repositorio_3 = 'SOCIEDADE BRASIL BR'; num_respositorio_3 = 8; num_respositorio_4 = 2.5898
print (github_2); print (repositorio_3); print(num_respositorio_3); print(num_respositorio_4); print (type(github_2)); print (type(repositorio_3)); print(type(num_respositorio_3)); print(type(num_respositorio_4)) 

#Concatenando valores no comando print:
github = 'Meu repositório pessoal'
repositorio = 'Projetos de Python'
num_respositorio = 3
num_respositorio_2 = 1.118
print ('O nome do GitHub é', github, 'com nome de repositório', repositorio, 'listado no número', num_respositorio, 'e também listado no número', num_respositorio_2)

# Comentando códigos com uma única linha. Utilize o (#) para fazer o código virar comentário.
#github = 'Meu repositório pessoal'
#repositorio = 'Projetos de Python'
#num_respositorio = 3
#num_respositorio_2 = 1.118

# Comentando códigos com diversas linhas. Utilize três aspas para fazer o código virar comentário em diversas linhas (''')
# Caso queira comentar um bloco e continuar um novo código abaixo, você pode utilziar conforme o exemplo abaixo.
'''
print (github)
print (repositorio)
print (num_respositorio)
print (num_respositorio_2)


print (type(github))
print (type(repositorio))
print (type(num_respositorio))
print (type(num_respositorio_2))
'''