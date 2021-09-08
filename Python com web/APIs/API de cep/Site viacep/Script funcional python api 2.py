# Importação das bibliotecas.
import requests
import pandas as pd

# Requisição para consumir informações do site.
request = requests.get("https://viacep.com.br/ws/06023090/json/")

# Declaração de variável para alocar o resultado da pesquisa.
resultado = request.text

print(resultado)

# Script finalizado