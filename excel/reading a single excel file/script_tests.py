'''
Created by: Sempreboni.

Created in: 29/01/2022.

Last modification: 30/01/2022.
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Importing libraries
import os
import openpyxl

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com o caminho do repositório de origem.
source_repository_path = r'C:\Users\pheli\OneDrive\Archives\2 - Github\Repositories\python\excel\reading a single excel file\archives'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com o nome do arquivo, que neste caso é fixo, mas pode ser alterado de acordo com a necessidade.
employees_file_name = 'employee_registration.xlsx'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com a concatenação do repositório e nome do arquivo, para ter o caminho completo até a localização do arquivo.
# Notar que é utilizado duas barras, pois, somente uma barra represente quebra de texto, ou seja, mudança de linha sem sair do contexto atual.
employee_file_repository_path = (source_repository_path + '\\' + employees_file_name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com o comando para verificar se o repositório origem, o mesmo da variável (source_repository_path) existe.
check_existence_source_repository = os.path.isdir(source_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com o comando para verificar se o arquivo origem, o mesmo da variável (employees_file_name) existe.
check_existence_source_file = os.path.isfile(employee_file_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

if check_existence_source_file:
    print('existe')

else:
    print('não existe')