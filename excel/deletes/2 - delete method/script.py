# Modelo para excluir um arquivo do tipo Excel de um determinado repositório (pasta).
# Neste caso o arquivo principal da variável (nome_arquivo) é o arquivo do tipo Excel que será excluído, e os demais arquivos serão mantidos.
# Altere o nome das variáveis para funcionar corretamente em seu script.

# Importação de biblioteca.
import os  # Biblioteca para manipular arquivos do sistema operacional do windows.

# Declaração do caminho origem, ou seja, onde os arquivos se encontram.
caminho_origem = r'C:\Windows\Temp\testes'

# Declaração de variável com o nome do arquivo, que neste caso irá facilitar para utilização no decorrer do script.
nome_arquivo = 'Sou-Milionário.xlsx'

# Loop para verificar os arquivos existentes no caminho origem, ou seja, na variável que carrega o caminho.
for root, dirs, files in os.walk(caminho_origem):

    # Loop para verificar somente os arquivos do for acima.
    for file in files:

        # If para verificar somente o arquivo com o noem da variável (nome_arquivo).
        if file == nome_arquivo:

            # Remove o arquivo que tem o nome da variável (nome_arquivo).
            os.remove(caminho_origem + '\\' + file)

            # Imprimi na tela a mensagem do arquivo que foi excluídos.
            print('Arquivo', file, 'removido com sucesso!')

        # Else para manter os demais arquivos que estiverem no caminho origem, ou seja, na variável que carrega o caminho.
        else:

            # Caso os arquivos do repositório não tiverem o nome da variável (nome_arquivo), então o processo irá prosseguir e ignorar estes arquivos.
            continue
