# Testes com regex em Python.

# Biblioteca utilizada: re
# Comando utilizado: findall

# Neste exemplo, utilizando o comando (re.findall), conseguimos localizar todas as expressões procuradas.
# Caso ele localize a expressão, e tenhamos mais expressões iguais, com esse comando (findall) localizaremos todas.

import re
string = 'Este é um teste de expressões regulares. O teste é importante.'
print(re.findall(r'teste', string))