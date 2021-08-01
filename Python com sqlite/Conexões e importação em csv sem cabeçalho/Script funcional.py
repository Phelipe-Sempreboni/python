# Importando bibliotecas.
import csv
import sqlite3
import pandas as pd

# Conexão com o SQLite.
con = sqlite3.connect(r'') # Insira o caminho do local onde encontra-se seu banco de dados.

# Criação de cursor para manipular querys/consultas no banco de dados.
cur = con.cursor()

# Leitura do arquivo csv.
df = pd.read_csv(r'C:\Users\br0234206128\Desktop\Teste\0 - Full.csv') # Insira o caminho do local origem do arquivo csv.

# Retirar o cabeçalho e os indexs do arquivo csv.
df.to_csv(r'', header=False, index=False) # Insira o caminho do local origem do arquivo csv.

# Bloco para importar dados de um arquivo csv para uma tabela no banco de dados. Essa importação virá com o cabeçalho do arquivo csv.
with open(r'', encoding="utf8") as csv_file: # Insira o caminho do local origem do arquivo csv.
    csv_reader = csv.reader(csv_file, delimiter=";") # O campo (delimiter) pode ser alterado de acordo com o demilitar de caractres do seu arquivo csv.
    for row in csv_reader:
        to_db = [(row[0]), (row[1]), (row[2]), (row[3]), (row[4]), (row[5]), (row[6]), (row[7]), (row[8]), (row[9])] # Insira a quantidade de colunas que sua tabela possuí no banco de dados e lembre-se que no Python colunas iniciam em [0].
        cur.execute("INSERT INTO TABELA (COLUNAS) VALUES (?,?,?,?,?,?,?,?,?,?);", to_db) # Insira sua query/consulta de inserção dos dados no banco de dados. De acordo com o número de colunas exclua ou insira os (?) em (VALUES).
con.commit() # Comando para comitar/validar as inserções realizadas na tabela.