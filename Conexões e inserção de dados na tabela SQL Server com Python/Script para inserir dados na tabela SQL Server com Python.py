def conectar():

    import pyodbc

    try:
        conexao = pyodbc.connect(
            Driver='{SQL Server Native Client 11.0}', #Altere de acordo com seu driver. A (#Nota4) fala desse assunto.
            Server='SERVIDOR', #Insira seu servidor.
            Database='DATABASENAME',#Insira o nome do banco de dados (database) que você quer conectar.
            uid='USUARIO', #Insira seu usuário.
            pwd='SENHA', #Insira sua senha.
            Trusted_Connection='no' #Este campo em (no) refere-se ao tipo de autentição, neste caso, autenticação SQL Server.
        )
        return conexao.cursor()
    except:
        print('Não foi possível conectar ao banco de dados.')

# Nota: Neste caso, você pode trocar o comando de (INSERT INTO) e os parametros para o que preferir. Irei deixar o exemplo abaixo onde:
# [LPUS_ENERGIA]          = database
# [clientes]              = schema (agrupaemento) da tabela
# [tbl_cadastro_clientes] = tabela criada para cadastro de clientes.
def query():
    try:
        cursor = conectar()
        cursor.execute('''
            INSERT INTO [LPUS_ENERGIA].[clientes].[tbl_cadastro_clientes] VALUES ('Ronaldo Henrique', '1194458264', 'ronaldoe@outlook.com')
            INSERT INTO [LPUS_ENERGIA].[clientes].[tbl_cadastro_clientes] VALUES ('Adriano Barbosa', '1194454785', 'adriano@outlook.com')
            INSERT INTO [LPUS_ENERGIA].[clientes].[tbl_cadastro_clientes] VALUES ('Eduardo Leão', '1188596347', 'eduardo@outlook.com')
            INSERT INTO [LPUS_ENERGIA].[clientes].[tbl_cadastro_clientes] VALUES ('Silvio de Lima', '11974126895', 'silvio@outlook.com')
            ''')
        cursor.commit()
    except:
        print('Não foi possivel inserir os dados na tabela.')
    else:
        print('Dados inseridos com sucesso na tabela.') 
        
query()