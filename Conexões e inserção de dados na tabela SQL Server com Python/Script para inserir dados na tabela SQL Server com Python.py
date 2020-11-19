# Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha e de uma query para inserção de dados na tabela.
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