# Testes com regex em Python.

# Biblioteca utilizada: re
# Comando utilizado: sub

# Neste exemplo, utilizando o comando (re.sub), conseguimos localizar expressões e substituir o valor dela.
# Caso ele localize a expressão, ela será substituída.

# O (count=0) serve para substituir todas as expressões que forem iguais pelo orientado no script.
# O (count=0) é o padrão, então, não é necessário colocar.
# O (count=1) substituí somente a primeira expressão encontrada e mantém as outras originais.

import re
string = 'Este é um teste de expressões regulares. O teste é importante.'
print(re.sub(r'teste', 'método', string))

import re
string = 'Este é um teste de expressões regulares. O teste é importante.'
print(re.sub(r'teste', 'método', string, count=0))

import re
string = 'Este é um teste de expressões regulares. O teste é importante.'
print(re.sub(r'teste', 'método', string, count=1))

