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
