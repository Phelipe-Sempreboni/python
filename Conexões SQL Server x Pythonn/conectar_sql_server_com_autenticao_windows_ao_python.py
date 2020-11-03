#Exemplo de conexão do Python com o SQL Server com autenticação do Windows, sem necessidade de senha.
#Neste caso, pode ser utilizado quando a autentição for pelo Windows, pois, nota-se que não possui a password (senha) do database.

#Nota: Não precisa ser executado com a função "def conectar_sql_server_com_autenticao_windows_ao_python()", se quiser pode ser retirada.
#Nota2: Pode ser utilizado no Jupyter Notebook.
#Nota3: Por ser login no SQL Server com (Autenticação Windows), a linha de código 14 ("Trusted_Connection=yes;") necessita estar como "yes", indicando o login por esse tipo de autenticação"

def conectar_sql_server_com_autenticao_windows_ao_python():
    import pyodbc
    cnxn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=SERVIDOR;"
        "Database=DATABASENAME;"
        "uid=USUARIO;"
        "Trusted_Connection=yes;"
    )
conectar_sql_server_com_autenticao_windows_ao_python()