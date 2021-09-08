'''
Esse script acessa a API do site ViaCEP e nos retorna o resultado.

Nesse script, será necessário indicar o CEP pesquisado no campo (request = requests.get("https://viacep.com.br/ws/06023090/json/")), onde uma vez alterado o número do CEP, será possível enxergar as informações.

No script 1 desse repositório, temos a declaração de uma variável que que solicitar o CEP e retorna um resultado.

Espero que essa API ajude.

'''

# Importação das bibliotecas.
import requests
import pandas as pd

# Requisição para consumir informações do site.
request = requests.get("https://viacep.com.br/ws/06023090/json/")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

print(resultado)

# Script finalizado
