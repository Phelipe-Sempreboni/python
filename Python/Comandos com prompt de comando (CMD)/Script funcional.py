# Método 1 - Abrir o prompt de comando (CMD).
# Nota: Abrir o cmd em tela de comando no windows com a biblioteca os.
import os
os.system('start /wait cmd')

# Método 2 - Abrir o prompt de comando (CMD).
# Nota: Abrir o cmd em tela de comando no windows com a biblioteca os.
import os
os.system('start cmd')

# Método 3 - Abrir o prompt de comando (CMD).
# Nota: Abrir o cmd em tela de comando no windows com a biblioteca subprocess.
import subprocess
subprocess.run('start', shell = True)

# Método 4 - Abrir o prompt de comando (CMD).
# Nota: Abrir o cmd diretamente no terminal do Python.
import os
os.system('cmd')

# --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # ---------  # ---------  # ---------  # --------- 

# Executar comandos para verificação de diretórios.
# Nota: Teremos o script inicial e um exemplo para verificar repositórios.
# Observação: para todos os cripts abaixo é possível utilizar no lugar do (dir) o (cd) para acessar os diretórios.

#Script inicial:
# Este script executado da maneira abaixo, mostra os repositórios do local.
import os
os.system('dir')

# Script de exemplo 1. Se por exemplo, for inserido o nome de um repositório e (.), ele mostrará todas as pastas ou arquivos dentro daquele repositório.
import os
os.system('dir Desktop.')

#Script de exemplo 2. Se for por exemplo, for inserido o nome de um repositório e aopós (\nome_repositório), ele entrará neste repositório e mostrará todas as pastas ou arquivos dentro daquele repositório.
import os
os.system('dir Desktop\Temp')

# --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # --------- # ---------  # ---------  # ---------  # ---------
