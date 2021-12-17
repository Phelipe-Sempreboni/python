#!/usr/bin/env python
# coding: utf-8

# In[48]:


# Script desenvolvido no Jupyter Notebook com Python.

# Importar a biblioteca json.
import json

#  Importação do garquivo json. Neste caso direcionado para o local que o arquivo encontra-se.
json_read = open(r'C:\Users\lsempreboni\Desktop\textodesafio.txt')

# Leitura do arquivo json.
json_data = json_read.read()

# Carregamento do arquivo json para a variável results e transformar a lista em um dicionário.
results = json.loads(json_data)

# Impressão do resultado com o dumps, que converte um objeto python em uma string json.
print(json.dumps(results, indent=True))

