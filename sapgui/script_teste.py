import win32com.client  # Módulo para criação de componentes COM (Common Object Model) em Python. Pode-se tanto criar componentes para serem utilizados por outras linguagens/aplicações (servidores) quanto criar objetos previamente existentes (clientes) criados em outras linguagens.
import subprocess  # Módulo subprocess permite que você execute programas externos e inspecione suas saídas com facilidade.
import time  # Módulo provê várias funções relacionadas à tempo, onde neste caso estamos utilizando para a função (sleep).
import getpass  # Módulo para mascarar a senha quando é inserida no terminal.


# Função criada para realizar a conexão com o SAP GUI.
def sap_connection():

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


        login = input('Informe seu login: ')
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = login

        password = getpass.getpass()
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password

        session.findById("wnd[0]").sendVKey(0)

    except Exception as error_2:

        print(f'erro {error_2.__class__}')


sap_connection()