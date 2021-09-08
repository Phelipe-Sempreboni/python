# Importação das bibliotecas.
import requests
import pandas as pd

# Variável para pesquisar o CEP pelo terminal no Python.
cep = input('Digite o CEP: ')

# Requisição para consumir informações do site.
request = requests.get("https://viacep.com.br/ws/"+cep+"/json/")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

print(resultado)

# Script finalizado