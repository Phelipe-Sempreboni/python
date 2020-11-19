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

# Nota: Neste caso, você pode trocar o comando de (CREATE TABLE) e os parametros para o que preferir. Irei deixar o exemplo abaixo onde:
# [LPUS_ENERGIA]          = database
# [clientes]              = schema (agrupaemento) da tabela
# [tbl_cadastro_clientes] = tabela criada para cadastro de clientes.
def query():
    try:
        cursor = conectar()
        cursor.execute('''
            CREATE TABLE [LPUS_ENERGIA].[clientes].[tbl_cadastro_clientes]
            (
                N_IDCLIENTE INT IDENTITY (1,1) NOT NULL,
                T_NOMECLIENTE VARCHAR (50),
                T_TELEFONECLIENTE VARCHAR (15),
                T_EMAILCLIENTE VARCHAR (40)
                CONSTRAINT PK_N_IDCLIENTE PRIMARY KEY CLUSTERED (N_IDCLIENTE)
            )
            ''')
        cursor.commit()
    except:
        print('Não foi possivel criar a tabela.')
    else:
        print('Tabela criada com sucesso.') 
        
query()