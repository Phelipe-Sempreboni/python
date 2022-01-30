# Modelo excluir arquivos de um determinado repositório (pasta).
# Neste caso o arquivo principal é ignorado, ou seja, mantido no repositório, e os demais arquivos são excluídos.
# Altere o nome das variáveis para funcionar corretamente em seu script.

# Importação de biblioteca.
import os  # Biblioteca para manipular arquivos do sistema operacional do windows.

# Declaração do caminho origem, ou seja, onde os arquivos se encontram.
caminho_origem = r'C:\Users\Zé\Desktop\MeusArquivos'

# Declaração de variável com o nome do arquivo, que neste caso irá facilitar para utilização no decorrer do script.
nome_arquivo = 'Sou-Milionário.xlsx'

# Loop para verificar os arquivos existentes no caminho origem, ou seja, na variável que carrega o caminho.
for root, dirs, files in os.walk(caminho_origem):

    # Loop para verificar somente os arquivos do for acima.
    for file in files:

        # If para verificar somente o arquivo com o noem da variável (nome_arquivo).
        if file == nome_arquivo:

            # Caso o arquivo da variável (nome_arquivo) seja localizado, então o processo irá prosseguir e ignorar este arquivo.
            continue
        
        # Else para excluir os demais arquivos que estiverem no caminho origem, ou seja, na variável que carrega o caminho.
        else:

            # Remove os arquivos que não tem o nome da variável (nome_arquivo).
            os.remove(caminho_origem + '\\' + file)

            # Imprimi na tela a mensagem dos arquivos que foram excluídos.
            print('Arquivo', file, 'removido com sucesso!')