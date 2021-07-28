#Exemplo de conexão do Python com o SQL Server com autenticação Windows, sem necessidade de senha e execução de query.
#Neste caso, pode ser utilizado quando a autentição for Windows, pois, nota-se que não possui senha.

#Nota: Pode ser utilizado no Jupyter Notebook.

#Nota2: Por ser login no SQL Server com (Autenticação Windows), a linha de código 17 ("Trusted_Connection=no;") necessita estar como "yes", indicando o login por esse tipo de autenticação Windows.

#Nota3: Esse código, realiza a conexão, elabora a query e encerra o cursor e a conexão com SQL Server. 

#Nota4: Para verificar o (DRIVER) do SQL Server, conforme temos em todos comandos, você pode seguir o caminho: Tecla do Windows ou no pesquisa, digitar (ODBC), irá abrir uma janela com algumas abas, procure por (DRIVERS) e procure os referente a (SQL Server). Lá estarão as informações de (DRIVERS).

#Nota5: Utilize os comentários no código da (#Maneira1) para as demais maneiras.

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 1:
#Nota: A maneira 1 tem mais comandos e considero mais completo que a maneira 2, que considero mais simples.

import pyodbc

def conectar():
    try:
        conexao = pyodbc.connect(
            Driver='{SQL Server Native Client 11.0}', #Altere de acordo com seu driver. A (#Nota4) fala desse assunto.
            Server='SERVIDOR', #Insira seu servidor.
            Database='DATABASENAME', #Insira o nome do banco de dados (database) que você quer conectar.
            uid='USUARIO', #Insira seu usuário.
            Trusted_Connection='yes' #Este campo em (yes) refere-se ao tipo de autentição, neste caso, autenticação Windows.
        )
        return conexao.cursor()
    except:
        return 1

def query():
    try:
        cursor = conectar()
        cursor.execute("SELECT * FROM ...") #Insira sua consulta (query) neste local.
        query_resultado = cursor.fetchall()
        return ()
    except:
        print('Não foi possivel retornar os dados da consulta.') #Pode realizar a alteração de mensagem.
    finally:
        print(query_resultado)
        print('Consulta realizada com sucesso.') #Pode realizar a alteração de mensagem.

def encerrar_cursor_conexao():
    try:    
        cursor = conectar()
        cursor.close()
        conexao = conectar()
        conexao.close()
        return()
    except:
        print("Não foi possível encerrar o cursor e a conexão.") #Pode realizar a alteração de mensagem.
    finally:
        print("Cursor e conexão encerradas") #Pode realizar a alteração de mensagem.

def execucoes():
    try:
        query()
        encerrar_cursor_conexao()
    except:
        print('Caso haja erro na conexão com banco de dados ou falha na execução da consulta, por favor, verifique ou solicite ao responsável da programação verificar os scripts.') #Pode realizar a alteração de mensagem.

execucoes()

#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#
#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#----------#

#Maneira 2:

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
    cursor.execute("SELECT * FROM ...")
    query_resultado = cursor.fetchall()
    print(query_resultado)
    print("Consulta realizada com sucesso")
    try:
        cursor.close()
        conexao.close()
        return()
    finally:
        print('Conexao e cursor encerrados com sucesso')

conectar()
