#Exemplo de conexão do Python com o SQL Server com autenticação do Windows, sem necessidade de senha.
#Neste caso, pode ser utilizado quando a autentição for pelo Windows, pois, nota-se que não possui a password (senha) do database.

#Nota: Não precisa ser executado com a função "def conectar()" a maneira 1, se quiser pode ser retirada. A maneira 2 necessita ser mantida.
#Nota2: Pode ser utilizado no Jupyter Notebook.
#Nota3: Por ser login no SQL Server com (Autenticação Windows), a linha de código 21 da maneira 1 e linha de código 40 da maneira 2 ("Trusted_Connection=yes;") necessita estar como "yes", indicando o login por esse tipo de autenticação Windows que não requer senha.
#Nota4: Normalmente nas maneiras 1 e 2 , não temos como verificar realmente a mensagem de conexão, só vai ser possível com o teste de execução de uma query qualquer, pra isso criei as maneiras 3 e 4, para uma verificação realmente se temos conexão.

#Maneira 1 sem teste com query:
#Nota: Nesta maneira, não haverá nenhuma mensagem 

import pyodbc

def conectar():

    conexao = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVIDOR;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "Trusted_Connection=yes;"
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
            "Driver={SQL Server Native Client 11.0};"
            "Server=SERVER;"
            "Database=DATABASENAME;"
            "uid=USUARIO;"
            "Trusted_Connection=yes;"
        )
        return conexao.cursor()
    except:
        return 1

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 3:
