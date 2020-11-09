#Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha e execução de query.
#Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui a linha 15 ("pwd=SENHA").

#Nota: Pode ser utilizado no Jupyter Notebook.
#Nota2: Por ser login no SQL Server com (Autenticação SQL Server), a linha de código 18 ("Trusted_Connection=no;") necessita estar como "no", indicando o login por esse tipo de autenticação SQL Server.
#Nota3: Esse código, realiza a conexão, elabora a query e encerra o cursor e a conexão com SQL Server. 

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 1:
#Nota: A maneira 1 tem mais comandos e considero mais completo que a maneira 2, que considero mais simples.

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=SERVIDOR;"
            "Database=DATABASENAME;"
            "uid=USUARIO;"
            "pwd=SENHA;"
            "Trusted_Connection=no;"
        )
        return conexao.cursor()
    except:
        return 1

def query():
    try:
        cursor = conectar()
        cursor.execute("SELECT * FROM ...")
        query_resultado = cursor.fetchall()
        return query_resultado
    except:
        print('Não foi possivel retornar os dados da consulta.')
    finally:
        print(query_resultado)
        print('Consulta realizada com sucesso.')

def encerrar_cursor_conexao():
    try:    
        cursor = conectar()
        cursor.close()
        conexao = conectar()
        conexao.close()
        return()
    except:
        print("Não foi possível encerrar o cursor e a conexão.")
    finally:
        print("Cursor e conexão encerradas")

def execucoes():
    try:
        query()
        encerrar_cursor_conexao()
    except:
        print('Caso haja erro na conexão com banco de dados ou falha na execução da consulta, por favor, verifique ou solicite ao responsável da programação verificar os scripts.')

execucoes()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 2:

import pyodbc

def conectar():
    conexao = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVIDOR;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "pwd=SENHA;"
        "Trusted_Connection=no;"
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ...")
    query_resultado = cursor.fetchall()
    print(query_resultado)
    print("Consulta realizada com sucesso")

conectar()