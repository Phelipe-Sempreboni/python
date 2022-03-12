'''

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Created by: Luiz Phelipe Utiama Sempreboni

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Função resumida do script:
- Realizar a exclusão de arquivos do repositório e/ou servidor e mantém o arquivo do tipo Excel.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Para mais informações sobre as funções do script, consulte o arquivo README.md deste repositório.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ \

'''

# Modelo para excluir arquivos de qualquer tipo de extensão de um determinado repositório (pasta) e manter o arquivo do tipo Excel.
# Neste caso o arquivo principal da variável (nome_arquivo) é ignorado, ou seja, mantido no repositório, e os demais arquivos serão excluídos.
# Altere o nome das variáveis para funcionar corretamente em seu script.

# Importação de biblioteca.
import os  # Módulo para fornecer acesso a funções específicas do sistema para lidar com o sistema de arquivos, processos, planejador, etc.
import sys  # Módulo para fornecer funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de execução do Python e apesar de serem completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os (módulo para manipular o sistema operacional).
import time  # Módulo provê várias funções relacionadas à tempo, onde neste caso estamos utilizando para a função (sleep).

# Declaração do caminho origem, ou seja, onde os arquivos se encontram.
caminho_origem = r'C:\Windows\Temp\testes'

# Declaração de variável com o nome do arquivo, que neste caso irá facilitar para utilização no decorrer do script.
nome_arquivo = 'Sou-Milionário.xlsx'

# Variável com o comando para verificar se o repositório origem, o mesmo da variável (source_repository_path) existe.
verificao_existencia_repositorio = os.path.isdir(caminho_origem)

# Bloco de try para tentar realizar a execução abaixo.
try:

    # Caso a cláusula seja verdadeira, então irá executar o comando abaixo.
    # Verifica se o repositório origem existe. Caso existe, irá para o comando abaixo.
    if verificao_existencia_repositorio:

        # Loop para verificar os arquivos existentes no caminho origem, ou seja, na variável que carrega o caminho.
        for root, dirs, files in os.walk(caminho_origem):

                # Este (if) verifica se o (local - root) é o mesmo do repositório (nome_caminho), visto que os arquivos utilizados estão neste repositório.
                # Também certifica que o script não percorra outros repositórios dentro do repositório principal da variável (caminho_origem).
                if root == caminho_origem:

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
                            print('Arquivo', file, 'removido com sucesso!\n')

                            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                            print('=======================================================================================================================================================================\n')

    # Este (else) será executado caso a cláusula do (if) seja falsa.
    # Se a cláusula for falsa, então quer dizer que o repositório não existe, logo haverá mensagem abaixo.
    else:

        # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
        print('=======================================================================================================================================================================\n')

        # Mensagem ao usuário caso o repositório não exista.
        print('Repositório (' + caminho_origem + ') não existe. '
        f'\nPor favor, verifique o caminho informado ou se o repositório existe e tente novamente. '
        f'\nProcesso finalizado sem êxito. '
        f'\nEssa tela será fechada em 10 segundos. ')

        # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
        print('\n=======================================================================================================================================================================\n')

        # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
        time.sleep(10)

        # Caso ocorra o erro, então o script é encerrado e não prosseguirá para o próximo passo, assim evitando erros para o usuário posteriormente.
        sys.exit()

# Este (except) só será executado caso os (ifs) dentro do (loop for) não sejam suficientes para capturar possíveis erros, logo, o (excep) será ativado.
except Exception as error:

    #Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
    print('=======================================================================================================================================================================\n')

    print('Não foi possível realizar o processo de exclusão de arquivos. '
    f'\nPor favor, verifique e tente novamente. '
    f'\nProcesso finalizado sem êxito. '
    f'\nEssa tela será fechada em 10 segundos. '
    f'\nTipo do erro: {error.__class__}')

    # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
    print('\n=======================================================================================================================================================================\n')
