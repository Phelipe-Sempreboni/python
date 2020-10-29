# Python para Ciência de Dados - Lógica de Programação.

### Abaixo temos um pouco de um dos cursos realizados de Python para Data Science, onde, o intuito é apresentar a lógica de programação para os usuários, porém, se já houver lógica de programação do usuário derivados de outros sistemas como Java, SQL Server, por exemplo, fica mais fácil a compreensão.

Abaixo temos os scripts que podem ser executados no vscode, Jupyter, e outras plataformas.
Também temos o arquivo (logica_de_programacao.py) na extensão Python.

```

#A partir deste ponto os códigos podem ser copiados e executados em alguma plataforma de Python para leitura e execução.

#Script 1
nome = 'Sempreboni'
idade = 26
print(f'Meu nome é {nome} e minha idade é {idade} anos')

#Script 2
def saudacao ():
    nome = input('Qual seu nome? ')
    print(f'Olá {nome}')
saudacao()

#Script 3
def nome_completo():
 primeiro_nome = input('Qual seu primeiro nome? ')
 sobrenome = input('Qual seu sobrenome? ')
 nome_inteiro = primeiro_nome + ' ' + sobrenome
 print(f'Olá {nome_inteiro}')
nome_completo()

#Script 4
def saudacao_com_parametros(nome_da_pessoa):
    print(f'Olá {nome_da_pessoa}')
saudacao_com_parametros(nome)

#Script 5
idade = 19

def verifica_se_pode_dirigir_com_parametros(idade):
    if idade >= 18:
        print('Tem permissão para dirigir')
    else:
        print('Não tem permissão para dirigir')
verifica_se_pode_dirigir_com_parametros(idade)

#Script 6
def verifica_se_pode_dirigir_sem_parametros():
    idade = input ('Qual sua idade ? ')
    idade = int(idade)
    if idade >= 18:
        print('Tem permissão para dirigir')
    else:
        print('Não tem permissão para dirigir')
verifica_se_pode_dirigir_sem_parametros()

#Script 7
def velocidade_media():
    distancia = input ('Insira a distancia percorrida: ')
    distancia = float(distancia)
    tempo = input ('insira o tempo de percurso: ')
    tempo = float(tempo)
    calculo = distancia / tempo
    print(f'A velocidade média é {calculo} m/s')
velocidade_media()

#Script 8
def velocidade(espaco, tempo):
    v = espaco / tempo
    print(f'Velocidade: {v} m/s')
velocidade(100, 20)

#Script 9
def habilitacao():
 idade = input('Qual sua idade? ')
 idade = int(idade)
 if idade >= 18:
   print('Pode tirar habilitação')
 else:
   tempo = 18 - idade
   print(f'Calma... espere {tempo} ano(s) para tirar habilitação')

habilitacao()

#Script 10
idade = 22
type(idade)

#Script 11
nome = 'Semprebonu'
type(nome)

#Script 12
idades = [18, 22, 15, 50]
type(idades)

#Script 13
idades[2]

#Script 14
idades[0:3]

#Script 15
idades[1:]

#Script 16
#for fora da função
def verifica_se_pode_dirigir_com_parametros(idade):
    if idade >= 18:
        print(f'{idade} anos de idade, TEM permissão para dirigir')
    else:
        print(f'{idade} anos NÃO TEM permissão para dirigir')
for idade in idades:
    verifica_se_pode_dirigir_com_parametros(idade)

#Script 17
def verificar_se_pode_dirigir_dentro_funcao(idades):
    for idade in idades:
        if idade >= 18:
            print(f'{idade} anos de idade, TEM permissão para dirigir')
        else:
            print(f'{idade} anos NÃO TEM permissão para dirigir')
verificar_se_pode_dirigir_dentro_funcao(idades)

#Script 18
permissoes = []
idades = [20, 14, 40]

def verifica_se_pode_dirigir_boleanos(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)
    
verifica_se_pode_dirigir_boleanos(idades, permissoes)

#Script 19
for permissao in permissoes:
    if permissao == True:
        print('Tem permissao para dirigir')
    else:
        print('Não tem permissao para dirigir')

#Script 20
pi = 3.14
type(pi)

#Script 21
lista = ['Phelipe', 26, True, '18']

for elemento in lista:
    print(f'O elemento {elemento} é do tipo: ', type(elemento))

#Script 22
from random import randrange, seed
randrange(0, 11)

#Script 23
notas_matematica = []
for notas in range(8):
    notas_matematica.append(randrange(0, 11))
    
notas_matematica
len(notas_matematica)

#Script 24
lista = ['int', False, True, '18', 2020]
for elemento in lista:
 print(type(elemento))


#Script 25

 #constante = seed(11)
notas_portugues = []
for notas in range(8):
    notas_portugues.append(randrange(0,11))
notas_portugues

notas_portugues

#Script 26
import matplotlib.pyplot as plt
x = list(range(1,9))
y = notas_matematica
plt.plot(x, y, marker = 'o')
plt.title('Notas de matematica')
plt.xlabel('Provas')
plt.ylabel('Notas')
plt.show()

#Script 27
import matplotlib.pyplot as plt

notas_matematica = ['Matemática',8,7,6,6,7,7,8,10]
notas_portugues = ['Português',9,9,9,8,5,6,8,5]
notas_geografia = ['Geografia',10,10,6,7,7,7,8,7]

notas = [notas_matematica, notas_portugues, notas_geografia]

#Script 28
for nota in notas:
 x = list(range(1, 9))
 y = nota[1:]
 plt.plot(x, y, marker='o')
 plt.xlabel('Provas')
 plt.ylabel('Notas')
 plt.title(nota[0])
 plt.show()

 print(f'Curso finalizado')