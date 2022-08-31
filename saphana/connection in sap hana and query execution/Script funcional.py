# Importação da biblioteca. 
# Certifique-se de ter a biblioteca instalada.
import pyhdb

# Essa função traz/chama outro arquivo que contém a senha, visando não deixar exposta na aplicação.
# Caso não queira utilizar esse método e inserir diretamente a senha na conexão, exclua esse bloco e insira a senha diretamente no bloco (def connect) em (passoword).
def pass_location():
    pass_file = "" # Insira o caminho do arquivo com a senha.
    file = open(pass_file, 'r') # Leiteura do arquivo com read.
    return file.read()

# Realiza a conexão com o Sap Hana.
def connect():
    try:
        connection = pyhdb.connect(
            host = "", # Insira o server.
            port=,  # Insira a porta, normalmente númerica, caso não seja, utilize o ("") para digitar a localidade da porta.
            user="", # Insira o usuário.
            password=pass_location() # Aqui estamos utilizando o bloco (pass_location) que busca a senha em outro arquivo, caso não queira exclua o bloco e insira a senha.
            )
        return connection.cursor()
    except:
        return 1

# Executa a query no Sap Hana.
def query_exec():
    
    #A query de exemplo abaixo lista 10 instalacoes da tabela de dados mestres de instalacao
    cursor = connect()
    cursor.execute("SET SCHEMA SAPBP1") # Insira o schema do banco de dados.
    cursor.execute("SELECT top 10 "'"/BIC/EPINSTALA"'" \
                    from "'"SAPBP1"'"."'"/BIC/PEPINSTALA"'" ") # Insira a query.
  
    result = cursor.fetchall() # Retorna todos os resultados.
    cursor.close() # Encerra o cursor.
    return result


if __name__ == '__main__':
    
    connect() # Execução a função de conexão.
    resultado = query_exec() # Executa a função de execução da query.
    print (resultado) # Imprimi o resultado no terminal.