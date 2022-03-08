'''

created by: Luiz Phelipe Utiama Sempreboni

Script para:
- Conexão com o SAP GUI com solicitação de usuário e senha para o usuário.
- Limpeza e/ou exclusão de arquivos anteriores do repositório atual que os arquivos serão salvos, onde, este repositório sempre será limpo no início do script.
- Entrar na transação do SAP GUI para iniciar o processo, onde neste caso é uma transação ficticia.
- Executar os comandos automatizados do SAP GUI pelo script.
- Realizar a extração das bases de dados.
- Salvar as bases de dados.
- Finalizar o script.

'''

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Importação de módulos

import win32com.client  # Módulo para criação de componentes COM (Common Object Model) em Python. Pode-se tanto criar componentes para serem utilizados por outras linguagens/aplicações (servidores) quanto criar objetos previamente existentes (clientes) criados em outras linguagens.
import sys  # Módulo para fornecer funções e variáveis usadas para manipular diferentes partes do ambiente de tempo de execução do Python e apesar de serem completamente diferentes, muitas pessoas confundem o módulo sys e o módulo os (módulo para manipular o sistema operacional).
import os  # Módulo para fornecer acesso a funções específicas do sistema para lidar com o sistema de arquivos, processos, planejador, etc.
import glob  # Módulo usado para retornar todos os caminhos de arquivo que correspondem a um padrão específico.
import subprocess  # Módulo subprocess permite que você execute programas externos e inspecione suas saídas com facilidade.
import time  # Módulo provê várias funções relacionadas à tempo, onde neste caso estamos utilizando para a função (sleep).
from datetime import datetime  # Módulo fornece classes para manipular datas e tempo de forma simples ou complexas. Apesar de cálculos aritméticos com data e tempo serem suportados, o foco da implementação está na extração eficiente de atributo para formatar resultados e manipulação.
import getpass  # Módulo para mascarar a senha quando é inserida no terminal.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da data atual para inserção nos campos do SAP GUI, neste caso a variável (data).
# Variável (data_atual) formata o padrão da data.
# Essa data fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
data = datetime.now()
data_atual = data.strftime('%d.%m.%Y')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável da hora atual para inserção nos campos do SAP GUI, neste caso a variável (hora_atual).
# Essa hora fica pré definida para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
hora_atual = time.strftime('%Hh%M', time.localtime())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o endereço do caminho onde as bases de dados extraídas do SAP GUI serão salvas.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_caminho = r'C:\Users\Zézinho\ZUDWM_OT850_EQUIPS\Equipamentos'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_principal = r'\1 - Notas de equips medidores - Principal.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI. Neste caso, seria por exemplo, um arquivo complementar da extração ou um segundo arquivo de extração.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_complemento = r'\2 - Notas de equips medidores - Complemento.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável (nome_txt) que monta o nome de um arquivo no formato (txt) para indicar no final do script, a data e hora da atualização.
# Variável (nome_txt_caminho) que concatena o caminho dos arquivos da extração do SAP GUI e o arquivo montado com a informação da da variável (nome_txt).
nome_txt = r'\Atualização em ' + data_atual + ' às ' + hora_atual + '.txt'
nome_txt_caminho = nome_caminho + nome_txt

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

arquivos = glob.glob(r'C:\Users\br0234206128\Enel Spa\SM - Acompanhamento - General\Medidores Substituídos Piloto\Extrações\ZUDWM_OT300_EQUI\Medidores\*')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


def saplogin_rpa():

    #Conexão com SAP GUI.
    try:
        path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(5)

        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.OpenConnection("H181 RP1 ENEL SP CCS Produção (without SSO)", True)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

        #Variáveis de login e senha dos campos do SAP.
        login = input('Informe seu login: ')
        password = getpass.getpass('Informe sua senha: ')

        #Campos de login e senha do SAP.
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = login
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = password



        for arquivos_gerais in arquivos:
            try:
                os.remove(arquivos_gerais)
            finally:
                0

        #Scrip gerado do SAP.
        #Alguns campos dos scripts do SAP são adaptados para funcionamento.
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[0]/okcd").text = "SE16N"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtGD-TAB").text = "ZUDWM_OT300_EQUI"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
        session.findById("wnd[0]/usr/ctxtGD-VARIANT").text = "/SM_EQUI_MED"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/btnPUSH[4,8]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/btnPUSH[4,8]").press()
        session.findById("wnd[1]/usr/tblSAPLSE16NMULTI_TC/ctxtGS_MULTI_SELECT-LOW[1,0]").text = "USM*"
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectAll()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").contextMenu()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem("&XXL")
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = nome_caminho
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = nome_arquivo_principal
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        #Colocao o processo em espera por 10 segundos e aguarda até abertura do Excel.
        time.sleep(30)

        #Fecha o arquivo Excel que é aberto no final do processo de extração.
        xl = win32com.client.Dispatch('Excel.Application')
        xl.DisplayAlerts = False
        xl.Quit()

        #Scrip gerado do SAP.
        #Alguns campos dos scripts do SAP são adaptados para funcionamento.
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/tbar[0]/okcd").text = "SE16N"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtGD-TAB").text = "ZUDWM_OT300_EQUI"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/txtGD-MAX_LINES").text = ""
        session.findById("wnd[0]/usr/ctxtGD-VARIANT").text = "/SM_EQUI_ME2"
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/btnPUSH[4,2]").setFocus()
        session.findById("wnd[0]/usr/tblSAPLSE16NSELFIELDS_TC/btnPUSH[4,2]").press()
        session.findById("wnd[1]/usr/tblSAPLSE16NMULTI_TC/ctxtGS_MULTI_SELECT-LOW[1,0]").text = "USM*"
        session.findById("wnd[1]/tbar[0]/btn[8]").press()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectAll()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").contextMenu()
        session.findById("wnd[0]/usr/cntlRESULT_LIST/shellcont/shell").selectContextMenuItem("&XXL")
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = nome_caminho
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = nome_arquivo_complemento
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        #Colocao o processo em espera por 10 segundos e aguarda até abertura do Excel.
        time.sleep(30)

        #Fecha o arquivo Excel que é aberto no final do processo de extração.
        xl = win32com.client.Dispatch('Excel.Application')
        xl.DisplayAlerts = False
        xl.Quit()

        #Encerra a tela de login do SAP.
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]/tbar[0]/btn[3]").press()
        session.findById("wnd[0]").close()
        session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()

        open(nome_txt_caminho, 'a')

        #Caso haja um erro nos processos acima, haverá a mensagem de erro abaixo.
    except:
        print(sys.exc_info()[0])

    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None

saplogin_rpa()