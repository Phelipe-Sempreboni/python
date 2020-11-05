import pyodbc

def conectar():
    conexao = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=LAPTOP-PI0F6JSQ;"
        "Database=SUCOS_VENDAS;"
        "uid=sempreboni;"
        "Trusted_Connection=yes;"
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM [SUCOS_VENDAS].[dbo].[TABELA DE VENDEDORES]")
    query_resultado = cursor.fetchall()
    print(query_resultado)
    print("Consulta realizada com sucesso")

conectar()