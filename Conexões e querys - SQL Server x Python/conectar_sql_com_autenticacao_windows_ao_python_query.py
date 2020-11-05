#Exemplo de conexão do Python com o SQL Server com autenticação Windows, sem necessidade de senha e execução de query.
#Neste caso, pode ser utilizado quando a autentição for Windows, pois, nota-se que não possui senha.

#Nota: Pode ser utilizado no Jupyter Notebook.
#Nota2: Por ser login no SQL Server com (Autenticação Windows), a linha de código 17 ("Trusted_Connection=no;") necessita estar como "yes", indicando o login por esse tipo de autenticação Windows.
#Nota3: Esse código, realiza a conexão, elabora a query e encerra o cursor e a conexão com SQL Server. 

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=LAPTOP-PI0F6JSQ;"
            "Database=SUCOS_VENDAS;"
            "uid=sempreboni;"
            "Trusted_Connection=yes;"
        )
        return conexao.cursor()
    except:
        return 1

def query():
    try:
        cursor = conectar()
        cursor.execute("SELECT * FROM [SUCOS_VENDAS].[dbo].[TABELA DE VENDEDORES]")
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
        conexao = conectar()
        cursor.close()
        conexao.close()
    except:
        print("Não foi possível encerrar o cursor e a conexão.")

def execucoes():
    try:
        query()
        encerrar_cursor_conexao()
    except:
        print('Caso haja erro na conexão com banco de dados ou falha na execução da consulta, por favor, verifique ou solicite ao responsável da programação verificar os scripts.')

execucoes()