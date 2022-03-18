'''

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Created by: Luiz Phelipe Utiama Sempreboni

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Função resumida do script:
- Realizar uma conexão com o SAP GUI e extração de dados.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Para mais informações sobre as funções do script, consulte o arquivo README.md deste repositório.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ \

'''

# Importação de módulos

import win32com.client  # Módulo para criação de componentes COM (Common Object Model) em Python. Pode-se tanto criar componentes para serem utilizados por outras linguagens/aplicações (servidores) quanto criar objetos previamente existentes (clientes) criados em outras linguagens.
import sys  # Módulo para fornecer funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de execução do Python e apesar de serem completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os (módulo para manipular o sistema operacional).
import os  # Módulo para fornecer acesso a funções específicas do sistema para lidar com o sistema de arquivos, processos, planejador, etc.
import subprocess  # Módulo subprocess permite que você execute programas externos e inspecione suas saídas com facilidade.
import time  # Módulo provê várias funções relacionadas à tempo, onde neste caso estamos utilizando para a função (sleep).
import psutil  # Módulo de plataforma cruzada Python usada para acessar detalhes do sistema e utilitários de processo. É usado para controlar a utilização de vários recursos no sistema
from datetime import datetime  # Módulo fornece classes para manipular datas e tempo de forma simples ou complexas. Apesar de cálculos aritméticos com data e tempo serem suportados, o foco da implementação está na extração eficiente de atributo para formatar resultados e manipulação.


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da data atual para inserção nos campos do SAP GUI, neste caso a variável (data).
# Variável (data_atual) formata o padrão da data.
# Essa data fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
data = datetime.now()
data_atual = data.strftime('%d.%m.%Y')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da data inicial e da data final para inserção nos campos que exigem datas.
# Essa data fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
# Notar que a data_final é a mesma da data_atual, mas pode ser alterado.
data_inicial = '01.10.2020'
data_final = data_atual

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da hora atual para inserção nos campos do SAP GUI, neste caso a variável (hora_atual).
# Essa hora fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
hora_atual = time.strftime('%Hh%M', time.localtime())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o endereço do caminho onde as bases de dados extraídas do SAP GUI serão salvas.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_caminho = r'C:\Windows\Temp\testes'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_principal = r'\Arquivo_1.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI. Neste caso, seria por exemplo, um arquivo complementar da extração ou um segundo arquivo de extração.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_complemento = r'\Arquivo_2.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável (nome_txt) que monta o nome de um arquivo no formato (txt) para indicar no final do script, a data e hora da atualização.
# Variável (nome_txt_caminho) que concatena o caminho dos arquivos da extração do SAP GUI e o arquivo montado com a informação da da variável (nome_txt).
nome_txt = r'\Atualização em ' + data_atual + ' às ' + hora_atual + '.txt'
nome_txt_caminho = nome_caminho + nome_txt

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
print('=======================================================================================================================================================================\n')

# Imprimir mensagem abaixo para o usuário.
print('Iniciando o processo de extração de dados do SAP GUI.\n')

# Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
print('=======================================================================================================================================================================\n')

# Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# Função criada para realizar a finalização processo do excel diretamente na aplicação do gerenciador de tarefas.
def close_excel():

    # Bloco com (try) para tentarmos executar as ações abaixo.
    try:

        # loop for para verificar a existência do processo do windows (EXCEL.EXE).
        for processos in psutil.process_iter():

            # Atribuição de valor a variável (processos_gerais), onde o valor recebido é o processo do windows, e aqui, são todos os processos atuais.
            processos_gerais = processos.as_dict(attrs=['name'])

            # Executar caso a verificação seja verdadeira.
            # Caso o processo do windows que está sendo verificado seja o (EXCEL.EXE), então executar o script abaixo.
            # Encerrando a aplicação do excel diretamente no gerenciador de tarefas caso tenha e/ou ainda esteja ativo.
            if processos_gerais == {'name': 'EXCEL.EXE'} or processos_gerais == {'name': 'EXCEL.exe'} or processos_gerais == {'name': 'excel.EXE'} or processos_gerais == {'name': 'excel.exe'}:

                # Finaliza o processo no windows (EXCEL.EXE).
                os.system('TASKKILL /F /IM EXCEL.EXE\n')

                print('\n=======================================================================================================================================================================\n')

            # Executar caso a verificação for falsa.
            else:

                # Continua a execução script.
                pass

    # Utilizando o (except) com (Exception) para capturar o erro e imprimir na tela pra o usuário.
    except Exception as error_4:

        # Caso haja erro na finalização da aplicação do Excel, então exibirá a mensagem para ao usuário.
        print(f'Não foi possível finalizar o processo do Excel. \nTipo do erro: {error_4.__class__}\n')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# Função criada para realizar a conexão com o SAP GUI.
def sap_connection_and_transaction():

    # Bloco com (try) para tentarmos executar as ações abaixo.
    try:

        # Caminho onde o executável do SAP GUI está locado. Varia de máquina para máquina.
        path = r"D:\Programming\SAP\FrontEnd\SapGui\saplogon.exe"

        # Realiza a abertura de um processo, neste caso o processo de execução do executável do SAP GUI.
        subprocess.Popen(path)

        # Realiza uma contagem de 5 segundos até execução do processo abaixo.
        time.sleep(5)

        # Variável que define o objeto, neste caso, o (SAPGUI), para execução do objeto SAP GUI.
        sap_gui_auto = win32com.client.GetObject('SAPGUI')

        # Este (if) verifica se não existe nenhum tipo de objeto da variável (sap_gui_auto).
        if not type(sap_gui_auto) == win32com.client.CDispatch:
            return

        # Aqui utilizamos a variável (sap_gui_auto) junto do método (GetScriptingEngine).
        # Essa variável (application) executa a tecnologia, ou seja, o SAP GUI, fazendo com que o sistema seja aberto.
        application = sap_gui_auto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            sap_gui_auto = None
            return sap_gui_auto

        # Aqui utilizamos a variável (application) com o método (OpenConnection).
        # Essa variável (connection) executa o módulo do SAP GUI, ou seja, o que você precisa realmente se conectar, por exemplo, CCS PRODUTIVO.
        connection = application.OpenConnection("SAP", True)
        if not type(connection) == win32com.client.CDispatch:
            application = None
            sap_gui_auto = None
            return application, sap_gui_auto

        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            sap_gui_auto = None
            return connection, application, sap_gui_auto

        # Comando interno gerado pelo script do SAP GUI para escrever o usuário na tela do sistema.
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = 'LSEMPREBONI'

        # Comando interno gerado pelo script do SAP GUI para escrever a senha na tela do sistema.
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = 'Estudar123+'

        # Comanndo para entrar efetivamente no sistema após inserção do usuário e senha.
        session.findById("wnd[0]").sendVKey(0)

        # Comando para escrever a transação IW59.
        session.findById("wnd[0]/tbar[0]/okcd").text = "iW59"

        # Comanndo para entrar efetivamente na transação IW59.
        session.findById("wnd[0]").sendVKey(0)

        # Comando para preencher a data de notificação inicial com a varíável (data_inicial), que está pré definida no início do script.
        # Essa data está no primeiro bloco do SAP GUI na transação, no bloco nomeado como (Notification Selection).
        session.findById("wnd[0]/usr/ctxtDATUV").text = data_inicial

        # Comando para preencher a data de notificação final com a varíável (data_final), que está pré definida no início do script.
        # Essa data está no primeiro bloco do SAP GUI na transação, no bloco nomeado como (Notification Selection).
        session.findById("wnd[0]/usr/ctxtDATUB").text = data_final

        # Comando para executar a transação.
        session.findById("wnd[0]/tbar[1]/btn[8]").press()

        # Comando para selecionar todos os dados que foram retornados após executar a transação.
        session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectAll()

        # Comando para abrir o menu de opções e selecionar a exportação de dados, que neste caso será exportação com o excel.
        session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").contextMenu()

        # Comando para selecionar dentro do menu o tipo da exportação, que será uma extensão excel.
        session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").selectContextMenuItem("&XXL")

        # Comando para executar e realizar a extração dos dados.
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        # Comando para definir o caminho para onde a extração de dados no formato excel será alocada.
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = nome_caminho

        # Comando para definir o nome do arquivo no formato excel.
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = nome_arquivo_principal

        # Comando para executar e realizar a exportação dos dados no formato excel para o repositório de destino.
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        # Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
        # Neste caso, é para o sistema conseguir responder à tempo de fechar o arquivo Excel, pois, se o arquivo for muito grande a máquina "fraca", então pode travar o excel e o processo do script.
        time.sleep(5)

        # Executa a função para realizar a finalização processo do excel diretamente na aplicação do gerenciador de tarefas.
        close_excel()

        # Encerra a tela de login do SAP.
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]").close()
        session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()

    # Caso ocorra qualquer tipo de erro no bloco deste (try), então será acionado o (except), impressa a mensagem abaixo e o programa será encerrado.
    except Exception as error_1:

        # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
        print(
            '\n=======================================================================================================================================================================\n')

        # Mensagem impressa para na tela para o usuário.
        print(f'Ocorreu um erro ao tentar realizar o processo no SAP GUI. '
              f'\nPor favor, verifique e tente novamente.'
              f'\nProcesso finalizado sem êxito.'
              f'\nTipo do erro: {error_1.__class__}'
              f'\nEssa tela será fechada em 10 segundos')

        # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
        print(
            '\n=======================================================================================================================================================================\n')

        # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
        time.sleep(10)

        # Caso ocorra o erro, então o script é encerrado e não prosseguirá para o próximo passo, assim evitando erros para o usuário posteriormente.
        sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# Bloco de try para tentar realizar a execução abaixo.
try:

    # 1º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
    for root, dirs, files in os.walk(nome_caminho):

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # 2º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
        # Este (if) verifica se o (local - root) é o mesmo do repositório (nome_caminho), visto que os arquivos utilizados estão neste repositório.
        # Também certifica que o script não percorra outros repositórios dentro do repositório principal da variável (nome_caminho).
        if root == nome_caminho:

            # Imprimir mensagem de validação do repositório atual ao usuário.
            print('Validação do repositório atual: ' + root + '.\n')

            # Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
            time.sleep(5)

            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
            print('=======================================================================================================================================================================\n')

            # Imprimir mensagem de validação do repositório atual ao usuário.
            print('Iniciando o processo de exclusão de arquivos do tipo Excel, das extensões (xlsx e xlsm) do repositório.\n')

            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
            print('=======================================================================================================================================================================\n')

            # Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
            time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # Essa variável foi criada para caso não hajam arquivos no repositório.
        # Caso não hajam arquivos, o valor retornado seria uma lista vazia, ou seja, o valor [].
        # Se tentarmos utilizar (if files == '' or files == '[]'), não acontecerá nada, pois o valor retornado não é entendido pelo comando do (if).
        # Por isso a variável com a lista vazia foi criada, para conseguirmos comparar o valor vazio da variável (files) com um valor realmente vazio, neste caso, comparação com a variável (lista_vazia).
        # O (if) utilizando a comparação do valor vazio com a lista vazia está logo abaixo.
        lista_vazia_1 = []

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # 3º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
        # Este (if) verifica se existem arquivos de qualquer tipo de extensão no repositório da variável (nome_caminho).
        # Caso não exista nenhum tipo de arquivo, uma mensagem é exibida ao usuário; o script irá aguardar 30 segundos e será encerrado sem prosseguir para os passos seguintes.
        # Aqui o resultado da variável (files) é devolvido em formato de lista, logo, não é necessário realizar um (loop for) para verificar os arquivos; é verificado somente se o valor da lista é vazio ou não.
        # Aqui utilizamos a variável (lista_vazia) para comparar como valor da variável (files), onde caso seja vazio irá comparar com a variável (lista_vazia).
        if files == lista_vazia_1:

            # Imprimir mensagem abaixo para o usuário.
            print('Não existe nenhum tipo de arquivo de arquivo neste repositório. '
                  '\nPor favor, verifique o repositóro e tente novamente. '
                  '\nProcesso executado sem êxito. '
                  '\nEssa tela será fechada em 30 segundos. \n')

            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
            print('=======================================================================================================================================================================\n')

            # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
            time.sleep(30)

            # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
            sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # 4º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
        # Este (elif) verifica se existem arquivos de qualquer tipo de extensão no repositório.
        # Caso existam arquivos, mas nenhum com a extensão (xlsx/xlsm) do tipo excel, ele irá exibir a mensagem abaixo para o usuário, que não existe um arquivo excel nesse repositório.
        # Logo após a exibição da mensagem, irá começar um contador de 30 segundos e o código será encerrado para não comprometer os processos abaixo.
        # O primeiro (elif) verifica se a variável (lista_vazia_1) é diferente de vazia e se for verdadeiro, então seguirá para a declaração das variáveis e o if aninhado com este (elif) abaixo.
        # A variável (localizar_extensao_1) procura por arquivos da extensão (xlsx/xlsm) dentro da variável (files) que aponta para os arquivos do repositório.
        # Logo após, a variável (localizar_extensao_1) e (lista_vazia_2) são comparadas.
        # Caso a variável (localizar_extensao_1) seja igual a variável (lista_vazia_2), então o comando irá prosseguir para o (if aninhado com este if) abaixo.
        # Este (if) quer dizer que o valor de ambas variáveis são vazias, logo, irá imprimir a mensagem abaixo para o usuário, que não existe um arquivo com a extensão (xlsx/xlsm).
        # NOTAR QUE TEMOS OUTRO (ELIF) ABAIXO, PORÉM ESTÁ ANINHADO DENTRO DESTE (IF -> if localizar_extensao_1 == lista_vazia_2 and localizar_extensao_2 == lista_vazia_3).
        elif files != lista_vazia_1:

            # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
            lista_vazia_2 = []

            # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
            lista_vazia_3 = []

            # Monta a variável que busca dentro da lista variável (files) se existe algum arquivo com a extensão (xlsx) do tipo excel.
            localizar_extensao_1 = [extensao_1 for extensao_1 in files if '.xlsx' in extensao_1]

            # Monta a variável que busca dentro da lista variável (files) se existe algum arquivo com a extensão (xlsm) do tipo excel.
            localizar_extensao_2 = [extensao_2 for extensao_2 in files if '.xlsm' in extensao_2]

            # Compara se ambas variáveis são iguais, que neste caso se ambas tem o valor de uma lista vazia, ou seja, igual à [].
            if localizar_extensao_1 == lista_vazia_2 and localizar_extensao_2 == lista_vazia_3:

                # Imprimir mensagem abaixo para o usuário.
                print('Não existe um arquivo com a extensão do tipo (xlsx/xlsm) do excel nesse repositório. '
                      '\nPor favor, verifique o repositóro e tente novamente. '
                      '\nProcesso executado sem êxito. '
                      '\nEssa tela será fechada em 30 segundos. \n')

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('=======================================================================================================================================================================\n')

                # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
                time.sleep(30)

                # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
                sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

            # 5º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
            # Este (elif) aninhado com o (if) acima, verifica se existem arquivos do tipo de extensão (xlsx/xlsm) do excel no repositório atual.
            # Caso existam arquivos da extensão (xlsx/xlsm) do tipo excel neste repositório, então ele prosseguirá para o (try / except) aninhado, onde realiza a exclusão dos arquivos da extensão (xlsx/xlsm).
            elif files != lista_vazia_1:

                # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
                lista_vazia_4 = []

                # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
                lista_vazia_5 = []

                # Monta a variável que busca dentro da lista variável (files) se existe algum arquivo com a extensão (xlsx) do tipo excel.
                localizar_extensao_3 = [extensao_3 for extensao_3 in files if '.xlsx' in extensao_3]

                # Monta a variável que busca dentro da lista variável (files) se existe algum arquivo com a extensão (xlsm) do tipo excel.
                localizar_extensao_4 = [extensao_4 for extensao_4 in files if '.xlsm' in extensao_4]

                # Compara se ambas variáveis são iguais, que neste caso se ambas tem o valor de uma lista vazia, ou seja, igual à [].
                if localizar_extensao_3 != lista_vazia_4 or localizar_extensao_4 != lista_vazia_5:

                    # loop for para restringir a buscar somente por arquivos no repositório atual.
                    for file in files:

                        # Transformando os valores resultantes da variável (file) em valores de strings minusculas.
                        file = file.lower()

                        # Este (if) realiza o slicing (fatiamento) da string do nome arquivo e deixa somente os 4 últimos caracateres, neste caso, deixando somente a extensão do arquivo excel, ou seja (xlsx/xlsm).
                        if file[-4:] == 'xlsx' or file[-4:] == 'xlsm':

                            # Remove os arquivos com as extensões (xlsx/xlsm) do tipo excel.
                            os.remove(nome_caminho + '\\' + file)

                            # Imprimir mensagem abaixo para o usuário.
                            print('Arquivo: (' + file + ') removido com sucesso. \n')

                            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                            print('=======================================================================================================================================================================\n')

                            # Pausar ou colocar para dormir a execução do script por 3 segundos até a execução do comando abaixo.
                            time.sleep(3)

                        # Este (elif) verificar se os arquivos do repositório tem extensões diferente de (xlsx/xlsm) do tipo excel.
                        # Caso o repositório contenha arquivos que não sejam dessas extensões, então executará o comando (continue) abaixo.
                        # O comando (continue) ignora os arquivos que não tem a extensão do tipo (xlsx/xlsm), ou seja, sem fazer nenhuma alteração, no caso, remoção de arquivos.
                        elif file[-4:] != 'xlsx' or file[-4:] != 'xlsm':

                            # Caso o (elif) acima tenha o valor da cláusula (verdadeiro), então o comando prosseguirá sem fazer nenhuma alteração, no caso, remoção de arquivos.
                            continue

                        # Este (else) só será executado caso as cláusulas acima não sejam (verdadeiras).
                        else:

                            # Imprimir mensagem abaixo para o usuário.
                            # Notar que neste caso não iremos apontar uma mensagem que não existem arquivos do tipo da extensão (xlsx/xlsm) do tipo excel.
                            # Não será impressa uma mensagem assim, pois, nos (ifs) acima já verificamos se existem arquivos do tipo de extensão (xls/xlsm).
                            # Então, caso não seja excluído um arquivo e pare neste (else), é realmente porquê não foi possível deletar o arquivo por motivo, por exemplo, de estar aberto no momento da execução do comando de remoção.
                            # Neste caso o comando será encerrado neste ponto para não prejudicar os próximos passos do processo.
                            print('Não foi possível excluir o arquivo: ' + file + '\nPor favor, verifique, por exemplo, se o arquivo não está aberto ou outro motivo e tente novamente. '
                                                                                  '\nProcesso executado sem êxito. '
                                                                                  '\nEssa tela será fechada em 30 segundos. \n')

                            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                            print('=======================================================================================================================================================================\n')

                            # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
                            time.sleep(30)

                            # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
                            sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Este é o (except) do (try) geral, ou seja, é o que fecha o primeiro comando (try) aberto.
# Caso nenhuma das verificações dentro do (try) geral for verdadeira, então irá ativar este (except).
except Exception as error_2:

    # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
    print('=======================================================================================================================================================================\n')

    print(f'Não foi possível realizar o processo de validação de repositório e arquivos. '
          f'\nPor favor, verifique os seguintes pontos que podem estar causando o erro: '
          f'\n1 - Verifique se o repositório indicado no caminho da variável (nome_caminho) realmente existe. '
          f'\n2 - Verifique se existem arquivos com as extensões (xlsx/xlsm) no repositório. '
          f'\n3 - Verifique se os arquivos não estão com erro de formato. '
          f'\nEssa tela será fechada em 30 segundos. '
          f'\nTipo do erro: {error_2.__class__}\n')

    # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
    print('=======================================================================================================================================================================\n')

    # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
    time.sleep(30)

    # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
    sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
# O comando abaixo é para verificação, abertura e login do SAP GUI.
time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Bloco de try para tentar realizar a execução abaixo.
try:

    # 1º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
    for root, dirs, files in os.walk(nome_caminho):

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # 2º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
        # Este (if) verifica se o (local - root) é o mesmo do repositório (nome_caminho), visto que os arquivos utilizados estão neste repositório.
        # Também certifica que o script não percorra outros repositórios dentro do repositório principal da variável (nome_caminho).
        if root == nome_caminho:

            # Imprimir mensagem de validação do repositório atual ao usuário.
            print('Realizando a verificação se todos os arquivos do tipo Excel foram excluídos do repositório para prosseguir com o processo. Por favor, aguarde.\n')

            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
            print('=======================================================================================================================================================================\n')

            # Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
            time.sleep(5)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # Essa variável foi criada para caso não hajam arquivos no repositório.
        # Caso não hajam arquivos, o valor retornado seria uma lista vazia, ou seja, o valor [].
        # Se tentarmos utilizar (if files == '' or files == '[]'), não acontecerá nada, pois o valor retornado não é entendido pelo comando do (if).
        # Por isso a variável com a lista vazia foi criada, para conseguirmos comparar o valor vazio da variável (files) com um valor realmente vazio, neste caso, comparação com a variável (lista_vazia).
        # O (if) utilizando a comparação do valor vazio com a lista vazia está logo abaixo.
        lista_vazia_1 = []

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # 3º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
        # Este (if) verifica se existem arquivos de qualquer tipo de extensão no repositório.
        # Caso existam arquivos, mas nenhum com a extensão (xlsx/xlsm) do tipo excel, ele irá exibir a mensagem abaixo para o usuário, que não existe um arquivo excel nesse repositório.
        # Logo após a exibição da mensagem, irá começar um contador de 30 segundos e o código será encerrado para não comprometer os processos abaixo.
        # A variável (localizar_extensao_1) procura por arquivos da extensão (xlsx/xlsm) dentro da variável (files) que aponta para os arquivos do repositório.
        # Logo após, a variável (localizar_extensao_1) e (lista_vazia_2) são comparadas.
        # Caso a variável (localizar_extensao_1) seja igual a variável (lista_vazia_2), então o comando irá prosseguir para o (if aninhado com este if) abaixo.
        # Este (if) quer dizer que o valor de ambas variáveis são vazias, logo, irá imprimir a mensagem abaixo para o usuário, que não existe um arquivo com a extensão (xlsx/xlsm).
        if files == lista_vazia_1 or files != lista_vazia_1:

            # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
            lista_vazia_2 = []

            # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
            lista_vazia_3 = []

            # Monta a variável que busca dentro da lista variável (files) se existe algum arquivo com a extensão (xlsx) do tipo excel.
            localizar_extensao_1 = [extensao_1 for extensao_1 in files if '.xlsx' in extensao_1]

            # Monta a variável que busca dentro da lista variável (files) se existe algum arquivo com a extensão (xlsm) do tipo excel.
            localizar_extensao_2 = [extensao_2 for extensao_2 in files if '.xlsm' in extensao_2]

            # Compara se ambas variáveis são iguais, que neste caso se ambas tem o valor de uma lista vazia, ou seja, igual à [].
            if localizar_extensao_1 == lista_vazia_2 and localizar_extensao_2 == lista_vazia_3:

                # Imprimir mensagem de validação do repositório atual ao usuário.
                print('Realizando a abertura, login e processo de extração de dados no SAP GUI. Por favor, aguarde. \n')

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('=======================================================================================================================================================================\n')

                # Caso a cláusula seja verdadeira, ou seja, não existam arquivos do tipo Excel com as exntensões (xlsx/xlsm) no repositório, é realizada a chamada da função (sap_connection()).
                # Ou seja, é realizada a abertura do SAP GUI e a tentativa de conexão.
                sap_connection_and_transaction()

                # Pausar ou colocar para dormir a execução do script por 5 segundos até a execução do comando abaixo.
                time.sleep(5)

            # Caso a cláusula seja falsa, ou seja, ainda existam arquivos do tipo Excel com as exntensões (xlsx/xlsm) no repositório, é exibida uma mensagem ao usuário e o script encerrado.
            else:

                # Imprimir mensagem abaixo para o usuário.
                print('Ainda existem arquivos do tipo Excel no repositório. '
                      '\nPor favor, verifique e tente novamente. '
                      '\nProcesso executado sem êxito. '
                      '\nEssa tela será fechada em 30 segundos. \n')

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('=======================================================================================================================================================================\n')

                # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
                time.sleep(30)

                # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
                sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Este é o (except) do (try) geral, ou seja, é o que fecha o primeiro comando (try) aberto.
# Caso nenhuma das verificações dentro do (try) geral for verdadeira, então irá ativar este (except).
except Exception as error_3:

    # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
    print('=======================================================================================================================================================================\n')

    # Imprimir mensagem abaixo para o usuário.
    print(f'Não foi possível realizar o processo de abertura e login no SAP GUI. '
          f'\nPor favor, verifique e tente novamente. ' 
          f'\nTipo do erro: {error_3.__class__}\n')

    # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
    print('=======================================================================================================================================================================\n')

    # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
    time.sleep(30)

    # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
    sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
