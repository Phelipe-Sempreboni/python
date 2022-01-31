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
source_repository_path = r'C:\Users\pheli\OneDrive\Archives\2 - Github\Repositories\python\excel\Reading and printing data from multiple excel files\archives'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 3

# Variável com o nome do arquivo, que neste caso é fixo, mas pode ser alterado de acordo com a necessidade.
file_extension = 'xlsx'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 4

# Variável com o comando que informa os arquivos existente dentro do repositório origem, ou seja, da variável (source_repository_path).
files = os.listdir(source_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 5

# Variável com o comando para verificar se o repositório origem, o mesmo da variável (source_repository_path) existe.
check_existence_source_repository = os.path.isdir(source_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 6

# Variável com o comando para verificar se o arquivo origem, o mesmo da variável (employees_file_name) existe.
check_existence_source_file = os.path.isfile('xlsx')

print(check_existence_source_file)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #