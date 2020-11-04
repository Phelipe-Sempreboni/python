#Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha.
#Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui a linha 15 ("pwd=SENHA").

#Nota: Não precisa ser executado com a função "def conectar()", se quiser pode ser retirada.
#Nota2: Pode ser utilizado no Jupyter Notebook.
#Nota3: Por ser login no SQL Server com (Autenticação SQL Server), a linha de código 16 ("Trusted_Connection=no;") necessita estar como "no", indicando o login por esse tipo de autenticação"

#Maneira 1:

import pyodbc

def conectar():
    conexao = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVER;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "pwd=SENHA;"
        "Trusted_Connection=no;"
    )
conectar()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 2:

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=SERVER;"
            "Database=DATABASENAME;"
            "uid=USUARIO;"
            "pwd=SENHA;"
            "Trusted_Connection=no;"
        )
        return conexao.cursor()
    except:
        print('Não foi possível realizar a conexão com banco de dados.')