'''
Esse script acessa a API do site Webmania e nos retorna o resultado.

Nesse script, será necessário indicar o CEP pesquisado no campo request = requests.get("https://webmaniabr.com/api/1/cep/06023080/?app_key=SEU_APP_KEY&app_secret=SEU_APP_SECRET"), onde uma vez alterado o número do CEP, será possível enxergar as informações.

No script 1 desse repositório, temos a declaração de uma variável que que solicitar o CEP e retorna um resultado.

Notar que é necessário solicitar no site um APP KEY e um APP SECRET para utilização e consumo da API.

Espero que essa API ajude.

'''

# Importação das bibliotecas.
import requests
import pandas as pd

# Requisição para consumir informações do site.
request = requests.get("https://webmaniabr.com/api/1/cep/06023080/?app_key=SEU_APP_KEY&app_secret=SEU_APP_SECRET")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

print(resultado)

# Script finalizado
