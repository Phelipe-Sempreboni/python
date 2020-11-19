# Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha e de uma query para criação de tabela.
# Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui o campo ("pwd=SENHA").

#Nota: Caso não queira autenticação por SQL Server e sim autenticação por Windows, altere o comando da função (conectar()) chamado (Trusted_Connection) de 'no' para 'yes', e, retire o campo (pwd), pois, conexões com autenticação não necessitam de senhas, logo, o campo pode ser apagado.

#Nota2: Para verificar o (DRIVER) do SQL Server, conforme temos em todos comandos, você pode seguir o caminho: Tecla do Windows ou no pesquisa, digitar (ODBC), irá abrir uma janela com algumas abas, procure por (DRIVERS) e procure os referente a (SQL Server). Lá estarão as informações de (DRIVERS).


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