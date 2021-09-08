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
