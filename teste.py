import pyodbc
import pandas as pd

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