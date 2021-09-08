# Importação das bibliotecas.
import requests
import pandas as pd

# Requisição para consumir informações do site.
request = requests.get("https://covid19-brazil-api.now.sh/api/report/v1")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

# pd.read_json -> salva e lê o arquivo JSON como uma estrutura de dados do pandas.
# path_or_buf -> Leitura de uma string JSON, neste caso, o objeto/variável que foi convertido de objeto Python para JSON (resultado_tratado) devido as aspas simples para duplas.
# orient -> Tipo de orientação utilizada, neste caso, para colunas.
resultado_em_tabulacao = pd.read_json(
path_or_buf=resultado,
orient='columns'
)

# pd.json_normalize -> Utiizado para achatar arquivos JSON e transform-los em tipos tabulados.
# pd.json_normalize(data=resultado_em_tabulacao['data'] -> Neste caso, no comando (data=resultado_em_tabulacao['data']), selecionamos somente a chave (data) do arquivo JSON, que é a que contém os valores desejados.
# sep - Por padrão, todos os valores aninhados gerarão nomes de colunas separados por (.), e para separa por outro tipo de separador, neste caso, com o (_), utilizamos o comando (sep).
resultado_tabulado = pd.json_normalize(data=resultado_em_tabulacao['data'].iloc[0:], sep='_')

print(resultado_tabulado)

# Script finalizado.
