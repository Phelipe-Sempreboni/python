#Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha e execução de query com biblioteca pandas também.
#Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui a linha 15 ("pwd=SENHA").

#Nota: Não precisa ser executado com a função "def conectar_sql_server_com_autenticao_sql_ao_python()", se quiser pode ser retirada.
#Nota2: Pode ser utilizado no Jupyter Notebook.
#Nota3: Por ser login no SQL Server com (Autenticação SQL Server), a linha de código 16 ("Trusted_Connection=no;") necessita estar como "no", indicando o login por esse tipo de autenticação"
#Nota4: Neste caso abaixo, houve execução da query com utilização da biblioteca Pandas, que é mais utilizada para área de dados, logo, o "df" na linha 22, sigfica Data Frame.

def conectar_ao_sql_server_e_executar_query():
    import pandas as pd
    import pyodbc
    cnxn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVIDOR;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "pwd=SENHA;"
        "Trusted_Connection=no;"
    )
    cursor = cnxn.cursor()
    query = "SELECT * FROM ..."
    df = pd.read_sql(query, cnxn)
    print(df.head())
    
conectar_ao_sql_server_e_executar_query()