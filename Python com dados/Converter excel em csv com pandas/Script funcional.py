# Método para converter um arquivo CSV em EXCEL.

# Importação da biblioteca.
import pandas as pd

data = pd.read_excel(r'') # Comando para leitura do arquivo excel. Insira o caminho do arquivo origem. 

data.to_csv(r'', index=False) # Comando para converter o arquivo em csv. Insira o caminho do arquivo destino.
