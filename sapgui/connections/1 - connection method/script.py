'''

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Created by: Luiz Phelipe Utiama Sempreboni

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Função resumida do script:
- Realizar uma conexão com o SAP GUI.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ /

Para mais informações sobre as funções do script, consulte o arquivo README.md deste repositório.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------ \

'''

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

# Importação de módulos
import win32com.client  # Módulo para criação de componentes COM (Common Object Model) em Python. Pode-se tanto criar componentes para serem utilizados por outras linguagens/aplicações (servidores) quanto criar objetos previamente existentes (clientes) criados em outras linguagens.
import subprocess  # Módulo subprocess permite que você execute programas externos e inspecione suas saídas com facilidade.
import time  # Módulo provê várias funções relacionadas à tempo, onde neste caso estamos utilizando para a função (sleep).
import sys  # Módulo para fornecer funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de execução do Python e apesar de serem completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os (módulo para manipular o sistema operacional).

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


# Função criada para realizar a conexão com o SAP GUI.
def sap_connection():

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
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = 'USER'

        # Comando interno gerado pelo script do SAP GUI para escrever a senha na tela do sistema.
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = 'PASS'

        # Comanndo para entrar efetivamente no sistema após inserção do usuário e senha.
        session.findById("wnd[0]").sendVKey(0)

    # Caso ocorra qualquer tipo de erro no bloco deste (try), então será acionado o (except), impressa a mensagem abaixo e o programa será encerrado.
    except Exception as error:

        # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
        print(
            '\n=======================================================================================================================================================================\n')

        # Mensagem impressa para na tela para o usuário.
        print(f'Ocorreu um erro ao tentar realizar o processo de login no SAP GUI. '
              f'\nPor favor, verifique e tente novamente.'
              f'\nProcesso finalizado sem êxito.'
              f'\nTipo do erro: {error.__class__}'
              f'\nEssa tela será fechada em 10 segundos')

        # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
        print(
            '\n=======================================================================================================================================================================\n')

        # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
        time.sleep(10)

        # Caso ocorra o erro, então o script é encerrado e não prosseguirá para o próximo passo, assim evitando erros para o usuário posteriormente.
        sys.exit()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


# Chamada da função para login no SAP GUI.
sap_connection()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #