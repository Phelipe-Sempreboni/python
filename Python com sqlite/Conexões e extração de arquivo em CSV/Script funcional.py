# Importando bibliotecas.
import pandas as pd
import sqlite3

# Conexão com o SQLite.
con = sqlite3.connect(r'') # Insira o caminho do local onde encontra-se seu banco de dados.

# Criação de cursor para manipular querys/consultas no banco de dados.
cur = con.cursor()

# Execuçõa de query/consulta no banco de dados.
db_df = pd.read_sql_query('', con) # Insira a query/consulta.

# Conversão da consulta realizada, em uma exportação em formato de arquivo CSV.
db_df.to_csv(r'', index=False) # Insira o caminho do local destino de sua exportação.