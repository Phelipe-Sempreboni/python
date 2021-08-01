# 1º método de conexão com Oracle Database e execução de uma query.

import cx_Oracle # Importação da biblioteca 

uid = '' # Insira o usuário.
pwd = '' # Insira a senha.
db = '' # Insira, respectivamente, (Nome do Host:Porta/SID ou serviço). Lembrar de não deixar espaços em branco.
 
connection = cx_Oracle.connect(uid+'/'+pwd+'@'+db) # Realliza a concatenação dos campos (uid, pwd e db) para a string de conexão no Oracle.

cursor = connection.cursor() # Cria um cursor para conseguir executar comandos de query/scripts no banco de dados.

cursor.execute('SELECT * FROM [SCHEMA].[TABLE OU VIEW]')  # Executa a query. Insira sua query/consulta neste campo.

result = cursor.fetchall() # Irá retornar os registros da consulta. Neste caso, o comando (fetchall) busca todas as linhas de um resultado de consulta. Ele retorna todas as linhas como uma lista de tuplas. Uma lista vazia é retornada se não houver nenhum registro para buscar.
if result == None:
    print ('Nenhum resultado econtrado') # Caso a tabela esteja vazia, irá retornar essa mensagem.
    exit # Caso a tabela esteja vazia, irá sair do comando e encerrar.
else: # Comando para executar caso a tabela contenha registros.
    while result:
        print (result[0])
        result = cursor.fetchall() # Irá retornar os registros da consulta. Neste caso, o comando (fetchall) busca todas as linhas de um resultado de consulta. Ele retorna todas as linhas como uma lista de tuplas. Uma lista vazia é retornada se não houver nenhum registro para buscar.

cursor.close() # Encerra o cursor com o banco de dados.

connection.close() # Encerra a conexão com o banco de dados.

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

# 2º método de conexão com Oracle Database e execução de uma query.

import cx_Oracle # Importação da biblioteca 

conexao = cx_Oracle.connect('Usuário/Senha@Nome do Host/SID ou serviço') # Insira, respectivamente, (Usuário/Senha@Nome do Host/SID ou serviço). Lembrar de não deixar espaços em branco.

cursor = conexao.cursor() # Cria um cursor para conseguir executar comandos de query/scripts no banco de dados.

cursor.execute('') # Executa a query. Insira sua query/consulta neste campo.

for result in cursor:
  result = cursor.fetchall() # Irá retornar os registros da consulta. Neste caso, o comando (fetchall) busca todas as linhas de um resultado de consulta. Ele retorna todas as linhas como uma lista de tuplas. Uma lista vazia é retornada se não houver nenhum registro para buscar.
  print(result) # Imprimir o resultado no terminal.

cursor.close() # Encerra o cursor com o banco de dados.

conexao.close() # Encerra a conexão com o banco de dados.

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
