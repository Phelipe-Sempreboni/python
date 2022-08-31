'''
Esse scritp acessa um site de API com informações do COVID-19 e nos retorna o status de funcionamento atual da API.

Esse script é útil para utilização juntamente com outras informações da API, como a API de consulta de casos nos Estados do Brasil, onde analisamos o status da API.

É realizado um tratamento do formato JSON e disponibilização do resultado tabulado.

Espero que essa API ajude.

'''

# Importação das bibliotecas.
import requests
import pandas as pd

# Requisição para consumir informações do site.
request = requests.get("https://covid19-brazil-api.now.sh/api/status/v1")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

# pd.read_json -> salva e lê o arquivo JSON como uma estrutura de dados do pandas.
# path_or_buf -> Leitura de uma string JSON, neste caso, o objeto/variável que foi convertido de objeto Python para JSON (resultado_tratado) devido as aspas simples para duplas.
# orient -> Tipo de orientação utilizada, neste caso, para colunas.
resultado_em_tabulacao = pd.read_json(
path_or_buf=resultado,
orient='columns'
)

print(resultado_em_tabulacao)

# Script finalizado.
