# Converter um arquivo CSV em Excel.
# Lembrar de ter a biblioteca "pandas" e "openpyxl" instaladas, senão realize a instalação.
# Comando para executar a instalação no Jupyter Notebook pip install pandas
# Comando para executar a instalação no Jupyter Notebook pip install openpyxl

### Importação das bibliotecas.

import pandas as pd
import openpyxl

# Comando para leitura do arquivo CSV. Insira o caminho do arquivo origem.
# Temos um exemplo de caminho inserido.
archive_csv = pd.read_csv(r'C:\Users\USUARIO\Desktop\Temp\archive.csv')

# Comando para converter o arquivo em Excel. Insira o caminho destino, ou seja, onde você quer que o arquivo seja salvo.
# Temos um exemplo de caminho inserido.
archive_csv.to_excel(r'C:\Users\USUARIO\Desktop\Temp\archive.csv', index=False)

# Comando para leitura do arquivo Excel. Insira o caminho do arquivo origem.
# Temos um exemplo de caminho inserido.
archive_xlsx = pd.read_excel(r'C:\Users\USUARIO\Desktop\Temp\archive.xlsx')

# Realizar a leitura das 5 primeiras linhas.
archive_xlsx.head()
