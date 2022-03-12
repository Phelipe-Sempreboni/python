'''

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Created by: Luiz Phelipe Utiama Sempreboni

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Função resumida do script:
- Realizar a exclusão do arquivo do tipo Excel do repositório e/ou servidor e manter os demais arquivos com qualquer tipo de extensão.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Para mais informações sobre as funções do script, consulte o arquivo README.md deste repositório.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ \

'''

# Modelo para excluir um arquivo do tipo Excel e manter os demais arquivos de qualquer tipo de exntensão no repositório e/ou servidor.
# Neste caso o arquivo principal da variável (nome_arquivo) é excluído, e os demais arquivos serão mantidos.
# Altere o nome das variáveis para funcionar corretamente em seu script.

# Importação de biblioteca.
import os  # Módulo para fornecer acesso a funções específicas do sistema para lidar com o sistema de arquivos, processos, planejador, etc.

# Declaração do caminho origem, ou seja, onde os arquivos se encontram.
caminho_origem = r'C:\Windows\Temp\testes'

# Declaração de variável com o nome do arquivo, que neste caso irá facilitar para utilização no decorrer do script.
nome_arquivo = 'Sou-Milionário.xlsx'

# Loop para verificar os arquivos existentes no caminho origem, ou seja, na variável que carrega o caminho.
for root, dirs, files in os.walk(caminho_origem):

    # Este (if) verifica se o (local - root) é o mesmo do repositório (nome_caminho), visto que os arquivos utilizados estão neste repositório.
    # Também certifica que o script não percorra outros repositórios dentro do repositório principal da variável (caminho_origem).
    if root == caminho_origem:

        # Loop para verificar somente os arquivos do for acima.
        for file in files:

            # If para verificar somente o arquivo com o noem da variável (nome_arquivo).
            if file == nome_arquivo:

                # Remove o arquivo que tem o nome da variável (nome_arquivo).
                os.remove(caminho_origem + '\\' + file)

                # Imprimi na tela a mensagem do arquivo que foi excluídos.
                print('Arquivo', file, 'removido com sucesso!')

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('\n=======================================================================================================================================================================\n')

            # Else para manter os demais arquivos que estiverem no caminho origem, ou seja, na variável que carrega o caminho.
            else:

                # Caso os arquivos do repositório não tiverem o nome da variável (nome_arquivo), então o processo irá prosseguir e ignorar estes arquivos.
                continue
