# Exemplo de conexão do Python com o SQL Server com autenticação do SQL Server, com necessidade de senha.
# Notar que o comando abaixo faz a conexão deleta dados da tabela conforme ID do cliente, porém com declaração e input, ou seja, você poderá inserir direto pelo teclado.
# Neste caso, pode ser utilizado quando a autentição for pelo SQL Server, pois, nota-se que possui o campo ("pwd=SENHA").

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


# Nota: Neste caso, você pode trocar o comando de (DELETE) e os parametros para o que preferir. Irei deixar o exemplo abaixo onde:
# [LPUS_ENERGIA]          = database
# [clientes]              = schema (agrupaemento) da tabela
# [tbl_cadastro_clientes] = tabela criada para cadastro de clientes.
# Váriavel (id_cliente) declarada para utilização com input, ou seja, você irá digitar direto do teclado.
def query():
    
    id_cliente = input("Digite o ID do registro a ser deletado: ") #Você pode alterar o campo do input e da consulta. Não necessariamente necessita ser o ID do cliente, conforme exemplo de tabela.

    try:
        cursor = conectar()
        cursor.execute("DELETE [LPUS_ENERGIA].[clientes].[tbl_cadastro_clientes] WHERE N_IDCLIENTE = '"+id_cliente+"'") #Você pode alterar a query e a informação concatenada do ID cliente. Não necessita ser essa consulta e nem este campo.
        cursor.commit()
    except:
        print('Não foi possível deletar os dados da tabela')
    else:
        print('Dados da tabela deletados com sucesso')

query()