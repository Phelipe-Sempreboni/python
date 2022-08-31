#Exemplo de conexão do Python com o SQL Server com autenticação do Windows, sem necessidade de senha.
#Neste caso, pode ser utilizado quando a autentição for pelo Windows, pois, nota-se que não possui a password (senha) do database.

#Nota: Pode ser utilizado no Jupyter Notebook.

#Nota2: Por ser login no SQL Server com (Autenticação Windows), a linha de código 20 da maneira 1 e linha de código 40 da maneira 2 ("Trusted_Connection=yes;") necessita estar como "yes", indicando o login por esse tipo de autenticação Windows que não requer senha.

#Nota3: Normalmente nas maneiras 1 e 2 , não temos como verificar realmente a mensagem de conexão, só vai ser possível com o teste de execução de uma query qualquer, pra isso criei as maneiras 3 e 4, para uma verificação realmente se temos conexão.

#Nota4: Para verificar o (DRIVER) do SQL Server, conforme temos em todos comandos, você pode seguir o caminho: Tecla do Windows ou no pesquisa, digitar (ODBC), irá abrir uma janela com algumas abas, procure por (DRIVERS) e procure os referente a (SQL Server). Lá estarão as informações de (DRIVERS).

#Nota5: Utilize os comentários no código da (#Maneira1) para as demais maneiras.


#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 1 sem teste com query:
#Nota: Nesta maneira, não haverá nenhuma mensagem 

import pyodbc

def conectar():

    conexao = pyodbc.connect(
        Driver='{SQL Server Native Client 11.0}',#Altere de acordo com seu driver. A (#Nota4) fala desse assunto.
        Server='SERVIDOR',#Insira seu servidor.
        Database='DATABASENAME',#Insira o nome do banco de dados (database) que você quer conectar.
        uid='USUARIO',#Insira seu usuário.
        Trusted_Connection='yes'#Este campo em (yes) refere-se ao tipo de autentição, neste caso, autenticação Windows.
    )
conectar()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 2 sem teste com query:
#Nota: Nesta maneira, não haverá nenhuma mensagem 

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            Driver='{SQL Server Native Client 11.0}',
            Server='SERVIDOR',
            Database='DATABASENAME',
            uid='USUARIO',
            Trusted_Connection='yes'
        )
        return conexao.cursor()
    except:
        return 1

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 3:
#Menção a maneira 1, mas, com teste de execução por uma query.

import pyodbc

def conectar():
    conexao = pyodbc.connect(
        Driver='{SQL Server Native Client 11.0}',
        Server='SERVIDOR',
        Database='DATABASENAME',
        uid='USUARIO',
        Trusted_Connection='yes'
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ...") #Insira sua consulta (query) neste local.
    query_resultado = cursor.fetchall()
    print(query_resultado)

conectar()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#


#Maneira 4:
#Menção a maneira 2, mas, com teste de execução por uma query.


import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            Driver='{SQL Server Native Client 11.0}',
            Server='SERVIDOR',
            Database='DATABASENAME',
            uid='USUARIO',
            Trusted_Connection='yes'
        )
        return conexao.cursor()
    except:
        return 1

def query():
    try:
        cursor = conectar()
        cursor.execute("SELECT * FROM ...") #Insira sua consulta (query) neste local.
        query_resultado = cursor.fetchall()
    except:
        print('Não foi possivel retornar os dados da consulta.') #Pode realizar a alteração de mensagem.
    finally:
        print(query_resultado)
        print('Consulta realizada com sucesso.') #Pode realizar a alteração de mensagem.
query()
