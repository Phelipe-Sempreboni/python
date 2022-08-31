'''
Esse script acessa a API do site Webmania e nos retorna o resultado.

Ao rodar o script será solicitado que informe o CEP no terminal do Python, onde uma vez informado, siga com o ENTER e terá um retorno, tanto válido quanto inválido, onde irá depender do CEP digitado.

Notar que é necessário solicitar no site um APP KEY e um APP SECRET para utilização e consumo da API.

Espero que essa API ajude.

'''

# Importação das bibliotecas.
import requests
import pandas as pd

# Variável para pesquisar o CEP pelo terminal no Python.
cep = input('Digite o CEP: ')

# Requisição para consumir informações do site.
request = requests.get("https://webmaniabr.com/api/1/cep/"+cep+"/?app_key=SEU_APP_KEY&app_secret=SEU_APP_SECRET")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

print(resultado)

# Script finalizado
