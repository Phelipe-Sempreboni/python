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
nome_caminho = r'C:\Windows\Temp\testes'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_principal = r'\Notas - Principal.xlsx'

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Variável com o nome do arquivo que será salvo na extração do SAP GUI. Neste caso, seria por exemplo, um arquivo complementar da extração ou um segundo arquivo de extração.
# Esse caminho fica pré definido para facilitar o preenchimento no SAP GUI e controle de variáveis no script.
nome_arquivo_complemento = r'\Notas - Complemento.xlsx'

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

            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
            print('=======================================================================================================================================================================\n')

            # Imprimir mensagem abaixo para o usuário.
            print('Não existe nenhum tipo de arquivo de arquivo neste repositório. \nPor favor, verifique o repositóro e tente novamente. \nProcesso executado sem êxito. \nEssa tela será fechada em 30 segundos. \n')

            # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
            print('=======================================================================================================================================================================\n')

            # Pausar ou colocar para dormir a execução do script por 30 segundos até a execução do comando abaixo.
            time.sleep(30)

            # Comando para encerrar o script neste ponto, visando não haver erros nos processos seguintes.
            sys.exit()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

        # 4º nível de verificação de (locais - root), (repositórios - dirs), (arquivos - files).
        # Este (elif) verifica se existem arquivos de qualquer tipo de extensão no repositório.
        # Caso existam arquivos, mas nenhum com a extensão (xlsx) do tipo excel, ele irá exibir a mensagem abaixo para o usuário, que não existe um arquivo excel nesse repositório.
        # Logo após a exibição da mensagem, irá começar um contador de 30 segundos e o código será encerrado para não comprometer os processos abaixo.
        # O primeiro (elif) verifica se a variável (lista_vazia_1) é diferente de vazia e se for verdadeiro, então seguirá para a declaração das variáveis e o if aninhado com este (elif) abaixo.
        # A variável (localizar_extensao_1) procura por arquivos da extensão (xlsx) dentro da variável (files) que aponta para os arquivos do repositório.
        # Logo após, a variável (localizar_extensao_1) e (lista_vazia_2) são comparadas.
        # Caso a variável (localizar_extensao_1) seja igual a variável (lista_vazia_2), então o comando irá prosseguir para o (if aninhado com este if) abaixo.
        # Este (if) quer dizer que o valor de ambas variáveis são vazias, logo, irá imprimir a mensagem abaixo para o usuário, que não existe um arquivo com a extensão (xlsx).
        # NOTAR QUE TEMOS OUTRO (ELIF) ABAIXO, PORÉM ESTÁ ANINHADO DENTRO DESTE (IF -> if localizar_extensao_1 == lista_vazia_2).
        elif files != lista_vazia_1:

            # Variável declarada como uma lista vazia, para conseguirmos comparar caso a variável (files) seja ou não vazia, que no caso do (elif) acima, o foco é comparar se (files) não é vazio.
            lista_vazia_2 = []

            # Compara se ambas variáveis são iguais, que neste caso se ambas tem o valor de uma lista vazia, ou seja, igual à [].
            localizar_extensao_1 = [extensao_1 for extensao_1 in files if '.xlsx' in extensao_1]

            if localizar_extensao_1 == lista_vazia_2:

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('=======================================================================================================================================================================\n')

                # Imprimir mensagem abaixo para o usuário.
                print('Não existe um arquivo com a extensão (xlsx) do excel nesse repositório. \nPor favor, verifique o repositóro e tente novamente. \nProcesso executado sem êxito. \nEssa tela será fechada em 30 segundos. \n')

                # Print para realizar as divisões entre as mensagens, visando deixar a leitura do usuário mais organizada.
                print('=======================================================================================================================================================================\n')

finally:

    sys.exit()
