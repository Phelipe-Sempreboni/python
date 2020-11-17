#Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha e execução de storede procedure e query.
#Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui a linha 27 ("pwd=SENHA").

#Nota: Pode ser utilizado no Jupyter Notebook.

#Nota2: Por ser login no SQL Server com (Autenticação SQL Server), a linha de código 28 ("Trusted_Connection=no;") necessita estar como "no", indicando o login por esse tipo de autenticação SQL Server.

#Nota3: Esse código, realiza a conexão, executa uma store procedure, elabora a query e encerra o cursor e a conexão com SQL Server. 

#Nota4: Para verificar o (DRIVER) do SQL Server, conforme temos em todos comandos, você pode seguir o caminho: Tecla do Windows ou no pesquisa, digitar (ODBC), irá abrir uma janela com algumas abas, procure por (DRIVERS) e procure os referente a (SQL Server). Lá estarão as informações de (DRIVERS).

#Nota5: Você pode utilizar de modelo se quiser para testes em outras demandas e estudar.

#Nota6: Por favor, notar os comentários desse código visando não ocorrer erros na execução.


import pyodbc
import time

def conectar():
    try:
        conexao = pyodbc.connect(
            Driver='{SQL Server Native Client 11.0}', #Altere de acordo com seu driver. A (#Nota5) fala desse assunto.
            Server='SERVIDOR', #Insira seu servidor.
            Database='DATABASENAME', #Insira o nome do banco de dados (database) que você quer conectar.
            uid='USUARIO', #Insira seu usuário.
            pwd='SENHA', #Insira sua senha.
            Trusted_Connection='no' #Este campo em (no) refere-se ao tipo de autentição, neste caso, autenticação SQL Server. Se quiser fazer com autenticação Windows, retire o campo (pwd) que seria a senha, e mude este campo para (yes).
        )
        return conexao.cursor()
    except:
        return 1

def query_execute_stored_procedure():
    try:
        cursor = conectar()
        query_exec_stored_procedure = "EXECUTE procedure_name" #Insira a (STORED PROCEDURE) que deseja executar.
        cursor.execute(query_exec_stored_procedure)
        cursor.commit()
        return()
    except:
        print('Não foi possivel retornar os dados da consulta.') #Mensagem pode ser alterada se quiser.
    finally:
        print('Stored Procedure executada com sucesso.') #Mensagem pode ser alterada se quiser.

def query_qtde_carregada():
    try:
        cursor = conectar()
        data_hora_minuto_segundo_atual = time.strftime('%d-%m-%Y ás %H:%M:%S', time.localtime()) #Aqui você pode fazer alteração do formato de data se tiver conhecimento, do que está dentro do parenteses.
        query_exec_contador_linhas = "SELECT COUNT(*) FROM ..." #Insira a query que desaja executar e neste caso dessa query, ela faz a contagem de linhas que foram inseridas na tabela, então, tente seguir esse padrão, pois, no print abaixo, ele utilziar essa função para informar em mensagem a quantidade de linhas.
        cursor.execute(query_exec_contador_linhas)
        query_resultado = cursor.fetchone()
        return()
    finally:
        print('Quantidade de linhas inseridas na tabela é de',query_resultado, 'em', data_hora_minuto_segundo_atual,'.') #Mensagem pode ser alterada se quiser, mas os campos em branco, que são funções, não devem ser alteradas.

def encerrar_cursor_conexao():
    try:    
        cursor = conectar()
        cursor.close()
        conexao = conectar()
        conexao.close()
        return()
    except:
        print("Não foi possível encerrar o cursor e a conexão.") #Mensagem pode ser alterada se quiser.
    finally:
        print("Cursor e conexão com banco de dados foram encerradas.") #Mensagem pode ser alterada se quiser.

def execucoes():
    try:
        query_execute_stored_procedure()
        query_qtde_carregada()
        encerrar_cursor_conexao()
    except:
        print('Caso haja erro na conexão com banco de dados ou falha na execução da consulta, por favor, verifique ou solicite ao responsável da programação verificar os scripts.') #Mensagem pode ser alterada se quiser.
execucoes()