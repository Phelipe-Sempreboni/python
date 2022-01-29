'''
Created by: Sempreboni.

Created in: 29/01/2022.

Last modification: 29/01/2022.
'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Importing libraries


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com o caminho do repositório de origem.
source_repository_path = r'C:\Users\pheli\OneDrive\Archives\2 - Github\Repositories\python\projects\excel\read files and write data to database\archives'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com o nome do arquivo, que neste caso é fixo, mas pode ser alterado de acordo com a necessidade.
employees_file_name = 'employee_registration.xlsx'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Variável com a concatenação do repositório e nome do arquivo, para ter o caminho completo até a localização do arquivo.
# Notar que é utilizado duas barras, pois, somente uma barra represente quebra de texto, ou seja, mudança de linha sem sair do contexto atual.
employee_file_repository_path = (source_repository_path + '\\' + employees_file_name)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

