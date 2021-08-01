# Importando bibliotecas.
import csv
import sqlite3
import pandas as pd

# Criação da função (sqlite).
def sqlite():

    # Conexão com o SQLite.
    con = sqlite3.connect(r'C:\Temp\SQLiteStudio\SAP.db') # Insira o caminho do local onde encontra-se seu banco de dados.
    
    # Criação de cursor para manipular querys/consultas no banco de dados.
    cur = con.cursor()

    # Execução de um cursor que executará a query.
    # Insira sua query/consulta.
    cur.executescript('')

    # Leitura do arquivo csv.
    df = pd.read_csv(r'') # Insira o caminho do local origem do arquivo csv.

    # Retirar o cabeçalho e os indexs do arquivo csv.
    df.to_csv(r'', header=False, index=False) # Insira o caminho do local origem do arquivo csv.

    # Bloco para importar dados de um arquivo csv para uma tabela no banco de dados. Essa importação virá com o cabeçalho do arquivo csv.
    with open(r'', encoding="utf8") as csv_file: # Insira o caminho do local origem do arquivo csv.
        csv_reader = csv.reader(csv_file, delimiter=";") # O campo (delimiter) pode ser alterado de acordo com o demilitar de caractres do seu arquivo csv.
        for row in csv_reader:
            to_db = [(row[0]), (row[1]), (row[2]), (row[3]), (row[4]), (row[5]), (row[6]), (row[7]), (row[8]), (row[9])] # Insira a quantidade de colunas que sua tabela possuí no banco de dados e lembre-se que no Python colunas iniciam em [0].
            cur.execute("INSERT INTO tb_iw59_medidores (nota, instalacao, tipo_de_nota, code_codificacao, status_usuario, data_da_nota, modificado_em, encerram_por_data, centro_trabalho, cidade) VALUES (?,?,?,?,?,?,?,?,?,?);", to_db) # Insira sua query/consulta de inserção dos dados no banco de dados. De acordo com o número de colunas exclua ou insira os (?) em (VALUES).
    con.commit() # Comando para comitar/validar as inserções realizadas na tabela.

    con.close() # Fechar conexão.

sqlite() # Comando para executar a função (sqlite).