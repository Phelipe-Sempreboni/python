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

# Variável com o nome da extensão do arquivo buscado, que neste caso é a extensão (xlsx).
# Notar que conseguimos verificar mais de um tipo de extensão do arquivo excel.
file_extension_one = 'xlsx'
file_extension_two = 'xlsm'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 4

# Variável com o comando para verificar se o repositório origem, o mesmo da variável (source_repository_path) existe.
check_existence_source_repository = os.path.isdir(source_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 5

# Variável com o comando que lista os arquivos no caminho origem, ou seja, na variável (source_repository_path).
files_repository_path = os.path.exists(source_repository_path)
#print(files_repository_path)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Bloco 6

# Importante:
# Este bloco realiza a verificação se o repositório existe, ou seja, o repositório origem da variável (source_repository_path).
# Este bloco realiza a verificação se o arquivo que será lido é da extensão (xlsx ou xlsm), ou seja, um arquivo excel.
# Caso o repositório ou o arquivo não exista, então haverá o erro e uma mensagem amigável será exibida ao usuário, tanto informando a inexistência do repositório ou do arquivo.
# Caso o repositório ou o arquivo não exista, então além da mensagem exibida ao usuário, o script será encerrado neste bloco 6 e não serão executados os demais scripts abaixo.

# Caso a cláusula seja verdadeira, então irá executar o comando abaixo.
# Verifica se o repositório origem existe. Caso existe, irá para o comando abaixo.
if check_existence_source_repository:

    # loop for para verificar os arquivos existentes no repositório origem, ou seja, na variável (source_repository_path).
    for root, dicts, files in os.walk(source_repository_path):

        # loop for para verificar somente os arquivos, assim restringindo e melhorando a verificação.
        for file in files:

            # Caso a cláusula seja verdadeira, o comando abaixo é executado.
            # Realiza a verificação se existe algum arquivo no repositório da variável (). Aqui é qualquer arquivo, não depende da extensão.
            # Caso não exista nenhum arquivo, então será executado um else, com uma mensagem ao usuário e encerramento do script aqui, neste bloco 6.
            if files_repository_path is True:

                # Caso a cláusula seja verdadeira, o comando abaixo é executado.
                # Este (if) realiza um slicing (fatiamento) do nome do arquivo que foi localizado pelos quatro últimos caracteres, que neste caso, seria o (xlsx ou xlsm) que procuramos.
                # Esse slicing (fatiamento) é comparado com a variável (file_extension_one e file_extension_two), que tem como valor (xlsx ou xlsm), ou seja, o valor que procuramos.
                if file[-4:] == file_extension_one or file[-4:] == file_extension_two:

                    # Variável com o comando para abertura dos arquivos excel que desejamos trabalhar, onde é feito com a biblioteca (openpyxl).
                    # Notar que neste caso, apontamos o caminho origem pela variável (source_repository_path) e concatenamos com a variável (file) que são os arquivos, visto que só teremos os arquivos no formato excel na extensão (xlsx ou xlsm) realizado pelo (if).
                    # Para ficar mais visível, neste exemplo, a variável (file) iria trazer os arquivos do caminho origem nomeados como (employee_registration_one.xlsx, employee_registration_two.xlsx e employee_registration_macro.xlsm).
                    # Temos um arquivo de extensão (txt) no caminho origem, porém, não será lido, pois, o if realizou a restrição neste caso.
                    wbk_employee_registration = openpyxl.load_workbook(source_repository_path + '\\' + file)

                    print(wbk_employee_registration)

                # Caso a cláusula seja falsa, então irá executar o comando abaixo.
                # Se o arquivo for diferente das eXtensions (xlsx ou xlsm) então ele segue com a verificação, com o comando abaixo.
                # Caso fosse colocado uma mensagem de erro e um comando para encerrar o script aqui, toda vez que o loop for localizar um arquivo fora dos parâmetros iria encerrar, e temos que continuar essa verificação.
                else:

                    # Continua com os demais comandos caso não haja erro no try, que neste caso, é na abertura do arquivo, indicando sua existência.
                    pass

            # Caso a cláusula seja falsa, então irá executar o comando abaixo.
            # Neste caso, caso não exista nenhum arquivo no caminho origem, então irá exibir a mensagem abaixo para o usuário e o script será encerrado aqui, neste bloco 6.
            else:

                # Mensagem que será exibida ao usuário caso não localize nenhum arquivo no repositório origem.
                print('Nenhum arquivo foi localizado no repositório (' + source_repository_path + '). \nPor favor, verifique o repositório e os arquivos e tente novamente. \nProcesso finalizado sem êxito.')

                # Caso ocorra o erro, então o script é encerrado e não prosseguirá para o próximo passo, assim evitando erros para o usuário posteriormente.
                sys.exit()

# Caso a cláusula seja falsa, então irá executar o comando abaixo.
# Se o repositório não existir, será informado a mensagem abaixo ao usuário.
else:

    # Mensagem ao usuário caso o repositório não exista.
    print('Repositório (' + source_repository_path + ') não existe. \nPor favor, verifique o caminho informado ou se o repositório existe e tente novamente. \nProcesso finalizado sem êxito.')

    # Caso ocorra o erro, então o script é encerrado e não prosseguirá para o próximo passo, assim evitando erros para o usuário posteriormente.
    sys.exit()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
