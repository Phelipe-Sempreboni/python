'''
Esse script acessa a API do site ViaCEP e nos retorna o resultado.

Ao rodar o script será solicitado que informe o CEP no terminal do Python, onde uma vez informado, siga com o ENTER e terá um retorno, tanto válido quanto inválido, onde irá depender do CEP digitado.

Espero que essa API ajude.

'''

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
