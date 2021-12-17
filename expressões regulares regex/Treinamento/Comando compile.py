# Testes com regex em Python.

# Biblioteca utilizada: re
# Comando utilizado: compile

# Neste exemplo, utilizando o comando (compile), em vez de processar a linha todas vezes com a expressão ('teste'), e possivelmente,
# quando houver muitas expressões e o código ficar lento, conseguimos utilizar o (compile) e processar a linha com a expressão ('teste') somente uma vez, e, utilizar os comandos normalmente.

# No segundo exemplo, criamos uma variável (regex) e utilizamos o comando (compile) com a expressão a ser procurada na váriável principal (string) com a frase.

import re

string = 'Este é um teste de expressões regulares. O teste é importante.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'método', string))

regex = re.compile(r'teste')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub('Método', string))