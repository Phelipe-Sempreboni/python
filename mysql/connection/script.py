import mysql.connector
from mysql.connector import errorcode

def conexaomysql():

	try:
		#Criação de cadeia de conexão com MySQL.
		conexao = mysql.connector.connect(host='localhost', user='root', password='Jg348*2uah@p', database='world')

		#Verificação e informação da versão do banco de dados MySQL que está sendo realizada a conexão.
		if conexao.is_connected():
			db_info = conexao.get_server_info()
			print('Conexão bem sucedida. Conectado ao servidor do MySQL versão', db_info)

		#Verifica a conexão e realiza a execução de query para verificar em qual banco de dados do MySQL está sendo realizada a conexão.
		if conexao.is_connected():
			query = ("SELECT * FROM world.city;")
			cursor = conexao.cursor()
			cursor.execute(query)
			resultado = cursor.fetchall()
			print('Conectado ao banco de dados', resultado)

		#Verificar a conexão e realizada o encerramento do cursor e da conexão com MySQL.
		if conexao.is_connected():
			cursor.close()
			conexao.close()
			print("Conexão foi encerrada")

	#Verificação de houver erro na etapa acima da cadeia de conexão.
	except mysql.connector.Error as error:

		if error.errno == errorcode.ER_BAD_DB_ERROR:
			print("Banco de dados não existe")
		elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Usuário ou senha incorretas")
		else:
			print(error)
	else:
		conexao.close()

conexaomysql()