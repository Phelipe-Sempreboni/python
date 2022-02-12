'''
Created by: Sempreboni.

Created in: 29/01/2022.

Last modification: 30/01/2022.
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 1

# Importação de bibliotecas.
import os  # biblioteca que realiza operações com arquivos do sistema windows.
import openpyxl  # biblioteca para operações com arquivos do tipo excel.
import sys  # biblioteca que realiza operações nativas do sistema windows.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 2

# Variável com o caminho do repositório de origem.
# Neste caso o caminho é fixo, ou seja, necessita de uma alteração manual.
#source_repository_path = r'C:\Users\pheli\OneDrive\Archives\2 - Github\Repositories\python\excel\Reading and printing data from a single excel file\archives'

# Neste caso o caminho é relativo, ou seja, não necessita de uma alteração manual.
# Este caminho, neste caso, seta o repositório que o este script está locado, logo, os arquivos necessitam estar junto do script no repositório.
path = os.path.abspath(__file__)
source_repository_path = os.path.dirname(path)
print(source_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 3

# Variável com o nome do arquivo, que neste caso é fixo, mas pode ser alterado de acordo com a necessidade.
file_name = 'employee_registration_many_lines.xlsx'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 4

# Variável com a concatenação do repositório e nome do arquivo, para ter o caminho completo até a localização do arquivo.
# Notar que é utilizado duas barras, pois, somente uma barra represente quebra de texto, ou seja, mudança de linha sem sair do contexto atual.
file_repository_path = (source_repository_path + '\\' + file_name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 5

# Variável com o comando para verificar se o repositório origem, o mesmo da variável (source_repository_path) existe.
check_existence_source_repository = os.path.isdir(source_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 6

# Variável com o comando para verificar se o arquivo origem, o mesmo da variável (employees_file_name) existe.
check_existence_source_file = os.path.isfile(file_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #