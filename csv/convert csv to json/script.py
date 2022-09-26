# Converter um arquivo CSV em JSON.

# Lembrar de ter a biblioteca "pandas" e "json" instaladas, senão realize a instalação.

# Comando para executar a instalação no Jupyter Notebook pip install pandas

#Comando para executar a instalação no Jupyter Notebook pip install json

### Importação das bibliotecas.

import pandas as pd
import json

# Comando para leitura do arquivo CSV. Insira o caminho do arquivo origem.
# Temos um exemplo de caminho inserido.
archive_csv = pd.read_csv(r'C:\Users\pheli\Desktop\case_mkt_campaign_add_decimais.csv')

# Comando para converter o arquivo em JSON. 
# Insira o caminho destino, ou seja, onde você quer que o arquivo seja salvo.
# Temos um exemplo de caminho inserido.

# Neste caso estamos convertendo para JSON e na orientação de tabela, onde existem algumas possibilidades.
archive_csv.to_json(r'C:\Users\pheli\Desktop\case_mkt_campaign_add_decimais.json', orient='table')

# Comando para leitura do arquivo JSON. 
# Insira o caminho do arquivo origem.
# Temos um exemplo de caminho inserido.
archive_json = pd.read_json(r'C:\Users\pheli\Desktop\case_mkt_campaign_add_decimais.json', orient='table')

# Realizar a leitura das 5 primeiras linhas.
archive_json.head()
