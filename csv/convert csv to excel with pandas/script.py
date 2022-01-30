# Método para converter um arquivo CSV em EXCEL.

# Importação da biblioteca.
import pandas as pd

data = pd.read_csv(r'') # Comando para leitura do arquivo csv. Insira o caminho do arquivo origem. 

data.to_excel(r'', index=False) # Comando para converter o arquivo em Excel. Insira o caminho do arquivo destino.