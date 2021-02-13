#Exemplo de conexão do Python com o SQL Server com autenticação do Windows, sem necessidade de senha e execução de query com biblioteca pandas também.
#Neste caso, pode ser utilizado quando a autentição for pelo Windows, pois, nota-se que não possui a password (senha) do database.

#Nota: Não precisa ser executado com a função "def conectar_sql_server_com_autenticao_windows_ao_python()", se quiser pode ser retirada.

#Nota2: Pode ser utilizado no Jupyter Notebook.

#Nota3: Por ser login no SQL Server com (Autenticação Windows), a linha de código 14 ("Trusted_Connection=yes;") necessita estar como "yes", indicando o login por esse tipo de autenticação"

#Nota4: Neste caso abaixo, houve execução da query com utilização da biblioteca Pandas, que é mais utilizada para área de dados, logo, o "df" na linha 21, sigfica Data Frame.

#Nota5: Para verificar o (DRIVER) do SQL Server, conforme temos em todos comandos, você pode seguir o caminho: Tecla do Windows ou no pesquisa, digitar (ODBC), irá abrir uma janela com algumas abas, procure por (DRIVERS) e procure os referente a (SQL Server). Lá estarão as informações de (DRIVERS).

import pandas as pd
import pyodbc

def conectar():
    conexao = pyodbc.connect(
        Driver='{SQL Server Native Client 11.0}', #Altere de acordo com seu driver. A (#Nota4) fala desse assunto.
        Server='SERVIDOR', #Insira seu servidor.
        Database='DATABASENAME', #Insira o nome do banco de dados (database) que você quer conectar.
        uid='USUARIO', #Insira seu usuário.
        Trusted_Connection='yes', #Este campo em (no) refere-se ao tipo de autentição, neste caso, autenticação Windows.
    )
    cursor = conexao.cursor()
    query = "SELECT * FROM ..." #Insira sua consulta (query) neste local.
    df = pd.read_sql(query, conexao)
    print(df.head())

conectar()
