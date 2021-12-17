# Testes com regex em Python.

# Biblioteca utilizada: re
# Comando utilizado: search

# Neste exemplo, utilizando o comando (re.search), conseguimos localizar a primeira expressão procurada.
# Caso ele localize a expressão, e tenhamos mais expressões iguais, com esse comando (search) só localizará a primeira.

import re
string = 'Este é um teste de expressões regulares. O teste é importante.'
print(re.search(r'teste', string))